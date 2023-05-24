# Amazon API Gateway to Amazon Kinesis 

This pattern creates an Amazon API Gateway REST API that integrates with an Amazon Kinesis data stream using AWS Cloud Development Kit (AWS CDK) in Typescript.

Learn more about this pattern at Serverless Land Patterns: [serverlessland.com/patterns/apigw-kinesis-typescript-cdk](https://serverlessland.com/patterns/apigw-kinesis-typescript-cdk)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed
* [Node and NPM](https://nodejs.org/en/download) installed
* [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd apigw-rest-api-kinesis-cdk/cdk
    ```
1. Use npm to install dependencies:
    ```
    npm install
    ```
1. Deploy the stack to your default AWS account and region. The output of this command should give you the HTTP API URL
   ```
   cdk deploy
   ```
   
## How it works

The API built in this pattern exposes HTTP GET and PUT methods on the API's resources. It integrates the methods with the [ListStreams](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreams.html) API in Kinesis to list the streams in the caller's account, the [GetShardIterator](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html) API to get a shard iterator from a stream, the [PutRecord](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html) API to write a record into a stream, and the [GetRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetRecords.html) API to get data records from a data stream's shard. There is no authentication on the API endpoint. 

Below is an illustration of the general Amazon API Gateway Integration pattern:

![alt text](https://github.com/MudassarBashir/serverless-patterns/blob/mmbashir-apigw-rest-api-kinesis-cdk/apigw-rest-api-kinesis-cdk/apigw-kinesis-architecture-diagram.png?raw=true)

## Testing

1. Upon deployment, you will see the API endpoint URL in the **Outputs** section of your deployed CloudFormation stack. It will take this format:

  ```
  https://${API_ID}.execute-api.${REGION_NAME}.amazonaws.com/prod
  ``` 
  This will form the base URI for any requests made to the API Gateway. For example, to invoke the ListStreams API, we use the following `curl` commmand:
```
curl https://${API_ID}.execute-api.${REGION_NAME}.amazonaws.com/prod/kinesis
```
and get a response similar to the following,
  ```json
  {"HasMoreStreams":false,"StreamNames":["temp-stream"],"StreamSummaries":[{"StreamARN":"arn:aws:kinesis:{AWS_REGION}:{AWS_ACCOUNT_NUMBER}:stream/temp-stream","StreamCreationTimestamp":1.681224803E9,"StreamModeDetails":{"StreamMode":"PROVISIONED"},"StreamName":"temp-stream","StreamStatus":"ACTIVE"}]}
  ```


2. Now that we know what streams there are, we can try to insert records. For testing the PutRecord API, enter the following `curl` command in the terminal and replace the variables in the brackets with your specific values found in step 1:
 
```
curl --location --request PUT 'https://{API_ID}.execute-api.{AWS_REGION}.amazonaws.com/prod/kinesis/{STREAM_NAME}/records' \
--header 'Content-Type: application/json' \
--data '{
    "Data": "abc123",
    "PartitionKey": "123",
    "StreamName": "{STREAM_NAME}"
}'
```
   This command, if successful, will result in output similar to the following:
    
  ```json
   {
   "Encryption": "KMS",
   "SequenceNumber": "49546986683135544286507457936321625675700192471156785154",
   "ShardId": "shardId-000000000000"
   }
  ```
  
3. Before we can get records from a stream, we need to obtain a shard iterator on the stream's shard which contains the record. A shard iterator represents the position of the stream and the shard from which the consumer will read. For testing the GetShardIterator API, enter the following `curl` command in the terminal and replace the variables in the brackets with your specific values found in step 1:

    ```
    curl --location 'https://{API_ID}.execute-api.{AWS_REGION}.amazonaws.com/prod/kinesis/{STREAM_NAME}/sharditerator?shard-id=0'
    ```
    
  This command, if successful, will result in output similar to the following example:
   ```json
   {
    "ShardIterator": "AAAAAAAAAAE1YXZFNAqJi4JXjyGww5DpbNxTQ5kIeRFYKCw2wtZw9zpAKMVolVf3IRN+lASki/fHs2PrDvjHb2Xl41bPojLmz0RlVrjOIoLFdjydDcVgkyF+ma+12RFFOtwXbIumDVTDYOHKx790TWoLCEBKR4RPbhtq0aOm7aTEegMpgi3t0VhpsYp7wB3KlLML31moO+ZKisMCInI0uEPNoxamBF3xysMrOZ/ZFR9fX/fYXk7SMg=="
}
   ```
   
4. The shard iterator specifies the position in the shard from which you want to start reading data records sequentially. If there are no records available in the portion of the shard that the iterator points to, the GetRecords API returns an empty list. Note that it might take multiple calls to get to a portion of the shard that contains records. For testing the GetRecords API, enter the following `curl` command in the terminal and replace the variables in the brackets with your specific values found in step 1, as well as the value of "ShardIterator" value found in step 3:

   ```
   curl --location 'https://{API_ID}.execute-api.{AWS_REGION}.amazonaws.com/prod/kinesis/{STREAM_NAME}/records' \ --header 'Shard-Iterator: {SHARD_ITERATOR}'
   ```

This command, if successful, will result in output similar to the following example (if records are found):
    
   ```json
   {
  "Records":[ {
    "Data":"abc123",
    "PartitionKey":"123",
    "ApproximateArrivalTimestamp": 1.441215410867E9,
    "SequenceNumber":"49544985256907370027570885864065577703022652638596431874"
  } ],
  "MillisBehindLatest":24000,
  "NextShardIterator":"AAAAAAAAAAE1YXZFNAqJi4JXjyGww5DpbNxTQ5kIeRFYKCw2wtZw9zpAKMVolVf3IRN+lASki/fHs2PrDvjHb2Xl41bPojLmz0RlVrjOIoLFdjydDcVgkyF+ma+12RFFOtwXbIumDVTDYOHKx790TWoLCEBKR4RPbhtq0aOm7aTEegMpgi3t0VhpsYp7wB3KlLML31moO+ZKisMCInI0uEPNoxamBF3xysMrOZ/ZFR9fX/fYXk7SMg=="
}
   ```
    
    
    
## Cleanup
 
1. Run this command to delete the stack:
    ```
    cdk destroy
    ```
2. Confirm the stack has been deleted:
    ```
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'ApigwKinesisIntegrationStack')].StackStatus"
    ```
 3. You should see a message confirming **DELETE_COMPLETE**
    
## Documentation

* [Tutorial: Create a REST API as an Amazon Kinesis proxy in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aws-services-kinesis.html)
* [How do I use API Gateway as a proxy for another AWS service?](https://repost.aws/knowledge-center/api-gateway-proxy-integrate-service)
* [Amazon API Gateway API request and response data mapping reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/request-response-data-mappings.html)
* [API Gateway mapping template and access logging variable reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html) 

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
