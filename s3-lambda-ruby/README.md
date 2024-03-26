# s3-lambda-ruby

## Introduction

This example shows how to use SAM to deploy a AWS Lambda Ruby 3.2 function that relies on a number of shared libraries which
are not part of the default runtime environment. The Lambda function is triggered by an S3 event (the upload of a JPEG image).
When triggered it will fetch the image, resize the image, and then place the new image in another S3 bucket. To do the
resizing we are using the RMagick gem. This depends on ImageMagick being available when we build the application and
at runtime.

To keep the ImageMagick shared libraries separate from the application code we'll create and deploy them using a Lambda
Layer. To be able to do so, we need to have the shared libraries available in the build environment. Thus the first step
is to create a custom build container into which we install the ImageMagick libraries. ImageMagick is available in
the Amazon Linux 2 repositories, but is not installed by default.

We're using arm64 as the Lambda processor architecture, but the same steps can be adapted for x86_64 processors.

The overall steps for this process are thus:

1. [Build a custom build container containing ImageMagick](#build-a-custom-build-container)
2. [Build a Lambda Layer containing the ImageMagick shared objects](#build-a-lambda-layer-containing-the-imagemagick-shared-objects)
3. [Build the application .zip archive](#build-the-application-zip-archive)
4. [Deploy the application](#deploy-the-application)
5. [Test the deployed application]()

## Build a custom build container

Our first step is to create a custom build container. We use the `build-ruby3.2:latest-arm64` container as
a base and install the tools and dependencies that are needed to build and use the RMagick gem.

```shell
$ cd build_container
$ docker build -t awsruby32:arm64
[..snipped build logs..]
$ docker images -a -f reference=awsruby32
REPOSITORY   TAG       IMAGE ID       CREATED         SIZE
awsruby32    arm64     2a25ef0baea0   2 minutes ago   3.53GB
```

## Build a Lambda Layer containing the ImageMagick shared objects

We now want to create a Lambda Layer which will contain the ImageMagick libraries, the dependencies for ImageMagick, and
the ImageMagick `coders` (which are loadable objects used by ImageMagick to support different image types). These
were all installed when we built the custom build container. We use the `Makefile` build method to create the layer. 

```shell
$ sam build --use-container --build-image awsruby32:arm64 --skip-pull-image ImageMagickLayer
```

## Build the application .zip archive

Now we can build the application .zip archive. We use the custom build image as the container to ensure that the
native extensions for the RMagick gem are built correctly and included in the archive.

```shell
$ sam build --use-container --build-image awsruby32:arm64 --skip-pull-image ImageResizerFunction
```

## Deploy the application

We can use `--guided` with `sam deploy` to interactively create and save deployment defaults to the `samconfig.toml`
file.

```shell
$ sam deploy --guided


Configuring SAM deploy
======================

	Looking for config file [samconfig.toml] :  Not found

	Setting default arguments for 'sam deploy'
	=========================================
	Stack Name [sam-app]: s3-lambda-ruby
	AWS Region [us-east-1]:
	Parameter SourceBucketName []: source-bucket-123456789012
	Parameter DestinationBucketName []: destination-bucket-123456789012
	#Shows you resources changes to be deployed and require a 'Y' to initiate deploy
	Confirm changes before deploy [y/N]:
	#SAM needs permission to be able to create roles to connect to the resources in your template
	Allow SAM CLI IAM role creation [Y/n]:
	#Preserves the state of previously provisioned resources when an operation fails
	Disable rollback [y/N]:
	Save arguments to configuration file [Y/n]:
	SAM configuration file [samconfig.toml]:
	SAM configuration environment [default]:

	Looking for resources needed for deployment:

	Managed S3 bucket: aws-sam-cli-managed-default-samclisourcebucket-12zeczklryers
	A different default S3 bucket can be set in samconfig.toml and auto resolution of buckets turned off by setting resolve_s3=False

	Saved arguments to config file
	Running 'sam deploy' for future deployments will use the parameters saved above.
	The above parameters can be changed by modifying samconfig.toml
	Learn more about samconfig.toml syntax at
	https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-config.html

	Uploading to s3-lambda-ruby/569d2bb82ed431fae9d597a3d54b2eb5  9094081 / 9094081  (100.00%)
	Uploading to s3-lambda-ruby/02afc764b9dd27f22c1df6a8acebe745  2203790 / 2203790  (100.00%)

	Deploying with following values
	===============================
	Stack name                   : s3-lambda-ruby
	Region                       : us-east-1
	Confirm changeset            : False
	Disable rollback             : False
	Deployment s3 bucket         : aws-sam-cli-managed-default-samclisourcebucket-12zeczklryers
	Capabilities                 : ["CAPABILITY_IAM"]
	Parameter overrides          : {"SourceBucketName": "source-bucket-123456789012", "DestinationBucketName": "destination-bucket-123456789012"}
	Signing Profiles             : {}

Initiating deployment
=====================

	Uploading to s3-lambda-ruby/5d9aa7144ce37fe8963a0139d4d8e6ba.template  2326 / 2326  (100.00%)


Waiting for changeset to be created..

CloudFormation stack changeset
-------------------------------------------------------------------------------------------------------------
Operation                   LogicalResourceId           ResourceType                Replacement
-------------------------------------------------------------------------------------------------------------
+ Add                       DestinationBucket           AWS::S3::Bucket             N/A
+ Add                       ImageMagickLayer6c4eb22f8   AWS::Lambda::LayerVersion   N/A
                            e
+ Add                       ImageResizerFunctionFileU   AWS::Lambda::Permission     N/A
                            ploadPermission
+ Add                       ImageResizerFunctionRole    AWS::IAM::Role              N/A
+ Add                       ImageResizerFunction        AWS::Lambda::Function       N/A
+ Add                       SourceBucket                AWS::S3::Bucket             N/A
-------------------------------------------------------------------------------------------------------------


Changeset created successfully. arn:aws:cloudformation:us-east-1:123456789012:changeSet/samcli-deploy1709721946/71b426f4-de8f-4f6e-8f78-b3ba754bbfc8


2024-03-06 11:45:53 - Waiting for stack create/update to complete

CloudFormation events from stack operations (refresh every 5.0 seconds)
-------------------------------------------------------------------------------------------------------------
ResourceStatus              ResourceType                LogicalResourceId           ResourceStatusReason
-------------------------------------------------------------------------------------------------------------
CREATE_IN_PROGRESS          AWS::CloudFormation::Stac   s3-lambda-ruby              User Initiated
                            k
CREATE_IN_PROGRESS          AWS::IAM::Role              ImageResizerFunctionRole    -
CREATE_IN_PROGRESS          AWS::S3::Bucket             DestinationBucket           -
CREATE_IN_PROGRESS          AWS::Lambda::LayerVersion   ImageMagickLayer6c4eb22f8   -
                                                        e
CREATE_IN_PROGRESS          AWS::IAM::Role              ImageResizerFunctionRole    Resource creation
                                                                                    Initiated
CREATE_IN_PROGRESS          AWS::S3::Bucket             DestinationBucket           Resource creation
                                                                                    Initiated
CREATE_IN_PROGRESS          AWS::Lambda::LayerVersion   ImageMagickLayer6c4eb22f8   Resource creation
                                                        e                           Initiated
CREATE_COMPLETE             AWS::Lambda::LayerVersion   ImageMagickLayer6c4eb22f8   -
                                                        e
CREATE_COMPLETE             AWS::IAM::Role              ImageResizerFunctionRole    -
CREATE_IN_PROGRESS          AWS::Lambda::Function       ImageResizerFunction        -
CREATE_COMPLETE             AWS::S3::Bucket             DestinationBucket           -
CREATE_IN_PROGRESS          AWS::Lambda::Function       ImageResizerFunction        Resource creation
                                                                                    Initiated
CREATE_IN_PROGRESS          AWS::Lambda::Permission     ImageResizerFunctionFileU   -
                                                        ploadPermission
CREATE_IN_PROGRESS          AWS::Lambda::Permission     ImageResizerFunctionFileU   Resource creation
                                                        ploadPermission             Initiated
CREATE_COMPLETE             AWS::Lambda::Permission     ImageResizerFunctionFileU   -
                                                        ploadPermission
CREATE_COMPLETE             AWS::Lambda::Function       ImageResizerFunction        -
CREATE_IN_PROGRESS          AWS::S3::Bucket             SourceBucket                -
CREATE_IN_PROGRESS          AWS::S3::Bucket             SourceBucket                Resource creation
                                                                                    Initiated
CREATE_COMPLETE             AWS::S3::Bucket             SourceBucket                -
CREATE_COMPLETE             AWS::CloudFormation::Stac   s3-lambda-ruby              -
                            k
-------------------------------------------------------------------------------------------------------------

CloudFormation outputs from deployed stack
---------------------------------------------------------------------------------------------------------------
Outputs
---------------------------------------------------------------------------------------------------------------
Key                 ImageResizerFunction
Description         Image Resizer Lambda Function ARN
Value               arn:aws:lambda:us-east-1:123456789012:function:s3-lambda-ruby-ImageResizerFunction-
SFJqeD2er0BR
---------------------------------------------------------------------------------------------------------------


Successfully created/updated stack - s3-lambda-ruby in us-east-1
```

Future deployments can now use `sam deploy` with no parameters to deploy updates to the application.

## Test the deployed application

To test the application we'll upload a JPEG to the source bucket. After a few seconds it should appear
in the destination bucket and we should see some log lines appearing.

You'll need two terminal windows open. In the first we'll tail the logs:

```shell
$ sam logs -t --stack-name s3-lambda-ruby
```

In the second terminal window we upload the image to S3:

```shell
$ aws s3 cp image.jpg s3://source-bucket-123456789012/
```

After a few seconds we should see log entries being displayed by `sam logs`:

```shell
2024/03/06/[$LATEST]b15bd38cf94a444889e32571e0aa080d 2024-03-06T13:19:52.059000 INIT_START Runtime Version: ruby:3.2.v14        Runtime Version ARN: arn:aws:lambda:us-east-1::runtime:c2bf444aaa97fb21e2bda8f3c44c7baa21844c9a10d005db32672d17f184b9a3
2024/03/06/[$LATEST]b15bd38cf94a444889e32571e0aa080d 2024-03-06T13:19:53.048000 START RequestId: 05762661-d2cb-4645-83ec-cb38ae7385c1 Version: $LATEST
2024/03/06/[$LATEST]b15bd38cf94a444889e32571e0aa080d 2024-03-06T13:19:53.049000 {
  "time": "2024-03-06T13:19:53.0497",
  "level": "INFO",
  "message": "Resizing image.jpg"
}
2024/03/06/[$LATEST]b15bd38cf94a444889e32571e0aa080d 2024-03-06T13:19:54.991000 {
  "time": "2024-03-06T13:19:54.9916",
  "level": "INFO",
  "message": "Initial size: 1275x1650"
}
2024/03/06/[$LATEST]b15bd38cf94a444889e32571e0aa080d 2024-03-06T13:19:56.093000 {
  "time": "2024-03-06T13:19:56.0929",
  "level": "INFO",
  "message": "Final size: 371x480"
}
2024/03/06/[$LATEST]b15bd38cf94a444889e32571e0aa080d 2024-03-06T13:19:56.462000 {
  "time": "2024-03-06T13:19:56.4628",
  "level": "INFO",
  "message": "S3 Etag: \"7fdab5968210a0c7c7e5e36e16b5ef95\""
}
2024/03/06/[$LATEST]b15bd38cf94a444889e32571e0aa080d 2024-03-06T13:19:56.509000 END RequestId: 05762661-d2cb-4645-83ec-cb38ae7385c1
2024/03/06/[$LATEST]b15bd38cf94a444889e32571e0aa080d 2024-03-06T13:19:56.509000 REPORT RequestId: 05762661-d2cb-4645-83ec-cb38ae7385c1  Duration: 3460.54 ms    Billed Duration: 3461 ms       Memory Size: 128 MB     Max Memory Used: 123 MB Init Duration: 987.66 ms   
```

We can confirm that the image now exists in the destination bucket:

```shell
$ aws s3 ls s3://destination-bucket-123456789012/
2024-03-06 14:19:57      30591 image.jpg
```

## Clean up

When we are finished experimenting we can clean up the resources created.
We will need to empty the S3 buckets before we can destroy the stack:

```shell
$ aws s3 rm --recursive s3://source-bucket-123456789012
delete: s3://source-bucket-123456789012/image.jpg
$ aws s3 rm --recursive s3://destination-bucket-123456789012  
delete: s3://destination-bucket-123456789012/image.jpg
```

Finally we can remove the stack using `sam delete`:

```shell
$ sam delete --no-prompts
        - Deleting S3 object with key s3-lambda-ruby/f57c1ce023ba51d2bc8aab8ea0c38286                                                                                  
        - Deleting S3 object with key s3-lambda-ruby/f95b1ac3984728ce006b718dd80fc8ad.template                                                                         
        - Deleting Cloudformation stack s3-lambda-ruby

Deleted successfully
```