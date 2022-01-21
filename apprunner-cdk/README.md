# AWS AppRunner Service

This project contains a sample AWS Cloud Development Kit (AWS CDK) template for deploying an AWS AppRunner service. 
This template showes how to add a custom image for AWS AppRunner service to use without having to pre-push the image to Amazon Elastic Container Registry (ECR) or another container library. This makes use of the in-built `apprunner.Source.fromAsset` method.
The custom image used is a simple hello world Node Js application. This project also provides an example of how to pass an environment variable to the image. Note that the image can be changed to other images that suit your use case by changing the codes found in the src directory.