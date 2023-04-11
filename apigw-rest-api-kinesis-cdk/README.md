# Amazon API Gateway to Amazon Kinesis 

This pattern creates an Amazon API Gateway REST API that integrates with an Amazon Kinesis data stream.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd apigw-rest-api-kinesis-cdk/cdk
    ```
1. Install dependencies
    ```
    npm install
    ```
1. Deploy the stack to your default AWS account and region. The output of this command should give you the HTTP API URL
   ```
   cdk deploy
   ```
   
## How it works

This pattern creates an Amazon API Gateway REST API that integrates directly with an Amazon Kinesis data stream. The API supports GET requests to list the details of your Kinesis stream and there is no authentication on the API endpoint. 

Below is an illustration of the general Amazon API Gateway Integration pattern.

![alt text](https://github.com/MudassarBashir/serverless-patterns/blob/mmbashir-apigw-rest-api-kinesis-cdk/apigw-rest-api-kinesis-cdk/apigw-kinesis-architecture-diagram.png?raw=true)

## Testing

Upon deployment, you will see the API endpoint URL in the Outputs section of your deployed CloudFormation stack. Click on the API URL. It will take this format:
  ```
  https://${API_ID}.execute-api.${REGION_NAME}.amazonaws.com/{DEPLOYMENT_STAGE}
  ```
### Response Elements
  
If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

  ```json
  {"HasMoreStreams":false,"StreamNames":["temp-stream"],"StreamSummaries":[{"StreamARN":"arn:aws:kinesis:{AWS_REGION}:{AWS_ACCOUNT_NUMBER}:stream/temp-stream","StreamCreationTimestamp":1.681224803E9,"StreamModeDetails":{"StreamMode":"PROVISIONED"},"StreamName":"temp-stream","StreamStatus":"ACTIVE"}]}
  ```

* [HasMoreStreams](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreams.html#API_ListStreams_ResponseSyntax:~:text=by%20the%20service.-,HasMoreStreams,-If%20set%20to)

* [StreamNames](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ListStreams.html#API_ListStreams_ResponseSyntax:~:text=length%20of%201048576.-,StreamNames,-The%20names%20of)

* [StreamSummaries](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_StreamSummary.html)


## Cleanup
 
1. Run the command to delete the stack
    ```
    cdk destroy
    ```
    
## Documentation

* [Tutorial: Create a REST API as an Amazon Kinesis proxy in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aws-services-kinesis.html)
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
