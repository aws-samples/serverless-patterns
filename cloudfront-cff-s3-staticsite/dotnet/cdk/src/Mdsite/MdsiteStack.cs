using Amazon.CDK;
using Amazon.CDK.AWS.S3;
using Amazon.CDK.AWS.S3.Deployment;
using Amazon.CDK.AWS.CloudFront;
using Constructs;
using Amazon.CDK.AWS.CloudFront.Origins;

namespace Mdsite
{
    public class MdsiteStack : Stack
    {
        public readonly CfnOutput MdSiteUrl;
        internal MdsiteStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            var mdsitebucket = new Bucket(this, "md-site-bucket", new BucketProps
            {
                Versioned = true
            });

            new BucketDeployment(this, "DeployFiles", new BucketDeploymentProps()
            {
                Sources = new[] {
                    Source.Asset("mycontent/site")
                    },
                DestinationBucket = mdsitebucket
            });

            Function cfFunction = new Function(this, "append-index-html", new FunctionProps
            {
                Code = FunctionCode.FromFile(new FileCodeOptions()
                {
                    FilePath = "cloudfrontfunction/append-index-html.js"
                })
            });

            var md_distribution = new Distribution(this, "md-site-distribution", new DistributionProps()
            {
                DefaultBehavior = new BehaviorOptions
                {
                    Origin = new S3Origin(mdsitebucket),
                    FunctionAssociations = new FunctionAssociation[]
                    {
                        new FunctionAssociation {
                            Function = cfFunction,
                            EventType = FunctionEventType.VIEWER_REQUEST
                        }
                    }
                }
            });

            this.MdSiteUrl = new CfnOutput(this, "CloudFront URL", new CfnOutputProps
            {
                Value = string.Format("https://{0}", md_distribution.DomainName)
            });
        }
    }
}
