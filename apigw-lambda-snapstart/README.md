# Amazon API Gateway, AWS Lambda and Amazon DynamoDB with Lambda SnapStart for Java

This pattern demonstrates how to create a synchronous REST API using API Gateway, AWS Lambda and DynamoDB.
This pattern is built using [Spring Boot 3](https://spring.io/projects/spring-boot) and leverages the
[AWS Serverless Java Container](https://github.com/awslabs/aws-serverless-java-container) for seamless integration with
AWS Lambda. This pattern also demonstrates the usage of [SnapStart](https://aws.amazon.com/blogs/compute/reducing-java-cold-starts-on-aws-lambda-functions-with-snapstart/)
to improve startup performance.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/apigw-lambda-snapstart.

## Spring Web support in Lambda

This pattern uses the Spring Web ```@Controller``` to support different REST endpoints in the same Lambda function. 
There are two supported ways to achieve this with the AWS Serverless Java Container.

### Delegating the handler to Spring

The first is to specify a Spring class as the function handler and reference the SpringBootApplication class as an 
environment variable.

```yaml
    Type: AWS::Serverless::Function
    Properties:
      Handler: com.amazonaws.serverless.proxy.spring.SpringDelegatingLambdaContainerHandler
      ...
      Environment:
         Variables:
            MAIN_CLASS: com.unicorn.store.StoreApplication
```

This is useful as you don't need to make any changes to your existing application to run it in Lambda.

### Starting Spring in your own handler

An alternative is to create your own handler and start Spring within it. The class ```StreamLambdaHandler``` is an 
example of this.

This is useful when you want control over the handler method, for example to add an annotation.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Java 17](https://aws.amazon.com/corretto/)
* [Maven](https://maven.apache.org/)
* [CURL](https://curl.se/)
* [jq](https://jqlang.github.io/jq/)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd apigw-lambda-snapstart
    ```
3. Build the function
    ```
    sam build
    ```
4. Deploy the infrastructure
    ```
    sam deploy --stack-name unicorn-store --guided
    ```

## Testing

To test the Lambda function you can POST a unicorn JSON payload to the '/unicorns' endpoint.

```bash
curl --location --request POST $(aws cloudformation describe-stacks --stack-name unicorn-store --query "Stacks[0].Outputs[?OutputKey=='UnicornEndpoint'].OutputValue" --output text)'/unicorns' \
--header 'Content-Type: application/json' \
--data-raw '{
"name": "Something",
"age": "Older",
"type": "Animal",
"size": "Very big"
}' | jq
```

## Measuring the results

You can use the following AWS CloudWatch Insights query to measure the duration your SnapStart Lambda function.

```
filter @message like "REPORT"
| filter @message not like "RESTORE_REPORT"
| parse @message /Restore Duration: (?<@restore_duration_ms>[0-9\.]+)/
| parse @message /	Duration: (?<@invoke_duration_ms>[0-9\.]+)/
| fields
  greatest(@restore_duration_ms, 0) as restore_duration_ms,
  greatest(@invoke_duration_ms, 0) as invoke_duration_ms
| fields
  restore_duration_ms + invoke_duration_ms as total_invoke_ms
| stat
  pct(total_invoke_ms, 50) as total_invoke_ms_p50,
  pct(total_invoke_ms, 99) as total_invoke_ms_p99,
  pct(total_invoke_ms, 99.9) as total_invoke_ms_p99.9
```