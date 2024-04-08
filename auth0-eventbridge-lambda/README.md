# Auth0 Amazon EventBridge Partner Integration to AWS Lambda

This pattern demonstrates how to use the Auth0 Amazon EventBridge SaaS integration and AWS Lambda to process events from Auth0. This pattern is leveraging the Auth0 Amazon EventBridge SaaS integration to send login events from the customer's Auth0 account to their AWS account, via an Amazon EventBridge Partner event bus. Once the Auth0 events are in the customer's account, an Amazon EventBridge rule routes suspicious login events to a downstream Lambda function. In production cases, the Lambda function could transform the event, send it to a downstream application, archive it, or send a notification email to a customer using SES. Amazon CloudWatch Log Groups are provisioned for debugging and auditing. This pattern deploys two EventBridge rules, one Lambda function, and two CloudWatch Log Groups.
    
Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/auth0-eventbridge-lambda

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS CDK CLI](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS CDK) installed
* [Create an Auth0 Account](https://auth0.com/signup?place=header&type=button&text=sign%20up) if you do not already have one and log in. 
* [Set up the Auth0 Amazon EventBridge SaaS integration](https://marketplace.auth0.com/integrations/amazon-log-streaming) if you have not already configured the integration.


## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd auth0-eventbridge-lambda
    ```
3. From the command line, use AWS CDK to deploy the AWS resources for the pattern as specified in the app.py file. A command-line argument is needed to deploy the CDK stack, "auth0EventBusName". This argument should be the name of the **SaaS event bus** associated with your Auth0 [partner event source](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-saas.html).
    ```
    cdk deploy --parameters auth0EventBusName=SAAS_EVENT_BUS_NAME_HERE
    ```

4. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing. This stack will output the name of the Lambda function deployed for testing to the CLI. See the example below. 

```
Outputs:
Auth0IntegrationStack.Auth0ProcessFailedLoginLambdaOutput = Auth0IntegrationStack-Auth0ProcessFailedLoginLambd....
```

## How it works

This service interaction uses an existing Auth0 SaaS integration in the customer's AWS account. If you do not have the Auth0 SaaS integration set up in your AWS account, please set it up before deploying this pattern. View the [integration on Auth0's marketplace](https://marketplace.auth0.com/integrations/amazon-log-streaming). See [Auth0's Log documentation](https://auth0.com/docs/deploy-monitor/logs) for available events. 

This pattern demonstrates how to:
1. Write EventBridge rules that match Auth0's event pattern
2. Send events from Auth0's EventBridge SaaS integration to Amazon CloudWatch for logging and debugging
3. Transform Auth0 events using AWS Lambda

See the below architecture diagram from the data flow of this pattern. 

![Architecture Diagram](/serverless-patterns/auth0-eventbridge-lambda/img/readme-arch-diagram.pngreadme-arch-diagram.png)

## Testing

### Test the AWS Lambda Function

The event.json file included in this pattern is a sample EventBridge event from Auth0. This event can be used to test the Lambda function and EventBridge rules deployed by this pattern.

To test the Lambda function via the CLI, copy and paste the following command, replacing the variables in <> with your own values:
```
aws lambda invoke --function-name <Auth0IntegrationStack-Auth0ProcessFailedLoginLambd-....> --payload file://event.json --cli-binary-format raw-in-base64-out response.json
```

You should receive a response that looks like: 
```
{
    "StatusCode": 200,
    "ExecutedVersion": "$LATEST"
}
```

The command should have create a response.json file in your directory. If you open this file, you see the output of the Lambda function.  

### Test the EventBridge Rule

You cannot put events on the Auth0 SaaS event bus, only Auth0 can publish events to this event bus. To test that the EventBridge rules deployed by this pattern were successfully deployed, follow these instructions: 

1. Navigate to the Amazon EventBridge console. Select "Rules". 

2. From the Event bus list, choose the SaaS event bus associated with your Auth0 partner event source. 

3. From the Rules list, select the "Auth0IntegrationStack-Auth0FailedLoginEventsRule54D..." 

![EventBridge Console](/serverless-patterns/auth0-eventbridge-lambda/img/EBconsole-rules.png)

4. Choose "Edit" to enter the rule editor. Click through to "Step 2. Build Event Pattern." 

![EventBridge Console](/serverless-patterns/auth0-eventbridge-lambda/img/BuildEvent.png)

5. Scroll down to "Sample event - optional." Select "Enter my own," and delete the pre-populated event. Copy the contents of event.json into the event editor. 

![EventBridge Console](/serverless-patterns/auth0-eventbridge-lambda/img/SampleEvent.png)

6. Scroll down to "Event pattern." Choose "Test Pattern." 

![EventBridge Console](/serverless-patterns/auth0-eventbridge-lambda/img/TestEvent.png)

You should see a green box appear that says "Sample event matched the event pattern." This means that the rule will successfully route incoming events to the AWS Lambda function. 

![EventBridge Console](/serverless-patterns/auth0-eventbridge-lambda/img/TestEventSuccessful.png)


## Cleanup
 
1. Delete the stack
    ```bash
    cdk destroy
    ```

----
Copyright 2024 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0