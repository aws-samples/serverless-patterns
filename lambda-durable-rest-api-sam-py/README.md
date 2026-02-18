# Lambda Durable Function - REST API Call with Python

This pattern demonstrates a Lambda durable function that calls an external REST API using Python.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

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
    cd lambda-durable-rest-api-sam-py
    ```

1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build
    sam deploy --guided
    ```
1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

This pattern demonstrates AWS Lambda Durable Execution for calling external REST APIs. It uses the AWS Durable Execution SDK to create a durable function that can:

**AWS Durable Execution Features:**
- **Automatic State Management**: AWS manages execution state across invocations
- **Durable Steps**: The `@durable_step` decorator marks functions that can be retried automatically
- **Durable Waits**: Use `context.wait()` to pause execution without consuming CPU or memory
- **Built-in Retry Logic**: Failed steps are automatically retried by AWS
- **Execution History**: AWS tracks the complete execution history and state

The function uses two key components:
1. `@durable_step` - Wraps the REST API call, making it automatically retryable
2. `@durable_execution` - Marks the Lambda handler as a durable execution workflow

AWS Lambda Durable Execution automatically handles failures, retries, and state persistence without requiring external services like DynamoDB or Step Functions.

## Testing

1. Get the function name from the stack outputs:
```bash
aws cloudformation describe-stacks --stack-name <your-stack-name> \
  --query 'Stacks[0].Outputs[?OutputKey==`FunctionName`].OutputValue' --output text
```

2. Invoke the function with default URL:
```bash
aws lambda invoke \
  --function-name <function-name> \
  --payload '{}' \
  response.json && cat response.json
```

3. Invoke with a custom URL:
```bash
aws lambda invoke \
  --function-name <function-name> \
  --payload '{"url": "https://jsonplaceholder.typicode.com/users/1"}' \
  response.json && cat response.json
```

Example JSON Lambda test event:
```json
{
  "url": "https://jsonplaceholder.typicode.com/posts/1"
}
```

Expected response (success):
```json
{
  "statusCode": 200,
  "headers": {"Content-Type": "application/json"},
  "body": "{\"message\": \"API call successful\", \"url\": \"https://jsonplaceholder.typicode.com/posts/1\", \"data\": {...}}"
}
```

The execution is durable - if the API call fails, AWS Lambda will automatically retry the `call_rest_api` step without re-executing the entire function.

## Cleanup
 
1. Delete the stack:
    ```bash
    aws cloudformation delete-stack --stack-name <your-stack-name>
    ```
1. Confirm the stack has been deleted:
    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'<your-stack-name>')].StackStatus"
    ```

----
