using Amazon.CDK;
using Amazon.CDK.AWS.CloudFront;
using Amazon.CDK.AWS.S3;
using Amazon.CDK.AWS.S3.Deployment;
using Constructs;
using System.IO;
using System;
using System.Security.Cryptography;

namespace Cdk
{
    public class CdkStack : Stack
    {
        internal CdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // 1. Generate a new 2048 bit RSA key
            var rsa = new RSACryptoServiceProvider(2048);

            // Private key format: PKCS#1
            var publicPrivateKeyPEM = rsa.ExportRSAPrivateKeyPem();
            
            // Public key format: X.509 SubjectPublicKeyInfo
            var publicOnlyKeyPEM = rsa.ExportSubjectPublicKeyInfoPem(); 



            // 2. Create S3 bucket
            var s3Bucket = new Bucket(this, "Bucket", new BucketProps
            {
                Versioned = false,
                PublicReadAccess = false,
                BlockPublicAccess = BlockPublicAccess.BLOCK_ALL
            });

            // 3. Copy private content
            new BucketDeployment(this, "CopyFiles", new BucketDeploymentProps
            {
                Sources = new[]
                {
                    Source.Asset("../private-content")
                },
                DestinationBucket = s3Bucket
            });

            // 4. Create public key for CloudFront Key Group
            var publicKeyConstruct = new PublicKey(this, "PublicKey", new PublicKeyProps
            {
                PublicKeyName = "MyAppPublicKey",
                EncodedKey = publicOnlyKeyPEM
            });

            // 5. Create CloudFront Behaviour that validates Signed URLs or Signed Cookies using the public key
            var defaultBehavior = new Behavior();
            defaultBehavior.IsDefaultBehavior = true;
            defaultBehavior.ViewerProtocolPolicy = ViewerProtocolPolicy.REDIRECT_TO_HTTPS;
            defaultBehavior.TrustedKeyGroups = new KeyGroup[] {
                new KeyGroup(this,"KeyGroup", new KeyGroupProps
                {
                    KeyGroupName = "MyApp-KeyGroup",
                    Items = new[] { publicKeyConstruct }
                })
            };

            // 6. Create OAI user, and grant it access on S3 bucket
            var originAccessIdentity = new OriginAccessIdentity(this, "OAI");
            s3Bucket.GrantRead(originAccessIdentity);

            // 7. Creating the CloudFront distribution that serves the files from the S3 bucket
            var distribution = new CloudFrontWebDistribution(this, "ContentDistribution", new CloudFrontWebDistributionProps
            {
                PriceClass = PriceClass.PRICE_CLASS_100,
                OriginConfigs = new ISourceConfiguration[]
                {
                    new SourceConfiguration
                    {
                        S3OriginSource = new S3OriginConfig
                        {
                            S3BucketSource = s3Bucket,
                            OriginAccessIdentity = originAccessIdentity,
                        },
                        Behaviors = new Behavior[] { defaultBehavior }
                    }
                }
            });


            // PRINT OUTPUT
            string pdfFileUrl = $"https://{distribution.DistributionDomainName}/sample.pdf";

            new CfnOutput(this, "RESOURCE_URL", new CfnOutputProps { Value = pdfFileUrl });
            new CfnOutput(this, "CLOUDFRONT_PUBLIC_KEY_ID", new CfnOutputProps { Value = publicKeyConstruct.PublicKeyId });
            new CfnOutput(this, "PRIVATE_KEY", new CfnOutputProps { Value = publicPrivateKeyPEM });
        }
    }
}
