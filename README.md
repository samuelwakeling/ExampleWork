# Hello

This is a repo to store some examples of my work. The main motivation being that employers can see examples of work I have done.

These projects represent personal projects, often done with limited time and on a 'get things done' basis.

Currently the repo has in it: 
- **lamba_function(petrolAPI).py**. This is a function I built to run on AWS Lamba. It is paired with a time trigger in EventBridge, which triggers it daily. It calls a few public API's, collecting fuel prices for all service stations in New South Wales and Tasmainia, calculates some relevant statistics, pulls out a csv from S3 which has all previous records, adds todays values and writes it back to S3. This was part of a project where I wanted to see whether I could effeciently collect prices of goods and services across Australia using AWS serverless products.
  
- **AES_marriage_equality.Rmd**. This is a project I wrote in 2020. I was really keen to learn networkD3 and how to make interactive visualisation. I was also amazed the the Australian Election Study (AES) data was publically available, as well as longitudinal. I had also listened recently to a podcast about status quo rationalisation, where people change their position on an issue after they become legislated (or reality). I thought marriage equality (which had been asked about in the AES in both 2016 and 2019 might be an interesting example of this effect - and a good excuse to make an interactive sankey! The output of this file is 

If you aren't and employer, and are instead thinking of using the code for your own project, feel free to.

Enjoy, 
Sam
