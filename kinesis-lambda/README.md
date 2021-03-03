# AWS Kinesis Data Streams to AWS Lambda

This pattern creates an AWS Kinesis Data Stream, a stream consumer, and an AWS Lambda function. When data is added to the stream, the Lambda function is invoked.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/kinesis-to-lambda](https://serverlessland.com/patterns/kinesis-to-lambda)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* AWS CLI already configured with Administrator permission
* [NodeJS 14.x installed](https://nodejs.org/en/download/)

## Installation Instructions

1. [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and login.

1. [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [install the AWS Serverless Application Model CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) on your local machine.

1. Create a new directory, navigate to that directory in a terminal and enter ```git clone https://github.com/aws-samples/serverless-patterns```.

1. Change directory to this pattern.

1. From the command line, run:
```
sam deploy --guided
```
Choose a stack name, select the desired AWS Region, and allow SAM to create roles with the required permissions. Once you have run guided mode once, you can use `sam deploy` in future to use these defaults.

* Note the outputs from the SAM deployment process. These contain the resource names and ARNs.

## Testing

Use the Amazon Kinesis Data Generator for testing. The easiest way to use this tool is to use the [hosted generator](https://awslabs.github.io/amazon-kinesis-data-generator/web/producer.html) and follow the [setup instructions](https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html).

After you have the generator configured, you should have a custom URL to generate data for your Kinesis data stream. In your configuration steps, you created a username and password. Log in to the generator using those credentials.

When you are logged in, you can generate data for your stream test.

1. Choose the region you deployed the application to
1. For Stream/delivery stream, select your stream.
1. For Records per second, keep the default value of 100.
1. On the Template 1 tab, name the template Sensor1.
1. Use the following template:
    ```JSON
    {
        "sensorId": {{random.number(50)}},
        "currentTemperature": {{random.number(
            {
                "min":10,
                "max":150
            }
        )}},
        "status": "{{random.arrayElement(
            ["OK","FAIL","WARN"]
        )}}"
    }
    ```
1. Choose Send Data.
1. After several seconds, choose Stop Sending Data.


----
Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0