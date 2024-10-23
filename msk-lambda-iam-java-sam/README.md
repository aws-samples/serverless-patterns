# msk-lambda-iam-java-sam
# Java AWS Lambda Kafka consumer with IAM auth, using AWS SAM

This pattern is an example of a Lambda function that consumes messages from an Amazon Managed Streaming for Kafka (Amazon MSK) topic, where the MSK Cluster has been configured to use IAM authentication. This pattern assumes you already have an MSK cluster with a topic configured, if you need a sample pattern to deploy an MSK cluster either in Provisioned or Serverless modes please see the [msk-cfn-sasl-lambda pattern](https://serverlessland.com/patterns/msk-cfn-sasl-lambda). 

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- kafka_event_consumer_function/src/main/java - Code for the application's Lambda function.
- events - Invocation events that you can use to invoke the function.
- kafka_event_consumer_function/src/test/java - Unit tests for the application code. 
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an MSK event source. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* Create MSK cluster and topic that will be used for testing. It is important to create the topic before deploying the Lambda function, otherwise the event source mapping will stay disabled. 


Before proceeding with the next step, please make sure you have Java JDK and Maven installed on your machine

For the latest version of Amazon Corretto JDK (at the time of publishing), please go the following link:

https://docs.aws.amazon.com/corretto/latest/corretto-21-ug/downloads-list.html

Please follow the instructions to download and install the JDK for your Operating System

Note that you don't have to use Amazon Corretto JDK but can use JDK from another source as well

For the latest version of Maven (at the time of publishing) please go the following link:

https://maven.apache.org/download.cgi#:~:text=Apache%20Maven%203.9.9%20is,recommended%20version%20for%20all%20users.

Please follow the instructions to download and install Maven and then add the location to the bin folder of Maven in your System PATH

To ensure Java and Maven are correctly installed, run the commands:

java --version

mvn --version


## Deploy the sample application

The AWS SAM CLI is a serverless tool for building and testing Lambda applications. It uses Docker to locally test your functions in an Amazon Linux environment that resembles the Lambda execution environment. It can also emulate your application's build environment and API.

To use the AWS SAM CLI, you need the following tools.

* AWS SAM CLI - [Install the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns.git
    ```
1. Change directory to the pattern directory:
    ```
    cd msk-lambda-iam-java-sam
    ```

## Use the SAM CLI to build and test locally

Build your application with the `sam build` command.

```bash
sam build
```

The SAM CLI installs dependencies defined in `kafka_event_consumer_function/pom.xml`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
sam local invoke --event events/event.json
```

## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build
sam deploy --guided
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Parameter MSKClusterName**: The name of the MSKCluster
* **Parameter MSKClusterId**: The unique ID of the MSKCluster
* **Parameter MSKTopic**: The Kafka topic on which the lambda function will listen on
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Disable rollback**: Defaults to No and it preserves the state of previously provisioned resources when an operation fails
* **Save arguments to configuration file**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.
* **SAM configuration file [samconfig.toml]**: Name of the configuration file to store configuration information locally
* **SAM configuration environment [default]**: Environment for storing deployment information locally

You should get a message "Successfully created/updated stack - <StackName> in <Region>" if all goes well


## Test the sample application

Once the lambda function is deployed, send some Kafka messages on the topic that the lambda function is listening on, on the MSK server.

Either send at least 10 messages or wait for 300 seconds (check the values of BatchSize: 10 and MaximumBatchingWindowInSeconds: 300 in the template.yaml file)

Then check Cloudwatch logs and you should see messages for the Cloudwatch Log Group with the name of the deployed Lambda function.

The lambda code parses the Kafka messages and outputs the fields in the Kafka messages to Cloudwatch logs

A single lambda function receives a batch of messages. The messages are received as a map with each key being a combination of the topic and the partition, as a single batch can receive messages from multiple partitions.

Each key has a list of messages. Each Kafka message has the following properties - Topic, Partition, Offset, TimeStamp, TimeStampType, Key and Value

The Key and Value are base64 encoded and have to be decoded. A message can also have a list of headers, each header having a key and a value.

The code in this example prints out the fields in the Kafka message and also decrypts the key and the value and logs them in Cloudwatch logs.
