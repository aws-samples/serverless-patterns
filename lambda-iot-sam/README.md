# AWS Lambda to AWS IoT Core

This pattern contains a sample AWS SAM stack to publish a message to AWS IoT Core Thing

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node and NPM](https://nodejs.org/en/download/) installed
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Clone the project to your local working directory

   ```sh
   git clone https://github.com/aws-samples/serverless-patterns/ 
   ```

2. Change the working directory to this pattern's directory

   ```sh
   cd serverless-patterns/lambda-iot-sam
   ```
3. Deploy the stack to your default AWS account and region. 

   ```sh
   sam deploy -g
   ```

### Testing Using AWS Console

1. Browse to AWS IoT Core in the AWS Management Console
2. Get the topic name from Manage -> All devices -> Thing
3. Navigate to MQTT test client
4. Subscribe to the topic created using the retrieved thing name
5. Browse to AWS Lamdba in the AWS MAnagement Console and navigate to the Lambda function specified in the SAM outputs
6. Configure  a test event in the console and run a Test invoke of the Lambda function
7. NAvigate back to the MQTT test client in AWS IoT Core Console, you will see the message appear in the MQTT test client

   ```sh
    {
      "type": "hello",
      "detail": "world"
    }
   ```

## Cleanup
 
Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted. See the Notes section in [README](./README.md)

```sh
sam delete
```

----
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. 

SPDX-License-Identifier: MIT-0
