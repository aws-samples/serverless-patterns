# Fan-out pattern using SNS-SQS filters

This CDK application demonstrates how to create fan-out pattern using sns topic and sqs queues using subscription filters. Number of queues required and type of filter (Message attribute based or message body based) can be defined in appSettings.json (Sample json is provided, replace queue names and filter by conditions as needed). 

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sns-sqs-fanout-pattern-cdk-dotnet

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [.NET 6](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd sns-sqs-fanout-pattern-cdk-dotnet/src
    ```
3. Build the application:
     ```
     dotnet build
     ```  
4. Return one level back to the path `sns-sqs-fanout-pattern-cdk-dotnet`
   ```
   cd..
   ```
5. Synth cdk
    ```
    cdk synth
    ```
6. Deploy the stack to your default AWS account and region.
    ```
    cdk deploy
    ```

## How it works

This application picks the configuration from appSettings.json file, based on that it creates one SNS Topic and 'n' number of queues with message attribute based or message body based filter and subscribe to the topic created. Sample appSettings.json with explanation, 
   ```
   {
       "SnsTopic": 
       {
           "Name" : "<<SNS Topic Name>>" CDK will prefix "stackname-" before resource name, It is defined in program.cs file
       },
       <<Add 'n' number of queues to be created and subscribed the topic created>>
       "SqsQueues": [
           {
               "Name": "<<Name of the queue>>",
               "FilterByAttribute": <<Boolean; True - Attribute based filter, False - Message body based filter>>,
               "Filters": [
                   {
                       "Name": "<<Filter based on which property>>", 
                       "Values": ["Value1","Value2"]
                   }                
               ]            
           }
       ]
   }
   ```

## Testing

Login to the AWS account where the cdk is deployed. SNS topic, queues and subscriptions policies should be available. Publish following messages in the topic created. Sample scenarios are listed below for the configuration given in appSettings.json (change the settings as needed)
#### Scenario-1
   ```    
   Attribute based filter. Copy Json to the message body and add attibutes given below. This message should be received only by Queue3
   Message Body:
   {
 	  "Message":"Test Message to be received by Queue3 only"
   }
   Message Attribute:
   Type - String; Name - Filter1Name; Value - Filter1Value1   
   ```
#### Scenario-2
   ```
   Attribute based filter. Copy Json to the message body and add attibutes given below. This message should be received by Queue1 and Queue3
   Message Body:
   {
 	  "Message":"Test Message to be received by Queue1 and Queue3"
   }
   Message Attribute:
   Type - String; Name - Filter1Name; Value - Filter1Value1
   Type - String; Name - Filter2Name; Value - Filter2Value1
   ```
#### Scenario-3
   ```
   Message body based filter. Copy Json to the message body and add attibutes given below. This message should be received by Queue1 and Queue3
   Message Body:
   {
 	  "Message":"Test Message to be received by Queue2 only",
 	  "Filter1Name":"Filter1Value1"
   }   
   ```

## Cleanup

Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
```
cdk destroy
``` 

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
