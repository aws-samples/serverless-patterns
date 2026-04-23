# Lambda with Amazon S3 Files Mount

This pattern deploys a Lambda function with an Amazon S3 Files file system mounted as a local directory, enabling standard file operations on S3 data without downloading objects.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-s3-files-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Node and NPM](https://nodejs.org/en/download/) installed
- [AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```bash
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```bash
   cd serverless-patterns/lambda-s3-files-cdk
   ```
3. Install CDK dependencies:
   ```bash
   npm install
   ```
4. Deploy the stack:
   ```bash
   cdk deploy
   ```

## How it works

[Amazon S3 Files](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files.html) (GA April 2026) provides NFS access to S3 buckets with full POSIX semantics. This pattern mounts an S3 bucket on a Lambda function at `/mnt/s3data`.

### What gets deployed

| Resource | Purpose |
|---|---|
| S3 Bucket | Data store backing the file system |
| VPC (2 AZs) | Network for Lambda and mount targets |
| S3 Files FileSystem | NFS file system linked to the S3 bucket |
| S3 Files MountTargets | Network endpoints in each private subnet |
| S3 Files AccessPoint | Application entry point (UID/GID 1000, root `/lambda`) |
| Security Group | Allows NFS traffic (port 2049) |
| Lambda Function | Reads, writes, and lists files via the mount |

### Architecture

```
┌──────────┐     ┌─────────────────────────────────────────┐
│ S3 Bucket│◄───►│         S3 Files FileSystem              │
└──────────┘     │  (auto-sync between S3 and filesystem)  │
                 └──────────────┬────────────────────────────┘
                                │ NFS (port 2049)
                 ┌──────────────┴────────────────────────────┐
                 │              VPC                           │
                 │  ┌────────────────┐  ┌────────────────┐   │
                 │  │  Mount Target  │  │  Mount Target  │   │
                 │  │    (AZ-1)      │  │    (AZ-2)      │   │
                 │  └────────────────┘  └────────────────┘   │
                 │           ▲                                │
                 │           │                                │
                 │  ┌────────┴───────┐                        │
                 │  │ Lambda Function│                        │
                 │  │ /mnt/s3data    │                        │
                 │  └────────────────┘                        │
                 └────────────────────────────────────────────┘
```

### Key S3 Files concepts

- **FileSystem** — A shared file system linked to your S3 bucket. Changes sync bidirectionally.
- **MountTarget** — Network endpoint in a specific AZ. Lambda must be in the same VPC/subnet.
- **AccessPoint** — Application-specific entry point with POSIX user identity and root directory.
- **High-performance storage** — Actively used data cached locally for sub-millisecond latency.

## Testing

1. After deployment, note the `FunctionName` and `BucketName` outputs.

2. **Write a file** through the Lambda mount:
   ```bash
   aws lambda invoke \
     --function-name <FunctionName> \
     --payload '{"action": "write", "filename": "hello.txt", "content": "Hello from Lambda via S3 Files!"}' \
     --cli-binary-format raw-in-base64-out \
     output.json

   cat output.json
   ```

3. **Verify the file appeared in S3** (sync takes ~1 minute):
   ```bash
   aws s3 ls s3://<BucketName>/lambda/
   ```

4. **Read the file** back through Lambda:
   ```bash
   aws lambda invoke \
     --function-name <FunctionName> \
     --payload '{"action": "read", "filename": "hello.txt"}' \
     --cli-binary-format raw-in-base64-out \
     output.json

   cat output.json
   ```

5. **List directory** contents:
   ```bash
   aws lambda invoke \
     --function-name <FunctionName> \
     --payload '{"action": "list"}' \
     --cli-binary-format raw-in-base64-out \
     output.json

   cat output.json
   ```

## Cleanup

```bash
cdk destroy
```

---

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
