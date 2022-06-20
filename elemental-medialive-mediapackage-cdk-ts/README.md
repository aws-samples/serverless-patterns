
# Live Streaming on AWS using AWS Elemental MediaLive and AWS Elemental MediaPackage

This sample project demonstrates how to implement Live streaming on AWS at scale leveraging AWS Elemental MediaLive, MediaPackage.

![Concept](img/diagram.drawio.png)

To solution Configures AWS Elemental MediaLive with one of three encoding profiles based on the source resolution defined at launch as a CloudFormation parameter.

  source/custom-resource/lib/medialive/encoding-profiles/

## AWS Elemental MediaLive

The solution can be configured with the following input type:

- RTP_PUSH
- RTMP_PUSH
- RTMP_PULL
- URL_PULL

3 encoding profiles are available:

- HD-1080p profile: 1920x1080, 1280x720, 960x540, 768x432, 640x360, 512x288
- HD-720p profile: 1280x720, 960x540, 768x432, 640x360, 512x288
- SD-540p profile: 960x540, 768x432, 640x360, 512x288

The profiles are defined in JSON and and can be found in:

```
config/encoding-profiles
```

## AWS Elemental MediaPackage

Ingests the MediaLive Output and package the Live stream into:

- HLS
- DASH
- CMAF

Each format is delivered through a MediaPackage custom endpoint.

Learn more about this pattern at: https://serverlessland.com/patterns/elemental-medialive-mediapackage-cdk-ts

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the AWS Pricing page for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.


TODO
