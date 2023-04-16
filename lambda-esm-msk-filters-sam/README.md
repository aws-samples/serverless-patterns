# Lambda event filtering using event source mapping for Amazon Managed Streaming for Apache Kafka (Amazon MSK)

AWS Lambda provides [content filtering options for Amazon MSK](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-msk-smak) and other services. With event pattern content filtering, you can write complex rules so that your Lambda function is only triggered under filtering criteria you specify. This helps reduce traffic to your Lambda functions, simplifies code, and reduces overall cost.


This project includes a SAM template deploys multiple lambda functions. Each of the lambda function uses different filter criteria. We validate the expected behaviour by publishing different messages to a MSK topic, and verifying that the messages are present or absent in the corresponding function's Cloudwatch logs.



## Pre-requisites

* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* An Amazon MSK cluster and a client machine that is configured to publish messages to a topic on that cluster. [Sample CloudFormation and instructions from Amazon MSK Labs](https://catalog.workshops.aws/msk-labs/en-US/msklambda/gsrschemareg/setup)

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
1. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda-esm-msk-filters-sam
    ```
1. From the command line, use AWS SAM to deploy the AWS resources for the pattern as specified in the template.yml file:
    ```
    sam build
    sam deploy --guided
    ```

## Filtering scenarios
Each of the Lambda functions uses different [filter comparision operators](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-syntax) to demonstrate how to filter events based on the message body and metadata.


1. **No Filter** - A simple trigger without a filter criteria
    * Function name : 1-fn-esm-no-filter

2. **Equals** - A filter checking whether a particular **JSON** field value equals a string value. Filtering is based on the **message payload**.
    * Function name : 2-fn-filter-events
    
```
{
   "value":{
      "kind":[
         "Event"
      ]
   }
}
```

3. **Equals and Numeric (equals)** - A filter checking whether a particular **JSON** field value equals a string value and a different JSON field value equals a numeric value. Filtering is based on the **message payload**.
    * Function name : 3-fn-filter-events-and-response-code
    
```
{
   "value":{
      "kind":[
         "Event"
      ],
      "responseStatus":{
         "code":[
            {
               "numeric":[
                  "=",
                  300
               ]
            }
         ]
      }
   }
}
```

4. **Numeric (range)** and **Equals**- Multiple filters pattern. One pattern filters by 'Numeric (range) operator'. Another pattern filters by 'Equals' operator. Filtering is based on the **message payload**.
    * Function name : 4-fn-filter-multiple-patterns
    
```
{
   "value":{
      "responseStatus":{
         "code":[
            {
               "numeric":[
                  ">=",
                  300
               ]
            }
         ]
      }
   }
}
```
```
{
   "value":{
      "RBAC":[
         true
      ]
   }
}
```

5. **Not** - A filter checking whether a particular **JSON** field value is not equal to a string. Filtering is based on the **message payload**.
    * Function name : 5-fn-filter-not-event-kind
    
```
{
   "value":{
      "kind":[
         {
            "anything-but":[
               "Event"
            ]
         }
      ]
   }
}
```

6. **Begins with** - A filter checking whether a particular **JSON** field value begins with a string. Filtering is based on the **message payload**.
    * Function name : 6-fn-filter-starts-with
    
```
{
   "value":{
      "region":[
         {
            "prefix":"us-"
         }
      ]
   }
}
```

7. **Numeric (range)** - A filter checking whether a particular **JSON** field value is within a numeric range. Filtering is based on the **message payload**.
    * Function name : 7-fn-filter-between-inclusive
    
```
{
   "value":{
      "responseStatus":{
         "code":[
            {
               "numeric":[
                  ">=",
                  300,
                  "<=",
                  350
               ]
            }
         ]
      }
   }
}
```


8. **Begins with** - A filter checking whether a particular **plain** string value is begins with a string. Filtering is based on 
the **message payload**.
    * Function name : 8-fn-filter-on-plain-string

```
{
   "value":[
      {
         "prefix":"OrderNumber"
      }
   ]
}
```

9. **Begins with** - A filter checking whether a particular **plain** string value is begins with a string. Filtering is based on the **message payload** and **message metadata**.
    * Function name : 9-fn-filter-on-plain-string-metadata

```
{
   "topic":[
      {
         "prefix":"ESMFiltersDemoTopic"
      }
   ],
   "value":{
      "region":[
         {
            "prefix":"us-"
         }
      ]
   }
}
```

## Sample events 
We use a mix of json and plain text messages to validate the functions are filtering events as expected.

1. **base-json.json**
```
{
    "fileNameForValidation": "base-json",
    "kind": "Event",
    "apiVersion": "audit.k8s.io/v1",
    "level": "Request",
    "requestReceivedTimestamp": "2023-02-06T10:00:00.000000Z",
    "user": {
        "username": "eks:pod-identity-mutating-webhook",
        "groups": [ "system:authenticated" ]
    },
    "sourceIPs": [ "10.0.0.1" ],
    "RBAC": false,
    "responseStatus":{
        "metadata":{},
        "code":200
    }
}
```

1. **code-is-300.json**
```
{
    "fileNameForValidation": "code-is-300",
    "kind": "Event",
    "apiVersion": "audit.k8s.io/v1",
    "level": "Request",
    "requestReceivedTimestamp": "2023-02-06T10:00:00.000000Z",
    "user": {
        "username": "eks:pod-identity-mutating-webhook",
        "groups": [ "system:authenticated" ]
    },
    "sourceIPs": [ "10.0.0.1" ],
    "RBAC": false,
    "responseStatus":{
        "metadata":{},
        "code":300
    }
}
```

1. **custom-with-region.json**
```
{
    "fileNameForValidation": "custom-with-region",
    "kind": "Custom",
    "region": "us-east-1",
    "apiVersion": "audit.k8s.io/v1",
    "level": "Request",
    "requestReceivedTimestamp": "2023-02-06T10:00:00.000000Z",
    "user": {
        "username": "eks:pod-identity-mutating-webhook",
        "groups": [ "system:authenticated" ]
    },
    "sourceIPs": [ "10.0.0.1" ],
    "RBAC": false,
    "responseStatus":{
        "metadata":{},
        "code":200
    }
}
```

1. **rbac-is-set.json**
```
{
    "fileNameForValidation": "rbac-is-set",
    "kind": "Event",
    "apiVersion": "audit.k8s.io/v1",
    "level": "Request",
    "requestReceivedTimestamp": "2023-02-06T10:00:00.000000Z",
    "user": {
        "username": "eks:pod-identity-mutating-webhook",
        "groups": [ "system:authenticated" ]
    },
    "sourceIPs": [ "10.0.0.1" ],
    "RBAC": true,
    "responseStatus":{
        "metadata":{},
        "code":200
    }
}
```

1. **plain-string.txt**
```
OrderNumber:12345
```

| Operators                                          | Filter Pattern                                                                                         | Function                             | base-json.json | code-is-300.json | custom-with-region.json | rbac-is-set.json | plain-string.txt |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------|----------------|------------------|-------------------------|------------------|------------------|
| None                                               | None                                                                                                   | 1-fn-esm-no-filter                   | Y              | Y                | Y                       | Y                | Y                |
| String Equals                                      | {"value":{"kind":["Event"]}}                                                                           | 2-fn-filter-events                   | Y              | Y                | N                       | Y                | N                |
| String Equals and Numeric   Equals(Single pattern) | {"value":{"kind":["Event"],"responseStatus":{"code":[{"numeric":["=",300]}]}}}                         | 3-fn-filter-events-and-response-code | N              | Y                | N                       | N                | N                |
| String Equals and Numeric   range(2 patterns)      | {"value":{"responseStatus":{"code":[{"numeric":[">=",300]}]}}}      and      {"value":{"RBAC":[true]}} | 4-fn-filter-multiple-patterns        | N              | Y                | N                       | Y                | N                |
| Not                                                | {"value":{"kind":[{"anything-but":["Event"]}]}}                                                        | 5-fn-filter-not-event-kind           | N              | N                | Y                       | N                | N                |
| prefix                                             | {"value":{"region":[{"prefix":"us-"}]}}                                                                | 6-fn-filter-starts-with              | N              | N                | Y                       | N                | N                |
| Numeric range                                      | {"value":{"responseStatus":{"code":[{"numeric":[">=",300,"<=",350]}]}}}                                | 7-fn-filter-between-inclusive        | N              | Y                | N                       | N                | N                |
| prefix                                             | {"value":[{"prefix":"OrderNumber"}]}                                                                   | 8-fn-filter-on-plain-string          | N              | N                | N                       | N                | Y                |
| prefix                                             | {"topic":[{"prefix":"ESMFiltersDemoTopic"}],"value":[{"prefix":"Order"}]}                              | 9-fn-filter-on-plain-string-metadata | N              | N                | N                       | N                | Y                |

Y - Message logged in CloudWatch logs
N - Message not logged in CloudWatch logs

Here are the list of patterns mapped to the lambda functions.

- fn-filter-events-and-response-code - Function demonstrating 'Equals' and 'Numeric (equals)' Comparison operator                                         
- events - Invocation events that you can use to invoke the function.
- tests - Unit tests for the application code. 
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

If you prefer to use an integrated development environment (IDE) to build and test your application, you can use the AWS Toolkit.  
The AWS Toolkit is an open source plug-in for popular IDEs that uses the SAM CLI to build and deploy serverless applications on AWS. The AWS Toolkit also adds a simplified step-through debugging experience for Lambda function code. See the following links to get started.

* [CLion](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [GoLand](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [IntelliJ](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [WebStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [Rider](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [PhpStorm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [PyCharm](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [RubyMine](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [DataGrip](https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/welcome.html)
* [VS Code](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html)
* [Visual Studio](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/welcome.html)

## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build --use-container
sam deploy --guided
```

The first command will build the source of your application. The second command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

You can find your API Gateway Endpoint URL in the output values displayed after deployment.

## Use the SAM CLI to build and test locally

Build your application with the `sam build --use-container` command.

```bash
lambda-msk-esm$ sam build --use-container
```

The SAM CLI installs dependencies defined in `hello_world/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
lambda-msk-esm$ sam local invoke HelloWorldFunction --event events/event.json
```

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
lambda-msk-esm$ sam local start-api
lambda-msk-esm$ curl http://localhost:3000/
```

The SAM CLI reads the application template to determine the API's routes and the functions that they invoke. The `Events` property on each function's definition includes the route and method for each path.

```yaml
      Events:
        HelloWorld:
          Type: Api
          Properties:
            Path: /hello
            Method: get
```

## Add a resource to your application
The application template uses AWS Serverless Application Model (AWS SAM) to define application resources. AWS SAM is an extension of AWS CloudFormation with a simpler syntax for configuring common serverless application resources such as functions, triggers, and APIs. For resources not included in [the SAM specification](https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md), you can use standard [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) resource types.

## Fetch, tail, and filter Lambda function logs

To simplify troubleshooting, SAM CLI has a command called `sam logs`. `sam logs` lets you fetch logs generated by your deployed Lambda function from the command line. In addition to printing the logs on the terminal, this command has several nifty features to help you quickly find the bug.

`NOTE`: This command works for all AWS Lambda functions; not just the ones you deploy using SAM.

```bash
lambda-msk-esm$ sam logs -n HelloWorldFunction --stack-name lambda-msk-esm --tail
```

You can find more information and examples about filtering Lambda function logs in the [SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html).

## Tests

Tests are defined in the `tests` folder in this project. Use PIP to install the test dependencies and run tests.

```bash
lambda-msk-esm$ pip install -r tests/requirements.txt --user
# unit test
lambda-msk-esm$ python -m pytest tests/unit -v
# integration test, requiring deploying the stack first.
# Create the env variable AWS_SAM_STACK_NAME with the name of the stack we are testing
lambda-msk-esm$ AWS_SAM_STACK_NAME=<stack-name> python -m pytest tests/integration -v
```

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name lambda-msk-esm
```

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)
