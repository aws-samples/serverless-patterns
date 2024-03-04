# Managed Service for Apache Flink Consuming from a Kinesis Data Stream and Sinking to an S3 Bucket

The purpose of this pattern is to deploy the infrastructure necessary to enable Managed Service for Apache Flink to consume a Kinesis data stream and produce to an S3 sink.

With Amazon Managed Service for Apache Flink, you can use Java, Scala, or SQL to process and analyze streaming data. The service enables you to author and run code against streaming sources to perform time-series analytics, feed real-time dashboards, and create real-time metrics.

Managed Service for Apache Flink provides the underlying infrastructure for your Apache Flink applications. It handles core capabilities like provisioning compute resources, parallel computation, automatic scaling, and application backups (implemented as checkpoints and snapshots). You can use the high-level Flink programming features (such as operators, functions, sources, and sinks) in the same way that you use them when hosting the Flink infrastructure yourself.

In this project, you create a Managed Service for Apache Flink application that has a Kinesis data stream as a source and an S3 bucket as a sink.


Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK Toolkit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed and configured
* [Python3](https://www.python.org/downloads/) for running the test script

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd serverless-pattern/cdk-kinesis-flink-s3/flinkapp
    ```
3. Create the jar file via:
    ```
    mvn -q clean package -DskipTests
    ```
    A ```target``` folder containing the jar should be created under ```flinkapp/```.
4. From the command line, navigate into the root of the project and deploy the infrastructure:
    ```
    cd ..
    cdk deploy
    ```
4. When prompted, confirm that you wish to deploy the changes


## How it works

The Managed Service for Apache Flink application runs the Java jar file located in the flinkapp/target folder. The StreamingJob class defines a streaming execution environment. The environment defines expected properties such as input stream, region and output S3 path. When the application is run, it becomes a consumer of the Kinesis Data Stream set to the LATEST position. Any incoming stream data is then processed and sent to the S3 destination.

## Testing

To test this project, follow the below steps:

1. Sign in to the AWS console at https://console.aws.amazon.com

2. From the Search bar, navigate to the Managed Apache Flink console.

3. Select the streaming application that was created as part of the deployment stack.

4. Press the Run button on the upper panel of the next screen, then choose Run without snapshot and click Run. Wait until the application enters a Running state.

5. From the repository, find the file: `serverless-patterns/cdk-kinesis-flink-s3/test/stock.py`. Navigate into the `test` directory and run it in a separate terminal:
```
python3 stock.py
```
Keep this file running in a separate terminal for a minute. This file will generate data and send it to the kinesis stream created as part of the solution. Note that this file uses the boto3 library and the default credentials chain for making API calls.

6. After a minute or so, exit the terminal running the file. Navigate to the S3 console and select the bucket created as part of the deployment stack. You should see a partitioned folder structure and at the lowest level are files containing the generated data. Each file will count of how many times each product (in stock.py) was counted within the Flink Time Window of 1 minute.

7. For additional validation, navigate to the Managed Apache flink streaming application again. In the upper panel of the screen, select "Open Apache Flink dashboard". In the dashboard, select Running Jobs on the left hand panel, and then the Stock Price job. The job details page contains information about records received from the stream and sent to the S3 bucket.

## Cleanup
 
1. Exit the terminal running the python stock application.
2. Stop the Managed Apache Flink application from the console (optional but will speed up deletion process).

3. Delete the stack
    ```
    cdk destroy
    ```
----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
