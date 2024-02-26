# Hello

This is a repo to store some examples of my work. The main motivation being that employers can see examples of work I have done.

These projects represent personal projects, often done with limited time and on a 'get things done' basis.

Currently the repo has in it: 
- **lamba_function(petrolAPI).py**. This is a function I built to run on AWS Lamba. It is paired with a time trigger in EventBridge, which triggers it daily. It calls a few public API's, collecting fuel prices for all service stations in New South Wales and Tasmainia, calculates some relevant statistics, pulls out a csv from S3 which has all previous records, adds todays values and writes it back to S3. This was part of a project where I wanted to see whether I could effeciently collect prices of goods and services across Australia using AWS serverless products.
  
- 

If you aren't and employer, and are instead thinking of using the code for your own project, feel free to.

Enjoy, 
Sam
