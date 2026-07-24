# AWS Lambda MicroVMs with Amazon S3 Files

Mount an Amazon S3 bucket as a POSIX file system *inside* a Lambda MicroVM — a Firecracker-isolated, snapshot-resumable serverless compute environment — and read/write your objects as files over NFS, with changes synchronized back to S3 automatically. The MicroVM reaches the file system through a VPC egress network connector.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-microvm-s3files

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage — please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) **v2.35.0 or newer**, installed and configured. Check with `aws --version` and [upgrade](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) if needed.
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
4. **Have a VPC and subnet ready.** This pattern deploys the S3 Files mount target
   and the VPC egress connector's elastic network interfaces (ENIs) into a subnet
   **you supply** — the template does *not* create a VPC. Before deploying, either
   pick an existing VPC/subnet or create one:
    * **Use an existing VPC** – every account has a **default VPC** in each region
      whose subnets work out of the box. Find one with:
      ```
      aws ec2 describe-vpcs --region us-west-2 \
        --filters "Name=isDefault,Values=true" --query 'Vpcs[0].VpcId' --output text
      aws ec2 describe-subnets --region us-west-2 \
        --filters "Name=vpc-id,Values=<VpcId>" --query 'Subnets[].SubnetId' --output text
      ```
    * **Or create one** – e.g. `aws ec2 create-default-vpc`, or provision a dedicated
      VPC + subnet with your own tooling.
    * **Subnet requirements:** any subnet in the chosen VPC works — public *or*
      private. The subnet only needs an available IP for the mount-target ENI; the
      MicroVM reaches the mount target by its **private IPv4** over the egress
      connector, so no public IP or internet route is required on this subnet.
      (Build-time package installs use a separate managed `INTERNET_EGRESS`
      connector, not this subnet.) If you create a *dedicated* VPC for this pattern,
      remember to tear it down during cleanup — see [Cleanup](#cleanup).
5. From the command line, deploy the AWS SAM template:
    ```
    sam deploy --guided
    ```
6. During the prompts, supply:
    * **Stack Name** – e.g. `lambda-microvm-s3files`
    * **AWS Region** – `us-west-2`
    * **CodeArtifactBucket** – the bucket name from step 3
    * **VpcId** – the VPC from step 4
    * **SubnetId** – a subnet in that VPC (the CLI validates it belongs to `VpcId`)
    * Accept the IAM-capabilities prompt (`CAPABILITY_IAM`)
7. Wait for the stack to reach `CREATE_COMPLETE`. The MicroVM **image build runs
   asynchronously** as part of the stack; confirm it finished before running:
    ```
    aws cloudformation describe-stacks --stack-name <stack-name> --region us-west-2 \
      --query "Stacks[0].Outputs[?OutputKey=='ImageState'].OutputValue" --output text
    ```
   Wait until this prints `CREATED` (it starts as `CREATING`).
   The other stack outputs — `ImageArn`, `ExecutionRoleArn`, `EgressConnectorArn`,
   `FileSystemId`, `AccessPointId`, `MountTargetId`, `DataBucket` — are informational
   (FYI): `src/run.sh` reads them automatically from the stack by name, so you do not
   need to copy them anywhere.
8. Launch a MicroVM from the built image and mount the file system:
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
2. Look up the data bucket name (used in the steps below):
    ```
    BUCKET=$(aws cloudformation describe-stacks --stack-name <stack-name> --region us-west-2 \
      --query "Stacks[0].Outputs[?OutputKey=='DataBucket'].OutputValue" --output text)
    ```
3. Delete the CloudFormation stack. This removes the image, the S3 Files resources
   (file system, mount target, access point), the connector, the roles, and the log
   group. **Expect it to fail on `DataBucket`** — the bucket has **versioning
   enabled** (S3 Files requires it), so CloudFormation will not delete it while it
   holds objects:
    ```
    sam delete --stack-name <stack-name> --region us-west-2
    ```
   It ends in `DELETE_FAILED` with
   `The bucket you tried to delete is not empty. You must delete all versions...`.
   Everything *except* the bucket is now gone — importantly the S3 Files file
   system, which had been actively syncing objects into the bucket. Emptying the
   bucket *before* this step does not help: while the file system still exists it
   keeps exporting files (and flushes once more as it is torn down), re-populating
   the bucket. So empty it **after** the file system is gone.
4. Empty the now-static bucket — delete every object version and delete marker.
   This loop batches both and stops when the bucket is empty:
    ```
    while true; do
      BATCH=$(aws s3api list-object-versions --bucket "$BUCKET" --region us-west-2 --max-items 500 \
        --query '{Objects: [Versions, DeleteMarkers][][].{Key:Key,VersionId:VersionId}}' --output json)
      # Stop when nothing is left (query returns {"Objects": null}).
      echo "$BATCH" | grep -q '"Key"' || break
      aws s3api delete-objects --bucket "$BUCKET" --region us-west-2 --delete "$BATCH" >/dev/null
    done
    ```
5. Re-run the stack delete; with the bucket empty it now removes the bucket and
   completes:
    ```
    aws cloudformation delete-stack --stack-name <stack-name> --region us-west-2
    aws cloudformation wait stack-delete-complete --stack-name <stack-name> --region us-west-2
    ```
6. Confirm the stack is deleted (should print nothing):
    ```
    aws cloudformation list-stacks --region us-west-2 \
      --query "StackSummaries[?StackName=='<stack-name>' && StackStatus!='DELETE_COMPLETE'].StackStatus"
    ```
7. **If you created a dedicated VPC/subnet for this pattern**, it is *not* part of
   the stack, delete it separately once the stack is gone.

----
SPDX-License-Identifier: MIT-0

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
