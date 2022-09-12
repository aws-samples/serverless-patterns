# Use Amazon Rekognition to index a faces within Lambda - with CDK (Typescript)

This pattern demonstrates how to index a face using Amazon Rekognition. When an image with headshot added into a S3 bucket, a Lamba function is triggered to index the face using Amazon Rekognition SDK.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/s3-lambda-rekognition-cdk

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

- [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
- [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Node and NPM](https://nodejs.org/en/download/) installed
- [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
   ```
   git clone https://github.com/aws-samples/serverless-patterns
   ```
2. Change directory to the pattern directory:
   ```
   cd s3-lambda-rekognition-cdk
   ```
3. Run below command to install required dependancies:

   ```
   npm install
   ```

4. From the command line, run:
   ```
   cdk deploy --all
   ```

## Testing

1. Upload a image with a headshot to S3 bucket created in the stack. File name of the image can be the name that is required to identify the person in the image. Ex: "Tom.jpg"

```
  aws s3 cp Tom.jpg s3://[S3BucketName]/Tom.jpg
```

2. Call the Rekognition list-faces API with the collection id.

```
  aws rekognition list-faces --collection-id "[FacesCollectionId]"
```

3. You should see the face is indexed with the file name as the ExternalImageId.

```
{
    "Faces": [
        {
            "FaceId": "1393dca4-15f3-4147-95f0-9abc37a2c8dc",
            "BoundingBox": {
                "Width": 0.30997100472450256,
                "Height": 0.39190998673439026,
                "Left": 0.33072400093078613,
                "Top": 0.16703000664710999
            },
            "ImageId": "9194dc03-f690-3623-a916-ff92f56251b0",
            "ExternalImageId": "Tom",
            "Confidence": 99.99889373779297
        }
    ]
}
```

## Cleanup

1. To delete the stack, run:
   ```bash
   cdk destroy --all
   ```

---

Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
