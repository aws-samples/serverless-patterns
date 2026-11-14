# MSK to Salesforce using EventBridge Pipes and API Destination

This pattern shows how to use EventBridge Pipes to send MSK data to Salesforce using API Destinations. The pattern uses an MSK cluster as a source to EventBridge Pipe, a Lambda function to base64 decode the payload and transform data to adhere to Salesforce schema, and an API Destination as a target to send the payload to Salesforce. The use case shown here is to create "Leads" in Salesforce using the payload from MSK. 

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/eventbridge-pipes-msk-to-salesforce.

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
* [Session Manager plugin for the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html), if you want to connect to the Kafka client instance from your terminal instead of the EC2 console

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd pipes-msk-to-salesforce-apidestination
    ```

3. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM
    ```
4. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region. The Kafka client instance uses the latest Amazon Linux 2023 AMI for that Region.
    * Enter MSK Kafka Version, defaults to 4.1.x.kraft
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

The stack deploys a Kafka client EC2 instance (Amazon Linux 2023) in a private subnet with Amazon Corretto 21, the Apache Kafka 4.1.2 client and the Amazon MSK IAM auth library installed. The instance has no public IP address and no SSH access. Its role allows the Kafka actions it needs on this cluster only, plus `AmazonSSMManagedInstanceCore` for Session Manager.

1. Connect to the instance with AWS Systems Manager Session Manager. The `KafkaClientInstanceId` stack output has the instance ID.
    * In the [Amazon EC2 console](https://console.aws.amazon.com/ec2/), select the instance, choose **Connect**, choose the **Session Manager** tab, then choose **Connect**.
    * Or, from your terminal:
        ```
        aws ssm start-session --target <KafkaClientInstanceId>
        ```

2. Session Manager signs you in as `ssm-user`. Switch to `ec2-user`, which has the Kafka client in `~/kafka` and the `CLUSTER_ARN`, `AWS_REGION` and `TOPIC` environment variables:

```
sudo su - ec2-user
cd kafka
export BOOTSTRAP=$(aws kafka get-bootstrap-brokers --cluster-arn $CLUSTER_ARN --query 'BootstrapBrokerStringSaslIam' --output text)
```

3. Next, create the topic in the MSK cluster
```
bin/kafka-topics.sh --create --bootstrap-server $BOOTSTRAP --topic $TOPIC --command-config client.properties
```

4. Start a producer
```
bin/kafka-console-producer.sh --bootstrap-server $BOOTSTRAP --topic $TOPIC --producer.config client.properties
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
