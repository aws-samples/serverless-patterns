# Amazon Macie to AWS Step Functions to Amazon S3 Quarantine

This pattern deploys an automated sensitive data response pipeline that uses Amazon Macie to detect sensitive data in Amazon S3, routes findings through Amazon EventBridge to AWS Step Functions for severity-based classification, and automatically quarantines high-severity objects to a separate Amazon S3 bucket while notifying security teams via Amazon SNS.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/macie-sfn-s3-quarantine-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Node.js 18+](https://nodejs.org/en/download/) installed
* [AWS CDK v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed and bootstrapped

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```bash
    cd serverless-patterns/macie-sfn-s3-quarantine-cdk/cdk
    ```
3. Install dependencies:
    ```bash
    npm install
    ```
4. Deploy the stack:
    ```bash
    npx cdk deploy --parameters NotificationEmail=your-email@example.com
    ```
5. Confirm the SNS subscription email you receive.

## How it works

This pattern creates an automated security response pipeline for sensitive data detected by Amazon Macie:

1. **Amazon Macie** continuously scans objects in the monitored Amazon S3 bucket for sensitive data (PII, credentials, financial data).
2. When sensitive data is found, Macie publishes a finding to **Amazon EventBridge**.
3. The Amazon EventBridge rule matches `SensitiveData` finding types and triggers the **AWS Step Functions** state machine.
4. The state machine classifies the finding by severity score:
   - **HIGH (score ≥ 7)**: Quarantine the object (copy to quarantine bucket, delete from source) + notify
   - **MEDIUM (score 4-6)**: Tag the object with finding metadata + notify
   - **LOW (score < 4)**: Notify only (no remediation action)
5. **Amazon SNS** delivers notifications to the security team with finding details.

## Architecture

```
Amazon Macie (scan) --> Amazon EventBridge (finding) --> AWS Step Functions (classify + quarantine)
                                                              |
                                                              +--> AWS Lambda (move/tag object) --> Amazon S3 (quarantine)
                                                              |
                                                              +--> Amazon SNS (alert)
```

## Testing

1. Upload a file containing sensitive data (e.g., credit card numbers, SSNs) to the monitored bucket:
    ```bash
    # Create a test file with sample sensitive data
    echo "Name: John Doe, SSN: 123-45-6789, Card: 4111-1111-1111-1111" > /tmp/sensitive-test.txt

    # Upload to the monitored bucket
    aws s3 cp /tmp/sensitive-test.txt s3://macie-monitored-<ACCOUNT_ID>-<REGION>/test/sensitive-test.txt
    ```

2. Wait for Amazon Macie to scan the object (findings are published every 15 minutes by default, or trigger a one-time classification job):
    ```bash
    # Create a one-time classification job for faster testing
    aws macie2 create-classification-job \
      --job-type ONE_TIME \
      --name "test-scan" \
      --s3-job-definition '{"bucketDefinitions": [{"accountId": "<ACCOUNT_ID>", "buckets": ["macie-monitored-<ACCOUNT_ID>-<REGION>"]}]}'
    ```

3. Monitor the Step Functions execution:
    ```bash
    aws stepfunctions list-executions \
      --state-machine-arn <StateMachineArn from stack outputs> \
      --status-filter SUCCEEDED
    ```

4. Verify quarantine (for high-severity findings):
    ```bash
    aws s3 ls s3://macie-quarantine-<ACCOUNT_ID>-<REGION>/quarantined/ --recursive
    ```

## Cleanup

> **Warning**: Destroying this stack will delete all objects in both the monitored and quarantine buckets. Ensure you have backed up any data you need before proceeding.

```bash
npx cdk destroy
```

## Resources

- [Amazon Macie documentation](https://docs.aws.amazon.com/macie/latest/user/)
- [Amazon Macie finding types](https://docs.aws.amazon.com/macie/latest/user/findings-types.html)
- [AWS Step Functions documentation](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- [Amazon EventBridge event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/filtering-examples-structure.html)
