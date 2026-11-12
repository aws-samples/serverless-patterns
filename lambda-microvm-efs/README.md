# AWS Lambda MicroVMs with Amazon EFS

Mount an Amazon EFS file system *inside* a Lambda MicroVM — a Firecracker-isolated,
snapshot-resumable serverless compute environment — and read/write it as an ordinary
POSIX file tree over NFS 4.1. Many MicroVMs mount the same file system at once, see
each other's writes immediately, and the data outlives every one of them. The MicroVM
reaches the file system through a VPC egress network connector.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/lambda-microvm-efs

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage — please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* **A region where AWS Lambda MicroVMs is available.** Lambda MicroVMs (and the `AWS::Lambda::MicrovmImage` / `AWS::Lambda::NetworkConnector` resources this pattern uses) are offered only in a subset of AWS Regions, and the service is still expanding. The examples below use `us-west-2`; if you deploy to a Region where the service is not yet available the stack fails at the MicroVM image/connector resources. Check the current list in the [Lambda MicroVMs documentation](https://docs.aws.amazon.com/lambda/) before choosing a Region.
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
    cd lambda-microvm-efs
    ```

3. Upload the MicroVM application artifact (the zipped `Dockerfile` + `app.py`) to an S3 bucket in your region. The image build reads this zip, so it must exist **before** you deploy. The helper creates the bucket if it does not exist:

    ```
    ./src/run.sh package <your-artifact-bucket>
    ```

4. **Have a VPC and subnet ready.** This pattern deploys the EFS mount target and the VPC egress connector's elastic network interfaces (ENIs) into a subnet **you supply** — the template does *not* create a VPC. Before deploying, either pick an existing VPC/subnet or create one:

    * **Use an existing VPC** – every account has a **default VPC** in each region whose subnets work out of the box. Find one with:

        ```
        aws ec2 describe-vpcs --region us-west-2 \
          --filters "Name=isDefault,Values=true" --query 'Vpcs[0].VpcId' --output text
        aws ec2 describe-subnets --region us-west-2 \
          --filters "Name=vpc-id,Values=<VpcId>" --query 'Subnets[].SubnetId' --output text
        ```

    * **Or create one** – e.g. `aws ec2 create-default-vpc`, or provision a dedicated VPC + subnet with your own tooling.

    * **Subnet requirements:** any subnet in the chosen VPC works — public *or* private. It only needs an available IP for the mount-target ENI; the MicroVM reaches the mount target by its **private IPv4** over the egress connector, so no public IP or internet route is required. (Build-time package installs use a separate managed `INTERNET_EGRESS` connector, not this subnet.)

    * **Use ONE subnet for both.** Putting the mount target and the connector ENIs in the same subnet keeps the MicroVM and the mount target in the same Availability Zone. Cross-AZ NFS still works but adds latency and inter-AZ data charges for no benefit here.

    If you create a *dedicated* VPC for this pattern, remember to tear it down during cleanup — see [Cleanup](#cleanup).

5. From the command line, deploy the AWS SAM template:

    ```
    sam deploy --guided
    ```

6. During the prompts, supply:
    * **Stack Name** – e.g. `lambda-microvm-efs`
    * **AWS Region** – `us-west-2`
    * **CodeArtifactBucket** – the bucket name from step 3
    * **VpcId** – the VPC from step 4
    * **SubnetId** – a subnet in that VPC (the CLI validates it belongs to `VpcId`)
    * Accept the IAM-capabilities prompt (`CAPABILITY_IAM`)

7. Wait for the stack to reach `CREATE_COMPLETE`. The MicroVM **image build runs asynchronously** as part of the stack; confirm it finished before running:

    ```
    aws cloudformation describe-stacks --stack-name <stack-name> --region us-west-2 \
      --query "Stacks[0].Outputs[?OutputKey=='ImageState'].OutputValue" --output text
    ```

    Wait until this prints `CREATED` (it starts as `CREATING`). The other stack outputs — `ImageArn`, `ExecutionRoleArn`, `EgressConnectorArn`, `FileSystemId`, `AccessPointId`, `MountTargetId` — are informational (FYI): `src/run.sh` reads them automatically from the stack by name, so you do not need to copy them anywhere.

8. Launch a MicroVM from the built image and mount the file system:

    ```
    ./src/run.sh run <stack-name>
    ```

## How it works

The application is a small HTTP service that runs inside a Lambda MicroVM and exposes the mounted file tree. Amazon EFS is a managed NFS 4.1 file system; the app reads and writes files on `/mnt/efs` and every other MicroVM mounting the same file system sees those writes immediately.

```
                         ┌─────────────────────────────────────────────┐
   client                │  Firecracker MicroVM (Amazon Linux 2023)    │
   (curl / browser)      │                                             │
        │   X-aws-proxy  │   :8080  Flask app  ── reads/writes ──┐     │
        └───────────────▶│   :9000  lifecycle hooks              │     │
                         │            │ mount in /run            ▼     │
                         │            │ umount in /suspend  /mnt/efs   │
                         │            │ mount in /resume         │     │
                         └────────────┼──────────────────────────┼─────┘
                                      │                          │ NFS 4.1
                              run-hook payload                   │ :2049
                              (fs id, AP, mount IP)         VPC egress
                                                            network connector
                                                                  │
                                                                  ▼
                                                        ┌──────────────────┐
                                                        │  EFS mount target│
                                                        │  (in your VPC)   │
                                                        └────────┬─────────┘
                                                                 │
                                    ┌────────────────────────────┴─────────┐
                                    │   Amazon EFS file system             │
                                    │   (elastic throughput, encrypted)    │
                                    │   ← also mounted by other MicroVMs → │
                                    └──────────────────────────────────────┘
```

The mount happens in the MicroVM's **`/run` lifecycle hook**, not at image-build time, for two reasons:

1. **The network connector is bound at run time.** The MicroVM reaches the EFS mount target (NFS port 2049) over a VPC egress connector that only exists on the running instance — not in the build sandbox.
2. **Credentials are run-time only.** The `mount -t efs` helper authenticates with the MicroVM's execution-role credentials, which are exposed to the guest via IMDSv2 and are not present during the build.

### Snapshots and the mount lifecycle

An NFS session **cannot survive a snapshot**. A resumed MicroVM has a new network identity and may be running on a different host, so a mount captured in the snapshot is dead on arrival: the first I/O returns `ENOTCONN` or hangs. This pattern therefore:

* mounts in **`/run`**,
* **unmounts in `/suspend`** — cleanly releasing the mount on the way down is what makes the re-mount reliable,
* re-mounts in **`/resume`**.

Two details in `app.py` are worth copying into your own code:

* **Detect the mount by reading `/proc/self/mounts`, never with `stat()`.** `stat()` on a stale NFS mount can return `ENOTCONN` or block indefinitely. Note also that `findmnt -T <path>` is *not* a valid check: it falls back to the mount point of the filesystem *containing* the path, so on an unmounted directory it reports `/` and exits 0 — i.e. it claims "mounted" forever.
* **Wait for the mount to carry I/O, not merely to appear.** amazon-efs-utils registers the mountpoint a few seconds before the efs-proxy TLS tunnel is actually passing data. `mount_efs()` does a write/read/delete round trip and only reports success once that works, so a write issued immediately after `run` cannot be lost.

**What CloudFormation provisions** (`template.yaml`): the `EFS::FileSystem` (elastic throughput, encrypted), the `EFS::MountTarget` and `EFS::AccessPoint`, the NFS security group, the `Lambda::NetworkConnector` (VPC egress), the IAM roles (one combined build + execution role, the connector-operator role), the CloudWatch log group, and the `Lambda::MicrovmImage`.

**What the `src/run.sh` helper does** (data-plane operations with no CloudFormation resource): `package` zips and uploads the app artifact; `run` calls `RunMicrovm`, mints an auth token, and waits for the mount; `prove` launches a second MicroVM to demonstrate sharing; `bench` measures throughput.

### `AdditionalOsCapabilities: [ALL]` is mandatory

The image sets `AdditionalOsCapabilities: [ALL]`, which is what grants `CAP_SYS_ADMIN` and exposes the full set of guest device nodes to the container. Without it the container gets only `/dev/sysgenid` and **cannot call `mount(2)` at all** — so no NFS, no EFS. That single property is the difference between this pattern working and being impossible. It is applied inside the VM isolation boundary and does not affect the host or other MicroVMs.

### Least privilege on the mount

The access point pins the POSIX identity to uid/gid 1000 and roots the mount at `/microvm`. Because the access point squashes all access to that identity, the execution role needs only `elasticfilesystem:ClientMount` and `ClientWrite` — **not** `ClientRootAccess` — and both are conditioned on `elasticfilesystem:AccessPointArn`, so the role cannot mount the file system any other way.

For defence in depth you can additionally attach an EFS **file system policy** that denies any access without `aws:SecureTransport`. It is left out of the template only because referencing the role ARN from the file system and the file system ARN from the role creates a CloudFormation circular dependency; add it with an explicit `RoleName` if you want it.

## Testing

After `./src/run.sh run <stack-name>` returns the `GET /` JSON with `"mounted": true`, prove the property that matters — **two MicroVMs, one file system**:

```
./src/run.sh prove <stack-name>
```

This writes a file from the first MicroVM, launches a **second** MicroVM with its own independent mount, reads the same path back through it, and asserts the bytes match. There is no export step and no sync lag: the second VM sees the data because it is the same file system, not a copy of one. It then prints `/shared-log`, a single append-only file on EFS carrying one line per MicroVM that has ever mounted it — including VMs that have since been terminated. The second VM is terminated automatically when `prove` finishes.

You can also drive the app directly with the endpoint and an auth token:

```
# List the mounted tree
curl "https://<endpoint>/files" -H "X-aws-proxy-auth: <token>" -H "X-aws-proxy-port: 8080"

# Write a file and read it back
curl -X PUT "https://<endpoint>/files/notes/hello.txt" --data-binary 'hello from a microVM' \
  -H "X-aws-proxy-auth: <token>" -H "X-aws-proxy-port: 8080"
curl "https://<endpoint>/files/notes/hello.txt" -H "X-aws-proxy-auth: <token>" -H "X-aws-proxy-port: 8080"

# Append to the shared log and see every MicroVM that has mounted this file system
curl "https://<endpoint>/shared-log" -H "X-aws-proxy-auth: <token>" -H "X-aws-proxy-port: 8080"
```

## Throughput

EFS traffic leaves the MicroVM over the VPC egress connector, so it is governed by the MicroVM's **egress** bandwidth allocation. This is *not* the documented 8–128 Mbps request/response table — that describes the service-managed HTTPS endpoint (the ingress path) and does not apply to a VPC mount.

Measure it from inside the guest:

```
./src/run.sh bench <stack-name> 15 8      # 15 seconds, 8 parallel streams
```

`/benchmark` reads a file on EFS with N parallel `O_DIRECT` streams and samples `/proc/net/dev` once a second, reporting the per-second series alongside the peak and the sustained median. Three things make the numbers meaningful:

* **`O_DIRECT`.** Without it the guest page cache absorbs re-reads and you measure memory bandwidth, not the network path to EFS.
* **Parallel streams.** A single stream does not saturate the allocation; throughput flattens at around 8.
* **A per-second series, not an average.** The egress allocation is a token bucket: an idle MicroVM bursts well above its sustained rate for the first several seconds. An average over the whole run blends the two into a figure that describes neither.

Sustained throughput scales with `MinimumMemoryInMiB` — redeploy with a larger value and re-run `bench` to watch it move. The burst ceiling, by contrast, is roughly the same at every size, so bursty interactive access to EFS performs well even on a small MicroVM; only sustained streaming is size-limited.

The file system is created with **elastic** throughput so that EFS scales on demand far above any single MicroVM's allocation. With bursting or a low provisioned value you would be measuring EFS rather than the MicroVM.

## Other base images

The **guest OS** is always the Lambda-managed Amazon Linux 2023 base image (`--base-image-arn`); that is not a choice. What *is* free is the **container base image**, the `FROM` line in `src/Dockerfile`. This pattern uses `public.ecr.aws/amazonlinux/amazonlinux:2023` purely because `amazon-efs-utils` and `nfs-utils` install from Amazon's repos in one line.

A RHEL 9 (UBI 9) userspace works and measures within 0.5% on EFS throughput. One catch if you switch: **`nfs-utils` is not in the UBI 9 repositories**, so `mount -t efs` has no NFS helper to call. Either install the `amazon-efs-utils` RPM explicitly, or call `mount(2)` directly with `addr=` and `clientaddr=` — which needs no package at all.

Note that arm64 is required: `CpuConfigurations.Architecture` accepts only `ARM_64`.

## Cleanup

1. Terminate the running MicroVM:

    ```
    ./src/run.sh terminate <stack-name>
    ```

2. Delete the CloudFormation stack. Unlike an S3-backed pattern there is nothing to empty first — EFS file systems delete with their data, so this removes the image, the file system, mount target and access point, the connector, the roles, and the log group in one step:

    ```
    sam delete --stack-name <stack-name> --region us-west-2
    ```

3. Confirm the stack is deleted (should print nothing):

    ```
    aws cloudformation list-stacks --region us-west-2 \
      --query "StackSummaries[?StackName=='<stack-name>' && StackStatus!='DELETE_COMPLETE'].StackStatus"
    ```

4. **If you created a dedicated VPC/subnet for this pattern**, it is *not* part of the stack — delete it separately once the stack is gone.

5. The artifact bucket from step 3 of the deployment is also outside the stack. Remove it if you no longer need it:

    ```
    aws s3 rm s3://<your-artifact-bucket>/app.zip --region us-west-2
    aws s3api delete-bucket --bucket <your-artifact-bucket> --region us-west-2
    ```

----
SPDX-License-Identifier: MIT-0

Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.
