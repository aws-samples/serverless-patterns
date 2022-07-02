
# Live Streaming on AWS using RTP/RTMP sources

This pattern creates a live streaming stack leveraging AWS Elemental MediaLive, MediaPackage for RTP/RTMP input sources.

![Concept](img/diagram.drawio.png)

## AWS Elemental MediaLive

To solution Configures AWS Elemental MediaLive with one of three encoding profiles.

  source/custom-resource/lib/medialive/encoding-profiles/

The encoding profile used when deploying the stack is specified using the parameter ```type``` in the file:

```
config/media_live.json
````

The solution can be configured with the following input type:

- RTP_PUSH
- RTMP_PUSH
- RTMP_PULL
- URL_PULL

3 encoding profiles are available:

```
config/encoding-profiles/hd-1080p.json
config/encoding-profiles/hd-720p.json
config/encoding-profiles/sd-540p.json
```

- **HD-1080p** profile: 1920x1080, 1280x720, 960x540, 768x432, 640x360, 512x288
- **HD-720p** profile: 1280x720, 960x540, 768x432, 640x360, 512x288
- **SD-540p** profile: 960x540, 768x432, 640x360, 512x288

## AWS Elemental MediaPackage

Ingests the MediaLive Output and package the Live stream into:

- HLS
- DASH
- CMAF

Each format is delivered through a MediaPackage custom endpoint.

Learn more about this pattern at: https://serverlessland.com/patterns/elemental-medialive-mediapackage-cdk-ts

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

AWS Elemental Media Live -> Aws Elemental Media Package

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:

    ```bash
    git clone https://github.com/aws-samples/serverless-patterns
    ```

1. Change directory to the pattern directory:

    ```bash
    cd elemental-medialive-mediapackage-cdk-ts
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

    StreamingStack.MediaLiveMediaLiveChannelArn9CBFE74E = arn:aws:medialive:eu-west-1:xxxxxxxxx:channel:5487010

    StreamingStack.MediaLiveMediaLiveEndpoint6C24CC11 = rtmp://STREAMING_IP_ADDRESS:STREAMING_PORT/live/primary

    StreamingStack.MediaPackageChannelDashEndpointURL075A4782 = https://aaaaaxxxxxccccvvv.mediapackage.eu-west-1.amazonaws.com/out/v1/9ba56ae160074159b272ee751fb3d20b/index.mpd

    StreamingStack.MediaPackageChannelHlsEndpointURL3F32439A = https://aaaaaxxxxxccccvvv.mediapackage.eu-west-1.amazonaws.com/out/v1/6cfa1b541d2e461d9e8af5cd03ce41ca/index.m3u8

    StreamingStack.MediaPackageChannelMssEndpointURL2826FEB1 = https://aaaaaxxxxxccccvvv.mediapackage.eu-west-1.amazonaws.com/out/v1/4914c65c06e9426bb6de3cb460ce1534/index.ism/Manifest
    ```

1. Note the outputs from the CDK deployment process. These contain the resource names and/or ARNs which are used for testing.

### Testing

1. Start Media Live channel using the channelId from the MediaLiveChannelArn:

    ```bash
    aws medialive start-channel --channel-id 5487010
    ```

    Wait for the channel to start

    ```bash
    while true ; do CHANNEL_STATUS=`aws medialive describe-channel --channel-id 5487010 --query "State" --output text` ; if [ $CHANNEL_STATUS == "RUNNING" ] ; then echo "Channel 5487010 is started" ; break ; else echo "Channel 5487010 is not started"; fi ; sleep 5 ; done
    ```

2. Configure your streaming app using the url from `MediaLiveMediaLiveEndpoint6C24CC11` and start streaming

3. Use the Endpoint URL (`MediaPackageChannelDashEndpointURL075A4782` or `MediaPackageChannelHlsEndpointURL3F32439A` or `MediaPackageChannelMssEndpointURL2826FEB1`) to play the video stream in any compatible player


## Cleanup

1. Stop Media Live channel

    ```bash
    aws medialive stop-channel --channel-id 5487010
    ```

    Wait for the channel to stop

    ```bash
    while true ; do CHANNEL_STATUS=`aws medialive describe-channel --channel-id 5487010 --query "State" --output text` ; if [ $CHANNEL_STATUS == "IDLE" ] ; then echo "Channel 5487010 is stopped" ; break ; else echo "Channel 5487010 is not stopped"; fi ; sleep 5 ; done
    ```


2. Delete the stack

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
