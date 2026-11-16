# Serving private content from CloudFront with signed URLs and signed cookies

This pattern demonstrates how to use CloudFront to securely serve private content.

In this pattern, the CDK stack creates an S3 bucket and a CloudFront distribution that is configured to accept requests with only valid signed URLs or signed Cookies.

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/cloudfront-s3-cdk-dotnet

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [.NET](https://dotnet.microsoft.com/en-us/download) installed
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Clone the project to your local working directory
    ```
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change the working directory to this pattern's directory
    ```
    cd cloudfront-s3/dotnet/cdk/src/cdk/src
    ```
3. Build the application
    ```
    dotnet build
    ```
4. Return one level back to the path `cloudfront-s3/dotnet/cdk/src/cdk`
    ```
    cd ..
    ```
5. Generate an RSA key pair with OpenSSL. CloudFront only needs the public key, so the stack reads `public_key.pem` and the private key stays on your machine. Both files are listed in `.gitignore`, so don't commit them.
    ```
    openssl genrsa -out private_key.pem 2048
    openssl rsa -pubout -in private_key.pem -out public_key.pem
    ```
    To use a public key stored somewhere else, add `-c publicKeyFile=<path>` to the `cdk deploy` command.
6. Deploy the stack to your default AWS account and region. The output shows the URL of a `sample.pdf` document and the ID of the CloudFront public key.
    ```
    cdk deploy
    ```

## Testing

1. After deployment, the output displays the following values.
   - Resource URL: `CloudFrontToS3CdkStack.RESOURCEURL = https://d1vdgbnd2t5hch.cloudfront.net/sample.pdf`
   - Public Key Id: `CloudFrontToS3CdkStack.CLOUDFRONTPUBLICKEYID = K2UQHVS54O0BAQ`
2. The PDF resource is only accessible with a signed URL. Opening the resource URL without a signature returns a `403` error.
3. Use the following function to generate a signed URL with your local private key, then use that URL to access the PDF resource.
    ```cs
    string GenerateCloudFrontSignedURL(string resourceUrl, string publicKeyId, string privateKeyFile)
    {
        string policyDoc = AmazonCloudFrontUrlSigner.BuildPolicyForSignedUrl(
            resourceUrl,
            DateTime.Now.AddDays(+1),
            null);

        // Accepts PKCS#1 or PKCS#8 PEM files and passes the key to the signer as PKCS#1.
        using var rsa = RSA.Create();
        rsa.ImportFromPem(File.ReadAllText(privateKeyFile));
        return AmazonCloudFrontUrlSigner.SignUrl(resourceUrl, publicKeyId, new StringReader(rsa.ExportRSAPrivateKeyPem()), policyDoc);
    }
    ```
    For example, `GenerateCloudFrontSignedURL("https://d1vdgbnd2t5hch.cloudfront.net/sample.pdf", "K2UQHVS54O0BAQ", "private_key.pem")`.
4. The above code requires the `AWSSDK.CloudFront` NuGet package and the `Amazon.CloudFront` and `System.Security.Cryptography` namespaces.


## Cleanup

1. Run the given command to delete the resources that were created. It might take some time for the CloudFormation stack to get deleted.
    ```
    cdk destroy
    ```
2. Delete the local key pair.
    ```
    rm private_key.pem public_key.pem
    ```

----
Copyright 2023 Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: MIT-0
