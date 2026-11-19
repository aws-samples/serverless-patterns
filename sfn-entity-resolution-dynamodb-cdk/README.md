# AWS Step Functions to AWS Entity Resolution to Amazon DynamoDB

This pattern deploys an automated entity matching pipeline that uses AWS Step Functions to orchestrate AWS Entity Resolution matching jobs. When customer records are uploaded to Amazon S3, Amazon EventBridge triggers the state machine which starts a matching job, polls for completion, and stores match metadata in Amazon DynamoDB.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/sfn-entity-resolution-dynamodb-cdk

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
    cd serverless-patterns/sfn-entity-resolution-dynamodb-cdk/cdk
    ```
3. Install dependencies:
    ```bash
    npm install
    ```
4. Deploy the stack:
    ```bash
    npx cdk deploy
    ```

## How it works

This pattern creates an automated entity resolution pipeline:

1. **Amazon S3** receives customer record files (JSON format) uploaded to the `records/` prefix.
2. **Amazon EventBridge** detects the new object creation and triggers the AWS Step Functions state machine.
3. **AWS Step Functions** orchestrates the matching workflow:
   - Calls AWS Entity Resolution `StartMatchingJob` API via SDK integration (no AWS Lambda needed)
   - Waits 30 seconds between status polls
   - Calls `GetMatchingJob` to check if the job has completed
   - On success, stores match job metadata in Amazon DynamoDB
   - On failure, the state machine reports the error
4. **AWS Entity Resolution** uses ML-based matching to identify duplicate or related customer records across the dataset.
5. **Amazon DynamoDB** stores the match job results including job ID, status, output path, and completion timestamp.

## Architecture

```
Amazon S3 (upload) --> Amazon EventBridge (Object Created) --> AWS Step Functions (orchestrate)
                                                                     |
                                                                     +--> AWS Entity Resolution (StartMatchingJob)
                                                                     |
                                                                     +--> Poll (GetMatchingJob) until SUCCEEDED
                                                                     |
                                                                     +--> Amazon DynamoDB (store results)
```

## Testing

1. Upload a sample customer records file to the source bucket:
    ```bash
    # Create sample data
    cat > /tmp/customers.json << 'EOF'
    {"record_id": "1", "full_name": "John Smith", "email": "john.smith@email.com", "phone": "+1-555-0101", "address": "123 Main St, Seattle, WA 98101"}
    {"record_id": "2", "full_name": "J. Smith", "email": "jsmith@email.com", "phone": "555-0101", "address": "123 Main Street, Seattle WA"}
    {"record_id": "3", "full_name": "Jane Doe", "email": "jane.doe@company.com", "phone": "+1-555-0202", "address": "456 Oak Ave, Portland, OR 97201"}
    EOF

    # Upload to source bucket
    aws s3 cp /tmp/customers.json s3://entity-resolution-source-<ACCOUNT_ID>-<REGION>/records/customers.json
    ```

2. Monitor the AWS Step Functions execution in the AWS Console or via CLI:
    ```bash
    aws stepfunctions list-executions \
      --state-machine-arn <StateMachineArn from stack outputs> \
      --status-filter RUNNING
    ```

3. Once complete, check the Amazon DynamoDB table for match results:
    ```bash
    aws dynamodb scan --table-name EntityMatchResults
    ```

4. Check matched output in the output bucket:
    ```bash
    aws s3 ls s3://entity-resolution-output-<ACCOUNT_ID>-<REGION>/matched-results/ --recursive
    ```

## Cleanup

> **Warning**: Destroying this stack will delete all data in the Amazon S3 buckets and the Amazon DynamoDB table. Back up any data you need before proceeding.

```bash
npx cdk destroy
```

## Resources

- [AWS Entity Resolution documentation](https://docs.aws.amazon.com/entityresolution/latest/userguide/what-is-service.html)
- [AWS Step Functions SDK integrations](https://docs.aws.amazon.com/step-functions/latest/dg/supported-services-awssdk.html)
- [Amazon EventBridge Amazon S3 event notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventBridge.html)
