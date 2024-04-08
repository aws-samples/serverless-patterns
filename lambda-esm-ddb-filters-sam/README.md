# AWS Event Source Mapping for Lambda from Amazon DynamoDB Stream

This pattern demonstrates the ability to filter Amazon DynamoDB Stream events so that only a subset of all events is sent to an AWS Lambda function for processing. Demo stack will create a single Amazon DynamoDB Table (table-lambda-esm-filter), enable [Change Data Capture](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) for that table, and create a number of AWS Lambda functions that are subscribed to the Amazon DynamoDB stream using different filter configurations.

Review [Filter rule syntax](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-syntax) for more details on the message filtering configuration.
**Important note**: Filter definition should not contain any whitespace (tabs, space, etc.) in order to work properly!

Learn more about this pattern at Serverless Land Patterns: [https://serverlessland.com/patterns/lambda-esm-ddb-filters-sam/](https://serverlessland.com/patterns/lambda-esm-ddb-filters-sam/)

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

``` sh
git clone https://github.com/aws-samples/serverless-patterns
```

1. Change directory to the pattern directory:

    ``` sh
    cd lambda-esm-ddb-filters-sam
    ```

1. From the command line, use AWS SAM CLI to build the application

    ``` sh
    sam build
    ```

1. From the command line, use AWS SAM CLI to deploy the AWS resources for the pattern as specified in the template.yml file:

    ``` sh
    sam deploy --guided
    ```

    or

    ```sh
    sam deploy --stack-name <STACK_NAME> --resolve-s3 --capabilities CAPABILITY_IAM --no-fail-on-empty-changeset
    ```

1. During the prompts:
    * Enter a stack name
    * Enter the desired AWS Region - AWS CLI default region is recommended if you are planning to run the test (test.sh) script
    * Allow SAM CLI to create IAM roles with the required permissions.

    Once you have run `sam deploy --guided` mode once and saved arguments to a configuration file (samconfig.toml), you can use `sam deploy` in future to use these defaults.

1. Note the outputs from the SAM deployment process. These contain the resource names and/or ARNs which are used for testing.

## How it works

A new Amazon DynamoDB table is created and is configured to send Change Data Capture (CDC) events to a DynamoDB Stream. Multiple AWS Lambda functions are subscribed to that stream with different filter settings. This way we demonstrate how various filtering settings affect which CDC events are sent to each AWS Lambda function for processing.

All AWS Lambda functions use the same code for demo purposes.

Please note, that working with DynamoDB stream events is slightly different from working with Amazon Kinesis events and Amazon Kinesis event filters. See [https://serverlessland.com/patterns/lambda-esm-kinesis-filters-sam/](https://serverlessland.com/patterns/lambda-esm-kinesis-filters-sam/) for Amazon Kinesis event filtering example. In particular, the following considerations should be taken into account when working with Amazon DynamoDB streams:

* Event payload is not base64 encoded
* All numbers are sent across the network to DynamoDB as strings ([Supported data types and naming rules in Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html)), thus it is not possible to use numeric based filters (like range, less, greater, less-or-equal, greater-or-equal)
* DynamoDB stream will have record information sent as a `NewImage` or `OldImage` JSON object, depending on the event type and stream configuration

## Testing

You can execute a test script to simulate the activity of adding and deleting test records from the demo Amazon DynamoDB Table (table-lambda-esm-filter).

```sh
./test.sh
```

This script will delete all existing records from the `table-lambda-esm-filter` DynamoDB Table.
All test records (see below) are defined in the [records](./records/) folder. The test script reads all files from that folder and adds them as records to the `table-lambda-esm-filter` DynamoDB Table.

### Pre-configured test messages

1. Basic JSON [events/base-json.json](records/base-record.json)

    ```json
    {
        "id": {
            "S": "base-record"
        },
        "kind": {
            "S": "Event"
        },
        "apiVersion": {
            "S": "audit.k8s.io/v1"
        },
        "level": {
            "S": "Request"
        },
        "requestReceivedTimestamp": {
            "S": "2023-02-06T10:00:00.000000Z"
        },
        "user": {
            "M": {
                "username": {
                    "S": "eks:pod-identity-mutating-webhook"
                },
                "groups": {
                    "L": [
                        {
                            "S": "system:authenticated"
                        }
                    ]
                }
            }
        },
        "sourceIPs": {
            "L": [
                {
                    "S": "10.0.0.1"
                }
            ]
        },
        "RBAC": {
            "BOOL": false
        },
        "responseStatus": {
            "M": {
                "metadata": {
                    "M": {}
                },
                "code": {
                    "N": "200"
                }
            }
        }
    }
    ```

1. Basic JSON record with responseStatus code set to 300 [records/code-is-300.json](records/code-is-300.json)

    ```json
    {
        "id": {
            "S": "code-is-300"
        },
        "kind": {
            "S": "Event"
        },
        "apiVersion": {
            "S": "audit.k8s.io/v1"
        },
        "level": {
            "S": "Request"
        },
        "requestReceivedTimestamp": {
            "S": "2023-02-06T10:00:00.000000Z"
        },
        "user": {
            "M": {
                "username": {
                    "S": "eks:pod-identity-mutating-webhook"
                },
                "groups": {
                    "L": [
                        {
                            "S": "system:authenticated"
                        }
                    ]
                }
            }
        },
        "sourceIPs": {
            "L": [
                {
                    "S": "10.0.0.1"
                }
            ]
        },
        "RBAC": {
            "BOOL": false
        },
        "responseStatus": {
            "M": {
                "metadata": {
                    "M": {}
                },
                "code": {
                    "N": "300"
                }
            }
        }
    }
    ```

1. Basic JSON with RBAC flag set to true [records/rbac-is-set.json](records/rbac-is-set.json)

    ```json
    {
        "id": {
            "S": "rbac-is-set"
        },
        "kind": {
            "S": "Event"
        },
        "apiVersion": {
            "S": "audit.k8s.io/v1"
        },
        "level": {
            "S": "Request"
        },
        "requestReceivedTimestamp": {
            "S": "2023-02-06T10:00:00.000000Z"
        },
        "user": {
            "M": {
                "username": {
                    "S": "eks:pod-identity-mutating-webhook"
                },
                "groups": {
                    "L": [
                        {
                            "S": "system:authenticated"
                        }
                    ]
                }
            }
        },
        "sourceIPs": {
            "L": [
                {
                    "S": "10.0.0.1"
                }
            ]
        },
        "RBAC": {
            "BOOL": true
        },
        "responseStatus": {
            "M": {
                "metadata": {
                    "M": {}
                },
                "code": {
                    "N": "200"
                }
            }
        }
    }
    ```

1. Basic JSON with kind set to Custom and a new region property [records/custom-with-region.json](records/custom-with-region.json)

    ```json
    {
        "id": {
            "S": "custom-with-region"
        },
        "kind": {
            "S": "Custom"
        },
        "region": {
            "S": "us-east-1"
        },
        "apiVersion": {
            "S": "audit.k8s.io/v1"
        },
        "level": {
            "S": "Request"
        },
        "requestReceivedTimestamp": {
            "S": "2023-02-06T10:00:00.000000Z"
        },
        "user": {
            "M": {
                "username": {
                    "S": "eks:pod-identity-mutating-webhook"
                },
                "groups": {
                    "L": [
                        {
                            "S": "system:authenticated"
                        }
                    ]
                }
            }
        },
        "sourceIPs": {
            "L": [
                {
                    "S": "10.0.0.1"
                }
            ]
        },
        "RBAC": {
            "BOOL": false
        },
        "responseStatus": {
            "M": {
                "metadata": {
                    "M": {}
                },
                "code": {
                    "N": "200"
                }
            }
        }
    }
    ```

### Viewing test results

Navigate to CloudWatch console and inspect messages logged to the following log groups:

| Log Group | Pattern(s) | Match messages | Comment |
| --- | --- | --- | --- |
| /aws/lambda/fn-ddb-esm-no-filter | | ALL | logs all CDC events |
| /aws/lambda/fn-ddb-filter-events | `{"dynamodb":{"NewImage":{"kind":{"S":["Event"]}}}}` | 2, 3, 4 | tests for a single property value equality for a events having a `NewImage` specification |
| /aws/lambda/fn-ddb-filter-events-and-response-code | `{"dynamodb":{"NewImage":{"kind":{"S":["Event"]},"responseStatus":{"M":{"code":{"N":["300"]}}}}}}` | 3 | tests for multiple properties, including a nested object |
| /aws/lambda/fn-ddb-filter-key | `{"eventName":["INSERT","REMOVE"],"dynamodb":{"Keys":{"id":{"S":["rbac-is-set"]}}}}` | 3 | tests for INSERT and REMOVE events matching a specific Keys filter |
| /aws/lambda/fn-ddb-filter-multiple-patterns | `{"dynamodb":{"NewImage":{"responseStatus":{"M":{"code":{"N":["300"]}}}}}}` and `{"dynamodb":{"OldImage":{"RBAC":{"BOOL":[true]}}}}` | 3, 4 | demonstrates that multiple patterns are ORed. **You'll have to run `test.sh` the second time or update the record with `id="rbac-is-set"` to have that event captured in CloudWatch, since it is triggered when that record is updated or deleted only!** |
| /aws/lambda/fn-ddb-filter-not-event-kind | `{"dynamodb":{"NewImage":{"kind":{"S":[{"anything-but":["Event"]}]}}}}` | 5 | tests for a single field inequality |
| /aws/lambda/fn-ddb-filter-starts-with | `{"dynamodb":{"NewImage":{"region":{"S":[{"prefix":"us-"}]}}}}` | 5 | tests for a string prefix |

## Cleanup

1. Delete the stack

    ```bash
    sam delete --stack-name <STACK_NAME>
    ```

1. Confirm the stack has been deleted

    ```bash
    aws cloudformation list-stacks --query "StackSummaries[?contains(StackName,'<STACK_NAME>')].StackStatus"
    ```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
