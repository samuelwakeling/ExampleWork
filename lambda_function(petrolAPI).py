#This Lambda function is designed to collect all fuel prices daily across NSW and TAS. 
#It calls the API, does a bit of wrangling, fetches the latest updated csv from S3, adds in the new values, and writes it back out to S3. 

import requests
import json
import datetime
import pandas as pd
import io
import boto3
import numpy as np



def lambda_handler(event, context):

#token stored as environmental variable
  access_token = os.environ.get('FUEL_API_TOKEN')

#request latest price for each site file. 
  url_prices = "https://fppdirectapi-prod.fuelpricesqld.com.au/Price/GetSitesPrices?countryId=21&geoRegionLevel=3&geoRegionId=1"

  headers = {
      'content-type': "application/json",
      'authorization': access_token
      }

  prices = requests.request("GET", url_prices, headers=headers)

  b = json.loads(prices.text)
  c = pd.json_normalize(b['SitePrices'])
  
  c['Price'] = c['Price']/10 #take it to cents.
  c = c.loc[c["Price"] != 999.9]
  c = c.loc[c["Price"] != 888.8]
  c = c.loc[c["Price"] != 0]

# request fuel type mapping file (digit coding to name of fuel)
  url_fueltypes = "https://fppdirectapi-prod.fuelpricesqld.com.au/Subscriber/GetCountryFuelTypes?countryId=21"

  headers2 = {
      'content-type': "application/json",
      'authorization': access_token
      }

  fuel_types = requests.request("GET", url_fueltypes, headers=headers2)

  d = json.loads(fuel_types.text)
  e = pd.json_normalize(d['Fuels'])

#join types/names to fueltype IDs. 
  df = pd.merge(c,e, on='FuelId', how = 'inner')

#convert to csv in temp file to write to s3
  csv_buffer = io.StringIO()
  df.to_csv(csv_buffer)

  file_contents = csv_buffer.getvalue()

# Create an S3 client
  s3 = boto3.client('s3')
  

# create time stamp for saving file name. 
  timestamp = datetime.datetime.now()
  timestamp = timestamp + datetime.timedelta(hours=10)
  timestamp = timestamp.strftime('%d-%m-%Y %H:%M:%S')

# Export the data to S3
  s3.put_object(Bucket='transport-fuelapi-qld', 
					Body=file_contents, 
					Key='rawdata/transport-fuelapi-qld{}.csv'.format(timestamp))
  
# this section takes geo/arithmetic/median/ and writes it to a master spreadsheet

  #function for geo mean
  def geometric_mean(x):
      a = np.log(x)
      return np.exp(a.mean())

  daily_means = df.groupby("Name").Price.agg([pd.Series.mean, pd.Series.median, geometric_mean])

  daily_means = daily_means.reset_index()

  daily_means.columns = ["item", "a_mean", "median", "g_mean"]

  daily_means['category'] = "transport"

  daily_means['group'] = "fuel"

  daily_means['datestamp'] = timestamp

  daily_means['state'] = 'QLD'

#standardise with nsw and tas fuel types 

  fuel_mapping = {
  'Diesel' : 'DL',
  'LPG' : 'LPG',
  'OPAL' : 'OPAL',
  'Premium Diesel' : 'PDL',
  'Premium Unleaded 95' : 'P95',
  'Premium Unleaded 98' : 'P98',
  'Unleaded' : 'U91',
  'e10' : 'E10',
  'e85' : 'E85'}

  daily_means['item'] = daily_means['item'].replace(fuel_mapping)

#fetch master sheet, add the prices, and save back to S3.
  try:
    # Try to fetch the S3 object
    obj = s3.get_object(Bucket="sure-thing-means-series", Key="transport_means.csv")
    content = obj["Body"].read().decode("utf-8")

    # Load the CSV file into a Pandas DataFrame
    df_historic = pd.read_csv(io.StringIO(content))
  except s3.exceptions.NoSuchKey:
    # If the file doesn't exist, create an empty DataFrame
    df_historic = pd.DataFrame(columns=["state", "category", "group", "item", "datestamp", "a_mean", "g_mean", "median"])

    # Concatenate the new DataFrame with the existing DataFrame
  df_historic = pd.concat([df_historic, daily_means], ignore_index=True)

    # Save the updated DataFrame back to S3
  s3.put_object(Bucket="sure-thing-means-series", Key="transport_means.csv", Body=df_historic.to_csv(index=False).encode("utf-8"))


  return {
  'statusCode': response.status_code,
  'body': response.text
        }
