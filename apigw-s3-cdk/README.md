# REST API as an Amazon S3 proxy in API Gateway

This pattern in CDK offers a boilerplate to generate an Amazon API Gateway REST API endpoint to Amazon S3 with the following methods -
* Expose GET on the API's root resource to list all of the Amazon S3 buckets of a caller
* Expose GET on a Folder resource to view a list of all of the objects in an Amazon S3 bucket
* Expose GET on a Folder/Item resource to view or download an object from an Amazon S3 bucket
* Expose PUT on a Folder/Item resource to upload an object to an Amazon S3 bucket
* Expose HEAD on a Folder/Item resource to get object metadata in an Amazon S3 bucket 

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory its source code folder:
    ```bash
      cd apigw-s3-cdk/cdk
    ```
3. From the command line, use npm to install the development dependencies:
    ```bash
      npm install
    ```
4. To deploy from the command line use the following:
    ```bash
      cdk deploy
    ```

## Testing

### Invoke Amazon S3 proxy API using Postman

1. After deployment, the output shows the API Gateway URL with the S3 integration - base url, for example: ```ApigwS3CdkStack.S3ObjectsApiEndpoint<random> = https://<random-id>.execute-api.us-east-1.amazonaws.com/prod/```.
2. Launch Postman.
3. Choose Authorization and then choose AWS Signature. Type your IAM user's Access Key ID and Secret Access Key into the AccessKey and SecretKeyinput fields, respectively. Type the AWS region to which your API is deployed in the AWS Region text box. Type execute-api in the Service Name input field. 
4. To list all of the Amazon S3 buckets of a caller, send a GET request to the base url from step 1
5. To view a list of all of the objects in an Amazon S3 bucket, send a GET request to {base url}/{bucketName}
6. To view or download an object from an Amazon S3 bucket, send a GET request to {base url}/{bucketName}/{item}
7. To upload an object to an Amazon S3 bucket, send a PUT request to {base url}/{bucketName}/{item}. Make sure a body is present with the request.
8. To get object metadata in an Amazon S3 bucket,  send a HEAD request to {base url}/{bucketName}/{item}
* {item} is the path to the object. For example, 
  * if the item 'README.md' is in 'apig-demo' bucket, then use {base url}/apig-demo/README.md
  * if the item 'README.md' is in a folder 'docs' under 'apig-demo' bucket, then use {base url}/apig-demo/docs%2FREADME.md 

## Documentation
- [Tutorial: Create a REST API as an Amazon S3 proxy in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/integrating-api-with-aws-services-s3.html)
- [How do I use API Gateway as a proxy for another AWS service?](https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-proxy-integrate-service/)
- [Amazon API Gateway API request and response data mapping reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/request-response-data-mappings.html)
- [API Gateway mapping template and access logging variable reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html)

## Cleanup
 
1. From the command line, use the following in the source folder
    ```bash
    cdk destroy
    ```
2. Confirm the removal and wait for the resource deletion to complete.


----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0