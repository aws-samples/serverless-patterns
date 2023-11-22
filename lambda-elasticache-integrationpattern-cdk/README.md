# AWS Lamda to Amazon ElastiCache integration pattern with CDK

Customers may want to connect to ElastiCache from their core lambda function(s) for use cases that involve fast read-write operations and improve latency of applications.In application like Leader board, Queue/wait-list , API rate limiting & Quota management, etc. that are built on Serverless platform there would a lambda that is computing would integrate with a either Redis or Memcache on Amazon ElastiCache. This documentation provides a quick start guide to launch Redis cluster in Amazon ElastiCache in a defined VPC and  creates a lambda function that read writes from the Cache. Customer can further modify the code in lambda function as per their requirements. Customers can also configure Memcached by modifying the config and change their lambda appropriately.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/?aws-products-pricing.sort-by=item.additionalFields.productNameLowercase&aws-products-pricing.sort-order=asc&awsf.Free%20Tier%20Type=*all&awsf.tech-category=*all) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

1. Create an [AWS account](https://portal.aws.amazon.com/billing/signup?redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start/email) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
2. [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed and configured
3. Git Installed
4. [Node and NPM](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
5. [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) installed

## Deployment Instructions
1. Open choice of terminal/command line. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository: 
`git clone https://github.com/aws-samples/serverless-patterns`
2. Change directory to the pattern directory: 
`cd lambda-elasticache-integrationpattern-cdk`
3. Run below command to install required dependancies: 
`npm install`
4. Change the VPC details to desired VPC, Redis cluster would be created in your defined VPC. Line 22-25 on the file lib/lambda-elasticache-integrationpattern-cdk-stack.ts. If you are planing to deploy cache in private subnet or a particular list of subnets then modify the line 48 appropriately.
5. From the command line, run: `cdk deploy`. 
6. CDK would display all the changes it will make to your AWS environment, accept the changes to deploy.
7. It will take 15 mins to deploy rsources and once it is complete the confirmation would be displayed on command line/terminal. 
8. You can go to AWS Console/Search for Cloud Formation and look for stack name LambdaElasticacheIntegrationpatternCdkStack and monitor the events during deployment.


## Testing
1. Navigate to AWS Console and search for Cloud Formation 
2. Click on Stacks on left and  find the recently deployed pattern stack , name LambdaElasticacheIntegrationpatternCdkStack. 
3. Click on the stack name and click on the resources tab 
4. Find the lambda function , look for Type = AWS::lambda::Function and open the lambda function by clicking on the URL. The function name would be something like LambdaElasticacheIntegrat-ElasticacheRedisAccessXXXX
5. Follow the steps on lamdba console testing guide [here](https://docs.aws.amazon.com/lambda/latest/dg/testing-functions.html). For this lambda the test event cam be empty or you can leave to default hello-world. 
`{"key1": "value1", "key2": "value2", "key3": "value3"}`

## Cleanup
To delete the stack, run: 
`cdk destroy --all`

## Useful commands

* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk synth`       emits the synthesized CloudFormation template
