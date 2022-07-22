# AWS IoT to DynamoDB

This pattern explains how to put data to AWS DynamoDB Table using AWS IoT Topic Rules.

Learn more about this pattern at [Serverless Land Patterns](https://serverlessland.com/patterns/iot-dynamodb).

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
    cd iot-dynamodb
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy -guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

## Testing

* IoT Rule -> DynamoDB Action

  * Visit [AWS IoT Core Management Console Test Client](https://console.aws.amazon.com/iot/home#/test)
  * Select 'Subscribe to a topic', enter Subscription topic as 'topics/ThingsGroupOne/TestThing' and select 'Subscribe'.
  * Enter below example message payload JSON and select 'Publish'.
  Note: IoT Rule in this case adds attributes 'thingId' (fetched from the topic entered in above step) and 'timestamp' putting event to DynamoDB Table. It puts full event payload JSON under 'device_data'.
  ```
  {
    "temperature_F" : "86"
  }
  ```
  * Visit [DynamoDB Management Console](https://console.aws.amazon.com/dynamodbv2/home#tables) and check the values in DynamoDB table 'IoTExampleTableOne'.

* IoT Rule -> DynamoDBv2 Action

  * Visit [AWS IoT Core Management Console Test Client](https://console.aws.amazon.com/iot/home#/test)
  * Select 'Subscribe to a topic', enter subscription topic as 'topics/ThingsGroupTwo/TestThing' and select 'Subscribe'.
  * Enter below example message payload JSON and select 'Publish'.
  ```
  {
    "eventId" : "cf2b37c2-04c2-11ed-b293-aa665a182631",
    "temperature_F" : "86"
  }
  ```
  * Visit [DynamoDB Management Console](https://console.aws.amazon.com/dynamodbv2/home#tables) and check the values in DynamoDB table 'IoTExampleTableTwo'.

## AWS Documentation
- [AWS IoT SQL Reference](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-reference.html?icmpid=docs_iot_console)
- [AWS IoT SQL - FROM Clause](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-from.html)
- [AWS IoT Rule Actions](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rule-actions.html)
- [CloudFormation - AWS::IoT::TopicRule](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html)
- [CloudFormation - AWS::DynamoDB::Table](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html)
- [AWS IoT Quotas](https://docs.aws.amazon.com/general/latest/gr/iot-core.html)

## Cleanup

1. Delete the stack
    ```bash
    sam delete
    ```

This pattern was contributed by Udit Parikh.

