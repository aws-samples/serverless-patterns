# Lambda MicroVMs with S3 Files

Mount an Amazon S3 bucket as a POSIX file system *inside* a Lambda MicroVM — a Firecracker-isolated, snapshot-resumable serverless compute environment — and read/write your objects as files over NFS, with changes synchronized back to S3 automatically. The MicroVM reaches the file system through a VPC egress network connector.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-microvm-s3files

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage — please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured. Upgrade the CLI if you encounter command not found errors.
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Serverless Application Model](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) (AWS SAM) installed
* `python3` and `zip` on your `PATH`

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repo:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd lambda-microvm-s3files
    ```
3. Upload the MicroVM application artifact (the zipped `Dockerfile` + `app.py`) to an S3 bucket in your region. The image build reads this zip, so it must exist **before** you deploy. The helper creates the bucket if it does not exist:
    ```
    ./src/run.sh package <your-artifact-bucket>
    ```
4. From the command line, deploy the AWS SAM template:
    ```
    sam deploy --guided
    ```
5. During the prompts, supply:
    * **Stack Name** – e.g. `lambda-microvm-s3files`
    * **AWS Region** – `us-west-2`
    * **CodeArtifactBucket** – the bucket name from step 3
    * **VpcId** / **SubnetId** – a VPC and subnet for the mount target and egress connector ENIs
    * Accept the IAM-capabilities prompt (`CAPABILITY_IAM`)
6. Note the stack outputs (`ImageArn`, `ExecutionRoleArn`, `EgressConnectorArn`, `FileSystemId`, `AccessPointId`, `MountTargetId`, `DataBucket`). The image build is asynchronous; wait until `ImageState` is `CREATED`.
7. Launch a MicroVM from the built image and mount the file system:
    ```
    ./src/run.sh run <stack-name>
    ```

## How it works

The application is a small HTTP service that runs inside a Lambda MicroVM and exposes the mounted file tree. Amazon S3 Files presents the S3 bucket as a POSIX file system over NFS 4.2; the app reads and writes files on `/mnt/s3files` and S3 Files synchronizes changes to and from the bucket in both directions.

```
                         ┌─────────────────────────────────────────────┐
   client                │  Firecracker MicroVM (Amazon Linux 2023)     │
   (curl / browser)      │                                              │
        │   X-aws-proxy  │   :8080  Flask app  ── reads/writes ──┐      │
        └───────────────▶│   :9000  lifecycle hooks              │      │
                         │            │ mount in /run            ▼      │
                         │            │                  /mnt/s3files   │
                         │            │                       │ NFS 4.2 │
                         └────────────┼───────────────────────┼────────┘
                                      │                        │ :2049
                              run-hook payload          VPC egress
                              (fs id, AP, mount IP)      network connector
                                                                │
                                                                ▼
                                                       ┌──────────────────┐
                                                       │  S3 Files mount  │
                                                       │  target (in VPC) │
                                                       └────────┬─────────┘
                                                          sync ▲│▼ both ways
                                                       ┌────────┴─────────┐
                                                       │   S3 bucket      │
                                                       │  (versioning on) │
                                                       └──────────────────┘
```

The mount happens in the MicroVM's **`/run` lifecycle hook**, not at image-build time, for two reasons:

1. **The network connector is bound at run time.** The MicroVM reaches the S3 Files mount target (NFS port 2049) over a VPC egress connector that only exists on the running instance — not in the build sandbox.
2. **Credentials are run-time only.** The S3 Files mount helper authenticates with the MicroVM's execution-role credentials, which are exposed to the guest via IMDSv2 and are not present during the build.

The same logic re-mounts in the **`/resume` hook**: suspending a MicroVM tears down the NFS connection, so it is re-established on resume.

**What CloudFormation provisions** (`template.yaml`): the data `S3::Bucket` (versioning on), the `S3Files::FileSystem` / `MountTarget` / `AccessPoint`, the NFS security group, the `Lambda::NetworkConnector` (VPC egress), the IAM roles (one combined build + execution role, the S3-Files-access role, the connector-operator role), the CloudWatch log group, and the `Lambda::MicrovmImage`.

**What the `src/run.sh` helper does** (data-plane operations with no CloudFormation resource): `package` zips and uploads the app artifact, and `run` calls `RunMicrovm`, mints an auth token, and exercises the app.

## Testing

After `./src/run.sh run <stack-name>` returns the `GET /` JSON with `"mounted": true`, prove the bidirectional sync — write a file through the mount and watch it appear in S3:

```
./src/run.sh prove <stack-name>
```

This calls `GET /sync-proof` (which writes a uniquely named file on the mount) and then polls the bucket until S3 Files exports it. Because the access point scopes the mount to `/microvm`, the file appears at `s3://<DataBucket>/microvm/sync-proof/<name>`.

You can also drive the app directly with the endpoint and an auth token:

```
# List the mounted tree
curl "https://<endpoint>/files" -H "X-aws-proxy-auth: <token>" -H "X-aws-proxy-port: 8080"
# Write a file directly to S3 and read it back through the mount
aws s3 cp ./local.txt s3://<DataBucket>/microvm/local.txt --region us-west-2
curl "https://<endpoint>/files/local.txt" -H "X-aws-proxy-auth: <token>" -H "X-aws-proxy-port: 8080"
```

## Cleanup

1. Terminate the running MicroVM:
    ```
    ./src/run.sh terminate <stack-name>
    ```
2. Delete the CloudFormation stack (removes the image, S3 Files resources, connector, roles, log group, and the data bucket):
    ```
    sam delete --stack-name <stack-name>
    ```
3. Confirm the stack is deleted:
    ```
    aws cloudformation list-stacks --query "StackSummaries[?StackName=='<stack-name>'].StackStatus"
    ```

## Repository layout

```
lambda-microvm-s3files/
├── template.yaml          # SAM/CloudFormation template (everything provisionable)
├── example-pattern.json   # Serverless Land pattern metadata
└── src/
    ├── app.py             # Flask app: filesystem browser + 6 lifecycle hooks
    ├── Dockerfile         # AL2023 + amazon-efs-utils (the mount -t s3files helper)
    └── run.sh             # data-plane helper: package / run / prove / terminate
```

----
SPDX-License-Identifier: MIT-0

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
