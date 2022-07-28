
# Live Streaming content at scale using Amazon CloudFront

This pattern demonstrates how to create MediaPackage custom endpoints as the Origins for a CloudFront distribution to enable the live stream content to be delivered globally and at scale.

![Concept](img/diagram.drawio.png)

## AWS Elemental MediaPackage

Ingests the MediaLive Output and package the Live stream into:

- HLS
- DASH


Each format is delivered through a MediaPackage custom endpoint. There is a [CDN authorization](https://docs.aws.amazon.com/mediapackage/latest/ug/cdn-auth.html) implemented for each endpoint to reinforce the security through a secret store on [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/). This is the way to secure the access to each MediaPackage endpoints.
The solution will create HLS, MPEG-DASH outputs with SCTE35 in Passthrough mode.

## Amazon CloudFront

A distribution is created to provide URL for HLS and MPEG-DASH. The default managed cache policy ELEMENTAL_MEDIA_PACKAGE is used for each behavior.
The output will provide URL for HLS and MPEG-DASH to play only from CloudFront (MediaPackage endpoints are secured using CDN authorization).

Learn more about this pattern at: https://serverlessland.com/patterns/elemental-mediapackage-cloudfront

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) (AWS CDK >= 2.2.0) Installed

## Language

Typescript

## Framework

CDK

## Services From/To

Aws Elemental Media Package -> Amazon CloudFront

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change directory to the pattern directory:

    ```bash
    cd elemental-mediapackage-cloudfront-cdk-ts
    ```

1. Install node modules:

    ```bash
    npm install
    ```

1. From the command line, use CDK to deploy the stack:

    ```bash
    cdk deploy
    ```

    Expected result:

    ```bash
    Outputs:
    StreamingStack.MediaPackageDashUrlStream20F09B6A = https://aaabbbcccddd.mediapackage.eu-west-1.amazonaws.com/out/v1/bffed8f1b33c428ca5d701b2023fde26/index.mpd

    StreamingStack.MediaPackageHlsUrlStreamF9304AC0 = https://aaabbbcccddd.mediapackage.eu-west-1.amazonaws.com/out/v1/e4e4df6e2f804e6897f96e72d8b18752/index.m3u8

    StreamingStack.MediaPackageMssUrlStream155D638F = https://aaabbbcccddd.mediapackage.eu-west-1.amazonaws.com/out/v1/dee22f1df1b24549b0ed85d680a51f50/index.ism/Manifest

    StreamingStack.MyCloudFrontDashEndpoint81378E6C = https://xxxxxxxxxxxx.cloudfront.net/out/v1/bffed8f1b33c428ca5d701b2023fde26/index.mpd

    StreamingStack.MyCloudFrontHlsEndpointBE112935 = https://xxxxxxxxxxxx.cloudfront.net/out/v1/e4e4df6e2f804e6897f96e72d8b18752/index.m3u8

    StreamingStack.MyCloudFrontMssEndpoint3844E3DD = https://xxxxxxxxxxxx.cloudfront.net/out/v1/dee22f1df1b24549b0ed85d680a51f50/index.ism/Manifest
    ```

1. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

### Testing

To test this you need to get a stream into MediaPackage. You can have a look [here](https://github.com/aws-samples/serverless-patterns/tree/main/elemental-medialive-mediapackage-cdk-ts) or [here](https://github.com/aws-samples/serverless-patterns/tree/main/elemental-mediaconnect-medialive-mediapackage-cdk-ts) for a SRT or RTP/RTMP stream as source for MediaConnect.

## Cleanup


1. Delete the stack

    ```bash
    cdk destroy
    ```

## Tutorial

See [this useful workshop](https://cdkworkshop.com/20-typescript.html) on working with the AWS CDK for typescript projects.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation


Enjoy!
