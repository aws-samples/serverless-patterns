# documentdb-streams-consumer-dynamo-sam

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- documentdb_streams_event_consumer_function/src/main/java - Code for the application's Lambda function.
- events - Invocation events that you can use to invoke the function.
- documentdb_streams_event_consumer_function/src/test/java - Unit tests for the application code. 
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including a Lambda function, a DocumentDB Streams event source and a DynamoDB table to which the lambda function will write. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.


## Use the SAM CLI to build and test locally

Build your application with the `sam build` command.

```bash
sam build
```

The SAM CLI installs dependencies defined in `documentdb_streams_event_consumer_function/pom.xml`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

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
* **Parameter StreamsProducerDocumentDBCluster**: The name of the DocumentDB cluster on which DocumentDB Streams is enabled
* **Parameter StreamsProducerDocumentDBDatabase**: The name of the DocumentDB database on which DocumentDB Streams is enabled
* **Parameter StreamsProducerDocumentDBCollection**: The name of the DocumentDB collection on which DocumentDB Streams is enabled
* **Parameter SecretsManagerSecretForDocumentDBCredentialsName**: The name of the secret in Secrets Manager where the DocumentDB connection secrets (username, password, engine, host, port, ssl, dbClusterIdentifier) - The secret iself if of the form AmazonDocumentDBCredentials-SmOvis. Enter the part before the '-' here for example AmazonDocumentDBCredentials
* **Parameter SecretsManagerSecretForDocumentDBCredentialsUniqueString**: The unique string of the secret in Secrets Manager where the DocumentDB connection secrets (username, password, engine, host, port, ssl, dbClusterIdentifier) - The secret iself if of the form AmazonDocumentDBCredentials-SmOvis. Enter the part after the '-' here for example SmOvis
* **Parameter Subnet1**: The first subnet of the VPC where the DocumentDB cluster has been installed
* **Parameter Subnet2**: The second subnet of the VPC where the DocumentDB cluster has been installed
* **Parameter Subnet3**: The third subnet of the VPC where the DocumentDB cluster has been installed
* **Parameter SecurityGroup**: The security group of the lambda function. This security group should be allowed to access the security group of the DocumentDb cluster on port 27017
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Disable rollback**: Defaults to No and it preserves the state of previously provisioned resources when an operation fails
* **Save arguments to configuration file**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.
* **SAM configuration file [samconfig.toml]**: Name of the configuration file to store configuration information locally
* **SAM configuration environment [default]**: Environment for storing deployment information locally

You should get a message "Successfully created/updated stack - <StackName> in <Region>" if all goes well


## Test the sample application

Once the lambda function is deployed, send some DocumentDB Streams messages on the DocumentDB cluster/database/collection that the lambda function is listening on.

Use the project ../documentdb_streams_message_sender_json.

Look at the Readme of that project to determine how to build that project and run the command that will send DocumentDB Streams messages with a Json payload to the lambda function built using this project. The lambda function will receive the DocumentDB Streams messages with a JSON payload and input fields from the DocumentDB Streams message into a DynamoDB table.

The value field of each DocumentDB Streams message that will be sent out will be a Json element of the format

"person": {
        "firstname": "Myra",
        "lastname": "Munns",
        "company": "Anker Law Office",
        "street": "461 Prospect Pl #316",
        "city": "Euless",
        "county": "Tarrant",
        "state": "TX",
        "zip": "76040",
        "homePhone": "817-914-7518",
        "cellPhone": "817-451-3518",
        "email": "mmunns@cox.net",
        "website": "http://www.ankerlawoffice.com"
}

Either send at least 10 messages or wait for 300 seconds (check the values of BatchSize: 10 and MaximumBatchingWindowInSeconds: 300 in the template.yaml file)

Then check Cloudwatch logs and you should see messages for the Cloudwatch Log Group with the name of the deployed Lambda function.

The lambda code parses the DocumentDB Streams messages and outputs the fields in the DocumentDB Streams messages to Cloudwatch logs

A single lambda function receives a batch of messages.

The code in this example prints out the fields in the DocumentDB Streams message and logs them in Cloudwatch logs.

Apart from outputting to Cloudwatch logs, the lambda function also inputs fields from the DocumentDB Streams message (both message metadata fields as well as payload fields from the JSON payload) into a DynamoDB table created by the SAM template. You can log into the AWS console and look at the DynamoDB table and run a scan to see data getting input from the DocumentDB Streams message into the DynamoDB table
