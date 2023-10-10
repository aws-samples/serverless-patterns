# Amazon AWS Lambda for Java using JBang

## How it works

This project uses JBang instead of Maven or Gradle. JBang allows defining the project configuration, dependencies 
and entire application in a single file.

```java
//usr/bin/env jbang "$0" "$@" ; exit $?
//JAVA 17
//DEPS com.amazonaws:aws-lambda-java-core:1.2.2
//DEPS com.amazonaws:aws-lambda-java-events:3.11.1
//SOURCES model/Person.java

import ...

public class MyApp implements RequestHandler<Person, APIGatewayProxyResponseEvent> {
    @Override
    public APIGatewayProxyResponseEvent handleRequest(Person person, Context context) {
        context.getLogger().log("Request received: " + person + "\n");

        return new APIGatewayProxyResponseEvent()
                .withStatusCode(200)
                .withHeaders(Map.of("Content-Type", "text/plain"))
                .withBody("Hello " + person.name() + "!");
    }
}
```
We import the additional file with the `Person` record, representing the request payload.

SAM build has been extended in the `template.yml` to include a custom `Makefile`, specifying the JBang command for application building.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [JBang](https://www.jbang.dev/)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```bash
    cd lambda-jbang
    ```
3. Build the function
    ```bash
    sam build
    ```
4. Deploy the infrastructure
    ```bash
    sam deploy --guided --stack-name lambda-jbang
    ```

## Testing

To test the Lambda function you can use AWS-CLI to invoke with the test payload:

```bash
aws lambda invoke --function-name JBangFunction --cli-binary-format raw-in-base64-out --qualifier live --payload '{"name": "John Doe", "age": 44}' /dev/stdout 
```

You'll see the confirmation of success:
```bash
{"statusCode":200,"headers":{"Content-Type":"text/plain"},"body":"Hello John Doe!"}
```

If you're using PowerShell on Windows, replace `/dev/stdout` in the previous command with `response.json; type response.json` to view the output.

## Cleanup

To clean up resources, delete the stack:

```bash
sam delete --stack-name lambda-jbang
```
Confirm your successful deletion of the stack:

```bash
aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'lambda-jbang')].StackStatus"
```