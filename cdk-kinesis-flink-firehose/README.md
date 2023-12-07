# Managed Service for Apache Flink Consuming from a Kinesis Data Stream and Sinking to a Firehose

The purpose of this pattern is to deploy the infrastructure necessary to enable Managed Service for Apache Flink to consume a Kinesis data stream and produce to a Firehose sink.

With Amazon Managed Service for Apache Flink, you can use Java, Scala, or SQL to process and analyze streaming data. The service enables you to author and run code against streaming sources to perform time-series analytics, feed real-time dashboards, and create real-time metrics.

Managed Service for Apache Flink provides the underlying infrastructure for your Apache Flink applications. It handles core capabilities like provisioning compute resources, parallel computation, automatic scaling, and application backups (implemented as checkpoints and snapshots). You can use the high-level Flink programming features (such as operators, functions, sources, and sinks) in the same way that you use them when hosting the Flink infrastructure yourself.

In this project, you create a Managed Service for Apache Flink application that has a Kinesis data stream as a source and a Kinesis Firehose sink. The Firehose is configured with an S3 bucket destination.

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/cdk-kinesis-flink-firehose]

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd serverless-pattern/cdk-kinesis-flink-firehose
    ```
3. From the command line, use AWS CDK to navigate into the cdk folder and deploy the infrastructure:
    ```
    cd cdk
    cdk deploy
    ```
4. When prompted, confirm that you wish to deploy the changes

5. Note the Kinesis Data Stream Name output. This value will be used for testing.

## How it works

The Managed Service for Apache Flink application runs the Java program located in the /flink-application/ folder. The DataStreamJob class defines a Kinesis Data Stream source and a Kinesis Firehose sink. It also creates a datastream execution environment sinking the stream to the firehose without any transformations. When the application is run, it becomes a consumer of the Kinesis Data Stream set to the LATEST position. Any incoming stream data is then sent to the Firehose. Separate from the Flink application, the Firehose is configured with an S3 destination.

## Testing

To test this project, follow the below steps:

1. Sign in to the AWS console at https://console.aws.amazon.com

2. From the Search bar, navigate to the Managed Apache Flink console.

3. Select the streaming application that was created as part of the dpeloyment stack.

4. Press the Run button on the upper panel of the next screen, then choose Run without snapshot and click Run. Wait until the application enters a Running state.

5. In this repository, open the file serverless-patterns/cdk-kinesis-flink-firehose/test/dataGen.py and update the STREAM_NAME variable with the Kinesis Data Stream name output from the stack. Update the REGION variable with region name where the solution is deployed. Navigate into the directory where the file is located and run:
```
python dataGen.py
```
This file will generate data and send it to the kinesis stream created as part of the solution. Note that this file uses the boto3 library and the default credentials chain for making API calls.

6. After a few minutes, navigate to the S3 console and select the bucket created as part of the deployment stack. You should see a partitioned folder structure and at the lowest level are files containining the generated data.

7. For additional validation, navigate to the Managed Apache flink streaming application again. In the upper panel of the screen, select "Open Apache Flink dashboard". In the dashboard, select Running Jobs on the left hand panel, and then the Stock Price job. The job details page contains information about records received from the stream and sent to the Firehose.

## Cleanup
 
1. Stop the Managed Apache Flink application from the console (optional but will speed up deletion process).

2. Delete the stack
    ```
    cdk destroy
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0