# AWS Service 1 to AWS Service 2

This pattern builds a predictive maintenance pipeline using Iot Core for ingestion of sensor data, Amazon Lookout for equipment for ML anomaly detection, and SNS for notification. It demonstrates how you can leverage AWS ML to predict equipment failure.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/cdk-predictive-maintenance-lookout-sns

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1.  Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1.  Change directory to the pattern directory:
    ```
    cd _patterns-model
    ```
1.  To manually create a virtualenv on MacOS and Linux:

    ```
    $ python3 -m venv .venv
    ```

1.  After the init process completes and the virtualenv is created, you can use the following
    step to activate your virtualenv.

        ```
        $ source .venv/bin/activate
        ```

If you are a Windows platform, you would activate the virtualenv like this:

    ```
    % .venv\Scripts\activate.bat
    ```

1. Once the virtualenv is activated, you can install the required dependencies.

   ```
   $ pip install -r requirements.txt
   ```

1. Then bootstrap your cloud environment

   ```
   $ cdk bootstrap aws://ACCOUNT-NUMBER/REGION
   ```

1. At this point you can now synthesize the CloudFormation template for this code.

   ```
   $ cdk synth
   ```

1. Then deploy the cdk construct using **\*your** email
   ```
   $ cdk deploy PredictiveMaintenanceAppStack --parameters EmailParameter=<email>
   ```
1. Ensure your IoT devices or simulator can effectively communicate with IoT Core by using MQTT test client to subscribe to the IoT topic.

- In the IoT Core Rule, ensure that you edit the SQL statement to the appropriate SQL for your IoT devices and add a `,` seperator or whatever seperator used in your data to the Kinesis Firehose Stream Action.

1.  Create a model and schedule inferencing on Amazon Lookout for Equipment on the console and connect it to the input and output buckets created from the stack. To learn how to to do this watch this [video](https://www.youtube.com/watch?v=N_eCUxrsPr0&feature=youtu.be)
1.  Add a prefix/sub-directory `output/` to the S3 output bucket.

## How it works

You will use for IoT Core and Kinesis for ingesting sensor data in real time, Amazon Lookout for Equipment to do the ML anamoly detection and SNS notification via email.

## Testing

Connect this deployment to your sensors (you can use AWS IoT Device simulator if you need it) and an Lookout inference model (video above show how to make one). Go to the Lookout console page and you should see a graph with your anomaly data. You will also recieve an email if an anomaly is detected.

## Cleanup

1. Delete the stack
   ```bash
   cdk destroy
   ```
1. Confirm the stack has been deleted
   ```bash
   aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'STACK_NAME')].StackStatus"
   ```

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
