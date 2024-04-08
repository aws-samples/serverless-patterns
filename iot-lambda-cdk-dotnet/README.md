# AWS IOT to Lambda based on IOT Rule 

The CDK stack deploys a Lambda function, an IoT thing, and the least IAM resources required to run the application.

When an IoT event is sent to an IoT topic, a Lambda function is invoked. This pattern configures a Lambda function to poll this event. The function is invoked with a payload containing the contents of the message event.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/iot-lambda-cdk-dotnet.

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
    cd iot-lambda-cdk-dotnet
    ```
1. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    cdk deploy 
    ```

## How it works

When message events are sent to a IoT topic, this event will trigger a Lambda function. This pattern configures a Lambda function to read this event. The function is invoked with a payload containing the contents of the event sent.

## Testing

The easiest way to test is using the MQTT test client.

1. In the [AWS IoT console](https://console.aws.amazon.com/iot/home), in the left menu, choose Test.

2. In the MQTT test client page, select the **Publish to a topic** tab and add the created topic name: `MyIotThing`

3. Add a message payload or use the the default one, the payload need to be in the JSON format. 
    ```bash
    {
    "message": "Hello from AWS IoT console"
    }
   ``` 

4. Click in **Publish** to send the event. After the event has been sent, the created Lambda will be triggered.

5. Go to the [Cloudwatch Log Groups](https://console.aws.amazon.com/cloudwatch/home?#logsV2:log-groups) page and search for the function Lambda name created. The SAM deployment process outputs will print the value for the **IOTProcessEventFunction**. If you are using the default one, the function name will be something like `STACK_NAME-IOTProcessEventFunction-*`, and the log group will be `/aws/lambda/STACK_NAME-IOTProcessEventFunction-*`

6. If you are able to see the logs with the sent payload, everything is working properly.


## Cleanup

Delete the stack: 
   ```bash
    cdk destroy
   ``` 

----
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
