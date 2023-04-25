# Amazon API Gateway to Amazon Kinesis 

This pattern creates an Amazon API Gateway REST API that integrates with an Amazon Kinesis data stream using AWS Cloud Development Kit (AWS CDK) in Typescript.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

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

The API built in this pattern exposes HTTP GET and PUT methods on the API's resource. It integrates the method with the [ListStreams](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreams.html) action in Kinesis to list the streams in the caller's account, the [GetShardIterator](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html) action to get a shard iterator from a stream, the [PutRecord](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html) action to write a record into a stream, and the [GetRecords](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetRecords.html) action to get data records from a data stream's shard. There is no authentication on the API endpoint. 

Below is an illustration of the general Amazon API Gateway Integration pattern:

![alt text](https://github.com/MudassarBashir/serverless-patterns/blob/mmbashir-apigw-rest-api-kinesis-cdk/apigw-rest-api-kinesis-cdk/apigw-kinesis-architecture-diagram.png?raw=true)

## Testing

1. Upon deployment, you will see the API endpoint URL in the **Outputs** section of your deployed CloudFormation stack. Click on the API URL. It will take this format:
  ```
  https://${API_ID}.execute-api.${REGION_NAME}.amazonaws.com/{DEPLOYMENT_STAGE}
  ``` 
   If the action is successful, the service sends back an HTTP 200 response. The following data is returned in JSON format by the [ListStreams](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreams.html) API:

  ```json
  {"HasMoreStreams":false,"StreamNames":["temp-stream"],"StreamSummaries":[{"StreamARN":"arn:aws:kinesis:{AWS_REGION}:{AWS_ACCOUNT_NUMBER}:stream/temp-stream","StreamCreationTimestamp":1.681224803E9,"StreamModeDetails":{"StreamMode":"PROVISIONED"},"StreamName":"temp-stream","StreamStatus":"ACTIVE"}]}
  ```


2. Now that you have the details about your stream, you are ready to input some data. For testing the [put-record](https://docs.aws.amazon.com/streams/latest/dev/fundamental-stream.html#put-record:~:text=%22Foo%22%0A%20%20%20%20%5D%0A%7D-,Step%202%3A%20Put%20a%20Record,-Now%20that%20you) command, input this into the CLI using the "StreamName" output in step 1:
   ```
   aws kinesis put-record --stream-name temp-stream --partition-key 123 --data testdata
   ```
   This command, if successful, will result in output similar to the following example:
    
  ```json
   {
   "ShardId": "shardId-000000000000",
    "SequenceNumber": "49546986683135544286507457936321625675700192471156785154"
    }
  ```
  
3. Before you can get data from the stream you need to obtain the shard iterator for the shard you are interested in. A shard iterator represents the position of the stream and shard from which the consumer (get-record command in this case) will read. You'll use the [get-shard-iterator](https://docs.aws.amazon.com/streams/latest/dev/fundamental-stream.html#put-record:~:text=Get%20the%20Record-,GetShardIterator,-Before%20you%20can) command, as follows:

    ```
    aws kinesis get-shard-iterator --shard-id shardId-000000000000 --shard-iterator-type TRIM_HORIZON --stream-name temp-stream
    ```
    
  This command, if successful, will result in output similar to the following example:
   ```json
   {
    "ShardIterator": "AAAAAAAAAAHSywljv0zEgPX4NyKdZ5wryMzP9yALs8NeKbUjp1IxtZs1Sp+KEd9I6AJ9ZG4lNR1EMi+9Md/nHvtLyxpfhEzYvkTZ4D9DQVz/mBYWRO6OTZRKnW9gd+efGN2aHFdkH1rJl4BL9Wyrk+ghYG22D2T1Da2EyNSH1+LAbK33gQweTJADBdyMwlo5r6PqcP2dzhg="
}
   ```
   
4. The shard iterator specifies the position in the shard from which you want to start reading data records sequentially. If there are no records available in the portion of the shard that the iterator points to, [get-records](https://docs.aws.amazon.com/streams/latest/dev/fundamental-stream.html#put-record:~:text=iterator%20command%20again.-,GetRecords,-The%20get%2Drecords) returns an empty list. Note that it might take multiple calls to get to a portion of the shard that contains records.

Enter this command below and replace the shard-iterator with the "ShardIterator" output you received from step 3:
   
   ```
aws kinesis get-records --shard-iterator AAAAAAAAAAHSywljv0zEgPX4NyKdZ5wryMzP9yALs8NeKbUjp1IxtZs1Sp+KEd9I6AJ9ZG4lNR1EMi+9Md/nHvtLyxpfhEzYvkTZ4D9DQVz/mBYWRO6OTZRKnW9gd+efGN2aHFdkH1rJl4BL9Wyrk+ghYG22D2T1Da2EyNSH1+LAbK33gQweTJADBdyMwlo5r6PqcP2dzhg=
   ```

This command, if successful, will result in output similar to the following example:
    
   ```json
   {
  "Records":[ {
    "Data":"dGVzdGRhdGE=",
    "PartitionKey":"123”,
    "ApproximateArrivalTimestamp": 1.441215410867E9,
    "SequenceNumber":"49544985256907370027570885864065577703022652638596431874"
  } ],
  "MillisBehindLatest":24000,
  "NextShardIterator":"AAAAAAAAAAEDOW3ugseWPE4503kqN1yN1UaodY8unE0sYslMUmC6lX9hlig5+t4RtZM0/tALfiI4QGjunVgJvQsjxjh2aLyxaAaPr+LaoENQ7eVs4EdYXgKyThTZGPcca2fVXYJWL3yafv9dsDwsYVedI66dbMZFC8rPMWc797zxQkv4pSKvPOZvrUIudb8UkH3VMzx58Is="
}
   ```
    
    
    
## Cleanup
 
1. Run the command to delete the stack:
    ```
    cdk destroy
    ```
2. Confirm the stack has been deleted:
    ```
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'ApigwKinesisIntegrationStack')].StackStatus
    ```
 3. You should see a message confirming **DELETE_COMPLETE**
    
## Documentation

* [Tutorial: Create a REST API as an Amazon Kinesis proxy in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aws-services-kinesis.html)
* [How do I use API Gateway as a proxy for another AWS service?](https://repost.aws/knowledge-center/api-gateway-proxy-integrate-service)
* [Amazon API Gateway API request and response data mapping reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/request-response-data-mappings.html)
* [API Gateway mapping template and access logging variable reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html) 
* [Perform BasicKinesis Data Stream Operations Using the AWS CLI](https://docs.aws.amazon.com/streams/latest/dev/fundamental-stream.html#put-record)
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
