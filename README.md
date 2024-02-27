# Hello

This is a repo to store some examples of my work. The main motivation being that employers can see examples of work I have done.

These projects represent personal projects, often done with limited time and on a 'get things done' basis.

Currently the repo has in it: 
- **lamba_function(petrolAPI).py**. This is a function I built in 2023 to run on AWS Lamba. It is paired with a time trigger in EventBridge, which triggers it daily. It calls a few public API's, collecting fuel prices for all service stations in New South Wales and Tasmania, calculates some relevant statistics, pulls out a csv from S3 which has all previous records, adds today’s values and writes it back to S3. This was part of a project where I wanted to see whether I could efficiently collect prices of goods and services across Australia using AWS serverless products.

- **Water_Quality_Sydneys_Northern_Beaches.ipynb**. I did this project in 2022 as part of General Assemblys' Data Science course. As a keen surfer, water quality is something I have always been aware of. During La Nina, it became apparent that the governments Beachwatch water quality warnings weren't very accurate. I scored great waves on 'do not swim due to water pollution' days and had some smelly sessions when the water quality was meant to be OK. After some research I discovered that the warnings were simply based on rainfall from the last 2-3 days. 25mm or more and beaches were marked as polluted. The actual bacteria testing took days to run, but there was a publicly available dataset I could use. I hypothesised that other factors which I could collect data on would be relevant: UV (which kills bacteria), tides, swell, wind (mixing of water), temperature (where certain temperatures can suppress bacteria growth, and warm temperatures can accelerate it). I went ahead and collected this data, tried a few models (this notebook has linear regression and random forest, but I did try others in another workbook). When push came to shove, my models performed badly (demonstrated by a lack of predictive power on test data). When I looked closely I could see the models performed terribly for extreme values. As these extreme values are the most important to know about, I called it a day. The extreme values may have represented events I could have never modelled; sewerage pipes bursting or groms with shovels emptying a lagoon to surf the 'lagoon wave'. 
    
- **AES_marriage_equality.Rmd**. This is a project I wrote in 2020. I was keen to learn networkD3 and how to make interactive visualisations. I was amazed the Australian Election Study (AES) data was publicly available, as well as longitudinal. I had recently listened recently to a podcast about status quo rationalisation, where people change their position on an issue after they become legislated (or reality). I thought marriage equality (which had been asked about in the AES in both 2016 and 2019) might be an interesting example of this effect - and a good excuse to make an interactive sankey! The output of this file is **SankeyMarkdown.html**. To view it you will need to first download the file, then open it in any browser.

If you aren't and employer and are instead thinking of using the code for your own project, feel free to.

Enjoy, 
Sam


