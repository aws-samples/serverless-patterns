# Amazon API Gateway, AWS Lambda and Amazon DynamoDB with Lambda SnapStart for Java

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* [Maven](https://maven.apache.org/)

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
    sam deploy --guided
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