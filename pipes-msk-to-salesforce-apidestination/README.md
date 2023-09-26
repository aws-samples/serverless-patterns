# MSK to Salesforce using EventBridge Pipes and API Destination

This pattern shows how to use EventBridge Pipes to send MSK data to Salesforce using API Destinations. The pattern uses an MSK cluster as a source to EventBridge Pipe, a Lambda function to base64 decode the payload and transform data to adhere to Salesforce schema, and an API Destination as a target to send the payload to Salesforce. The use case shown here is to create "Leads" in Salesforce using the payload from MSK. 

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/pipes-msk-to-salesforce-apidestination

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Salesforce account](https://login.salesforce.com/)
* [Salesforce connected app](https://help.salesforce.com/s/articleView?id=sf.connected_app_create_basics.htm&type=5)
* [Salesforce security token](https://help.salesforce.com/s/articleView?language=en_US&id=sf.user_security_token.htm)
* [Salesforce custom platform event](https://developer.salesforce.com/docs/atlas.en-us.234.0.platform_events.meta/platform_events/platform_events_define.htm)
* [Salesforce Flow](https://help.salesforce.com/s/articleView?id=sf.c360_a_build_a_flow_in_customer_data_platform.htm&type=5)
* [SSH Key Pair for an EC2 instance in the region where this will be deployed](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html) 

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd pipes-msk-to-salesforce-apidestination
    ```

Note: This pattern can be deployed in us-west-1 region. If you'd like to deploy to another region, update the AMI Id in line 25 of producer-stack with a public community AMI Id in that region

3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region(default is us-west-1. Replace AMI Id in producer-stack.yaml file with your AMI Id if you want to deploy in another region)
    * Enter a name for EC2 Key (this EC2 Key pair should exist in the region selected above)
    * Enter MSK Kafka Version, defaults to 2.8.1
    * Select MSK Cluster Instance Type, defaults to kafka.t3.small
    * Enter MSK Topic name
    
    (View Salesforce documentation for Salesforce connection parameters)

    * [SalesforceOAuthUrl](https://github.com/aws-samples/serverless-patterns/tree/main/eventbridge-pipes-sqs-enrich-with-sfdc#:~:text=Salesforce%20connection%20parameters.-,SalesforceOAuthUrl,-for%20token%20requests) for token requests.
    * [SFEndpointUrl](https://github.com/aws-samples/serverless-patterns/tree/main/eventbridge-pipes-sqs-enrich-with-sfdc#:~:text=for%20token%20requests-,SFEndpointUrl,-SalesforceOauthClientId%2C%20SalesforceOauthClientSecret%2C%20SalesforceUsername)
    * [SalesforceClientId, SalesforceClientSecret](https://onlinehelp.coveo.com/en/ces/7.0/administrator/getting_salesforce_client_id_and_client_secret_values.htm)
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

5. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

EventBridge Pipes polls for messages from the MSK cluster, sends the data from MSK to Lambda where it gets base64 decoded and each field is mapped to the schema expected by Salesforce. EventBridge pipe then sends the Lambda response to Salesforce using an API Destination. 
For our use case, we send a JSON message from the file (test.json) to MSK which contains the fields required to create a Lead in Salesforce (namely First Name, Last Name, Company, Phone Number, Email and Title). Lambda then decodes each field and maps it to adhere to custom field names from the Platform event in Salesforce. Using API Destination, this payload is sent to Salesforce where a Salesforce Flow creates a new Lead whenever an event lands on the custom Platform Event. 

Note: Based on specific use case, the pattern can be modified to perform particular actions in Salesforce (create a new case, add an opportunity, update account etc) using the data from MSK. 

## Testing

In order to test sending messages into Amazon MSK cluster, follow these steps:

Getting the MSK brokers:

1. Open a new Cloudshell environment and set environment variables as below:

```
export REGION=<region>
export ARN=$(aws kafka list-clusters --region $REGION --query 'ClusterInfoList[*].ClusterArn' --output text)
aws kafka get-bootstrap-brokers --cluster-arn $ARN --region $REGION --output text
```
3. Make a note of the bootstrap brokers

Sending JSON test data

1. SSH into the EC2 instance deployed in public subnet

2. Set the environment variable with bootstrap broker details

```
export BOOTSTRAP=<copy and paste the MSK bootstrap servers>
export TOPIC=<topic name>
``` 

3. Next, create topic in the MSK cluster
```
cd kafka_2.13-2.8.1/bin
./kafka-topics.sh --create --bootstrap-server $BOOTSTRAP --topic $TOPIC --command-config client.properties
```

4. Copy and paste the following command
```
./kafka-console-producer.sh --broker-list $BOOTSTRAP --topic $TOPIC --producer.config client.properties
```

5. When prompted to enter a message, paste the following JSON 

```
{"first_name":"Ramsey","last_name":"Kubes","email":"rkubese@oaic.gov.au","phone":"371-855-3572","company":"Towne Inc","title":"Senior Quality Engineer"}
```

6. Open your [Salesforce account](https://login.salesforce.com/) and verify that a lead is created. 


## Cleanup
 
1. Delete the stack
    ```bash
    sam delete
    ```
----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0