# Kinesis Poison Pill Pattern

This pattern demonstrates how to handle a Lambda consumer failure when reading from a Kinesis Data Stream with CDK

Without proper handling of failure when working with Kinesis Data Streams, an iterator will get stuck and the only way for the data to clear the stream is for it to **Age Out** beyond the trim horizon.

This will ultimately create wasteful invocations of a Lambda, wasted CPU cycles in a container and worst of all the downstream consumers will not get the data they need.

Learn more about this pattern at Serverless Land Patterns: << Add the live URL here >>

**Important**: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

-   [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
-   [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
-   [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
-   [Node and NPM](https://nodejs.org/en/download/) installed
-   [The Go Programming Langage](https://go.dev/doc/install) must be installed in order to build the Lambda
-   [Terraform](https://www.terraform.io) must be installed in order to provision infrastructure

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the lambda module directory:
    ```
    cd terraform-kinesis-poison-pill/modules/lambda
    ```
3. Install the project dependencies 
    ```
     npm install
    ```
4. Build lambda using make command
    ```
     make
    ```
5. Change directory to the pattern directory:
    ```
    cd ../..

6. Deploy the stack to your default AWS account and region using terraform
    ```
    terraform init
    terraform plan
    terraform apply
    ```

## How it works

This pattern is designed to highlight how to handle failure when processing records in a Lambda. The `Kinesis Event Source` turns a Lambda into a Data Consumer which will process a JSON event that looks like this in Go

```golang
type SampleEvent struct {
	FieldA string `json:"fieldA"`
	FieldB string `json:"fieldB"`
	FieldC int    `json:"fieldC"`
}
```

And like this in JSON

```javascript
// defintion
{
    fieldA: string;
    fieldB: string;
    fieldC: number
}

// example
{
    "fieldA": "ABC",
    "fieldB": "EFG",
    "fieldC": 123
}
```

Once the pattern is deployed to AWS, you will have the following resources created with the described capabilities

-   Kinesis Data Stream where the data will be "sourced"
-   Lambda Consumer written in Golang that will read from Kinesis in an attempt to process the records
-   SQS Queue where failed Kinesis records will be put

## Testing


### Testing Success


```bash
aws kinesis put-record \
    --stream-name kinesis-stream \
    --data 'eyJmaWVsZEEiOiAiQUJDIiwgImZpZWxkQiI6ICJFRkciLCAiZmllbGRDIjogMTIzIH0K' \
    --partition-key key --region us-west-1
```

This command will publish a JSON payload that will successfully be Unmarshalled in the Lambda.

### Testing Failure

```bash
aws kinesis put-record \
    --stream-name kinesis-stream \
    --data 'eyJmaWVsZEEiOiAiQUJDIiwgImZpZWxkQiI6ICJFRkciLCAiZmllbGRDIjogIjEyMyIgfQo=' \
    --partition-key key --region us-west-1
```

This command will publish a JSON payload that will not be Unmarshalled successfully in the Lambda. `FieldC` will be a `string` instead of a `number`

Based upon the definition in the terraform code, this will be attempted 5 times and will be bisected out of batch should more records be in the read.

### Inspecting in the AWS Console

-   Cloudwatch - for Logs

Go to Cloudwatch log group /aws/lambda/kinesis_stream
You should see two kind of log event for success and failure
For Success event shows as 
```
level=info msg="All good, see you later
```
For failure event shows as 
```
json: cannot unmarshal string into Go struct field SampleEvent.fieldC of type int: UnmarshalTypeError
```

-   SQS - for the failed message
-   Kinesis - DataViewer looking at the TRIM_HORIZON

## Cleanup

1. Delete the stack
    ```bash
    terraform destroy
    ```

## Documentation

-   [AWS Using Lambda with Kinesis](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html)
-   [AWS Lambda Failure-Handling Features](https://www.amazonaws.cn/en/new/2019/aws-lambda-supports-failure-handling-features-for-kinesis-and-dynamodb-event-sources/)

---

Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0