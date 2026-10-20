# Auto-quarantine vulnerable Amazon ECR images with Amazon Inspector, Amazon EventBridge, and AWS Step Functions

This pattern automatically quarantines a vulnerable container image the moment Amazon Inspector raises a HIGH or CRITICAL finding on it. An Amazon Inspector finding on an Amazon ECR container image is routed by Amazon EventBridge to an AWS Step Functions workflow that re-tags the offending image with a per-image `quarantine-<digest>` tag and sends an Amazon SNS notification.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/inspector-sfn-ecr-quarantine-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Architecture

```
Amazon ECR image (vulnerable)
        │  enhanced scanning
        ▼
Amazon Inspector  ──finding──▶  Amazon EventBridge rule
                                 (source: aws.inspector2,
                                  detail-type: "Inspector2 Finding",
                                  severity: HIGH | CRITICAL,
                                  status: ACTIVE,
                                  resource type: AWS_ECR_CONTAINER_IMAGE,
                                  repository: the demo repository)
                                        │
                                        ▼
                          AWS Step Functions (STANDARD)
                          1. Choice: severity HIGH/CRITICAL?
                          2. ecr:BatchGetImage  (GetImageManifest: read manifest by digest)
                          3. Choice: manifest returned? (otherwise failure notification)
                          4. ecr:PutImage       (ApplyQuarantineTag: re-tag same manifest as
                                                 "quarantine-<digest hex>")
                          5. Amazon SNS publish (NotifyQuarantined / NotifyFailure)
                             Retry (transient errors) + Catch → failure notification
                             Ecr.ImageAlreadyExistsException → AlreadyQuarantined (no email)
```

The workflow reads the finding fields directly from the Amazon EventBridge event:
`$.detail.severity`, `$.detail.resources[0].details.awsEcrContainerImage.repositoryName`, and `$.detail.resources[0].details.awsEcrContainerImage.imageHash`.

The happy path through the state machine is `GetImageManifest` → `ApplyQuarantineTag` → `RebuildBranchHint` → `NotifyQuarantined`.

## Design decisions

- **How the image is quarantined (no AWS Lambda function required).** A container image in Amazon ECR is content-addressed by its digest; a tag is a named pointer to a manifest. To mark an existing image without rebuilding or copying layers, the workflow calls `ecr:BatchGetImage` to read the manifest by digest, then `ecr:PutImage` to write the **same** manifest bytes back under a new tag, forwarding the `ImageManifestMediaType` that `ecr:BatchGetImage` returned. Both calls are available as AWS Step Functions optimized AWS SDK service integrations, so the entire remediation runs from the state machine with no AWS Lambda function.
- **Tag mutability.** The demo Amazon ECR repository uses the default MUTABLE tags. The quarantine tag is unique to each image (`quarantine-<digest hex>`), so the workflow never moves an existing tag. This pattern was not tested against a repository with IMMUTABLE tags.
- **One tag per image.** A tag in an Amazon ECR repository points at exactly one image, so a fixed `quarantine` tag would move from one image to the next. The tag is derived from the image digest (`quarantine-<sha256 hex>`), so every quarantined image keeps its own marker that downstream Amazon ECR lifecycle policies or deployment admission controllers can key off by the `quarantine-` prefix.
- **Repeat findings.** Amazon Inspector raises one finding per vulnerability per image and emits another event whenever a finding changes state, so one image can start many executions. The first execution applies the tag. Later ones call `ecr:PutImage` with an identical manifest and tag, which returns `ImageAlreadyExistsException`; the workflow catches `Ecr.ImageAlreadyExistsException` ahead of the generic catch and ends in `AlreadyQuarantined` without sending another email. Only transient errors (`Ecr.ServerException`, `Ecr.ThrottlingException`, `States.Timeout`) are retried.
- **Rule scope.** The Amazon EventBridge rule matches only findings with `status` `ACTIVE` (so findings that move to `CLOSED` or `SUPPRESSED` do not start the workflow) on images in the demo repository, because the state machine role only has Amazon ECR permissions on that repository.
- **Image deleted before the workflow runs.** `ecr:BatchGetImage` returns HTTP 200 with an empty `images` list in that case. A Choice state (`HasImageManifest`) checks for the manifest and routes the missing case to the failure notification.
- **Rebuild/patch branch.** A documented extension point (`RebuildBranchHint`) is included where a real deployment would kick off a patched-image rebuild (for example, an AWS CodeBuild project). It is intentionally a no-op so the pattern stays focused on the quarantine headline.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Node.js 22 or later](https://nodejs.org/en/download/) installed (see the [AWS CDK prerequisites](https://docs.aws.amazon.com/cdk/v2/guide/prerequisites.html))
- [AWS Cloud Development Kit (AWS CDK) v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) installed
- **Amazon Inspector enhanced scanning for Amazon ECR must be enabled at the account level.** Enable it in the [Amazon Inspector console](https://console.aws.amazon.com/inspector/v2/home) (Account management → Activate → enable ECR scanning), or with `aws inspector2 enable --resource-types ECR`. Without this, no findings are generated and the workflow is never triggered.

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd inspector-sfn-ecr-quarantine-cdk/cdk
    ```
3. Install dependencies:
    ```
    npm install
    ```
4. If the target AWS account and Region have never been used with the AWS CDK, bootstrap them once (see [Bootstrapping](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html)):
    ```
    npx cdk bootstrap
    ```
5. Deploy the stack to your default AWS account and Region. The output of this command should give you the Amazon ECR repository name, the AWS Step Functions state machine ARN, and the Amazon SNS topic ARN:
    ```
    npx cdk deploy
    ```

## Testing

The headline of this pattern is that a HIGH/CRITICAL Amazon Inspector finding on an Amazon ECR image automatically results in that image being tagged `quarantine-<digest hex>`.

1. Subscribe your email to the Amazon SNS topic from the stack output so you receive notifications:
    ```
    aws sns subscribe --topic-arn <SnsTopicArn> --protocol email --notification-endpoint you@example.com
    ```
    Confirm the subscription from the email you receive.

2. Authenticate Docker to Amazon ECR and push a known-vulnerable image to the demo repository (using the `RepositoryUri` output; replace `<region>` with the AWS Region you deployed the stack to). A deliberately old base image reliably produces HIGH/CRITICAL findings:
    ```
    aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <RepositoryUri>
    docker pull public.ecr.aws/docker/library/ubuntu:20.04
    docker tag public.ecr.aws/docker/library/ubuntu:20.04 <RepositoryUri>:vulnerable
    docker push <RepositoryUri>:vulnerable
    ```

3. Amazon Inspector scans the image on push. When it reports a HIGH or CRITICAL finding (this can take a few minutes), Amazon EventBridge triggers the AWS Step Functions workflow. Watch the execution in the [AWS Step Functions console](https://console.aws.amazon.com/states/home), where you should see the `GetImageManifest` → `ApplyQuarantineTag` → `RebuildBranchHint` → `NotifyQuarantined` path succeed. Amazon Inspector emits one event per finding, so you may see several executions for the one push; the first applies the tag and the others are expected to end in `AlreadyQuarantined`.

4. Verify the image now carries a `quarantine-<digest hex>` tag, alongside its original tag, pointing at the same digest:
    ```
    aws ecr describe-images --repository-name <RepositoryName> \
      --query 'imageDetails[].imageTags'
    ```
    You should see the `quarantine-` tag in the tag list, and you will receive an Amazon SNS email confirming the quarantine with the repository, digest, and severity.

## Cleanup

1. Delete the stack. The demo Amazon ECR repository is created with `RemovalPolicy.DESTROY` and `emptyOnDelete`, so the repository **and any images you pushed into it (including the vulnerable test image) will be permanently deleted**:
    ```
    cd inspector-sfn-ecr-quarantine-cdk/cdk
    npx cdk destroy
    ```
2. Optionally, disable Amazon Inspector ECR enhanced scanning if you enabled it only for this test:
    ```
    aws inspector2 disable --resource-types ECR
    ```

----
Copyright 2026 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
