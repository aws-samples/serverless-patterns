# DynamoDB stream to Opensearch Serverless 
 
 This pattern allows you to stream new created item on a specific DynamoDB talbe to a Opensearch serverless collection for searching capability for DyanmoDB table.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html)
* [Install CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
  * `npm install aws-cdk-lib`

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```

2. Change directory to the pattern directory:
    ```bash
    cd dynamodb-streams-aoss
    ```

3. Install node module: 
   ```bash
   npm install
   ```

4. Deploy
   ```bash
   cdk deploy
   ```

## How it works
This pattern will create a DynamoDB table, an Opensearch Serverless collections. When any new item being created on the DynamoDB table, it will trigger the lambda function which index the item with it's partition key to the Opensearch serverless collection. Removing the item in DynamoDB will also trigger the lambda function to remove the it from the Opensearch Serverless collection. 

## Cleanup 
1. remove entire stack with command: 
   ```bash
   cdk destroy
   ```

## Useful commands

* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk synth`       emits the synthesized CloudFormation template

