using Amazon.CDK;
using Amazon.CDK.AWS.CloudFront;
using Amazon.CDK.AWS.CloudFront.Origins;
using Amazon.CDK.AWS.S3;
using Amazon.CDK.AWS.S3.Deployment;
using Constructs;

namespace StaticSite
{
    public class StaticSiteStack : Stack
    {
        internal StaticSiteStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
             // Create an S3 bucket for static website hosting
            var siteBucket = new Bucket(this, "SiteBucket");

            // Deploy website contents to S3 bucket
            new BucketDeployment(this, "DeployWebsite", new BucketDeploymentProps
            {
                Sources = new[] { Source.Asset("static-site-content") },
                DestinationBucket = siteBucket,
            });

            // Define the CloudFront Function for geolocation redirection
            var geoRedirectFunction = new Function(this, "GeoRedirectFunction", new FunctionProps
            {
                Code = FunctionCode.FromInline(@"function handler(event) {
                    var request = event.request;
                    var uri = request.uri;
                    var headers = request.headers;
                    var country = headers['cloudfront-viewer-country'] ? headers['cloudfront-viewer-country'].value : null;

                    if (country) {
                        switch (country) {
                            case 'US':
                                // If the user is from the US, rewrite the URI to start with /us
                                uri = '/us' + uri;
                                break;
                            case 'PL':
                                // If the user is from Poland, rewrite the URI to start with /pl
                                uri = '/pl' + uri;
                                break;
                            default:
                                // For users from any other country, use the /intl path
                                uri = '/intl' + uri;
                                break;
                        }
                    } else {
                        // If the country can't be determined, use the default /intl path
                        uri = '/intl' + uri;
                    }

                    // Update the URI in the original request
                    request.uri = uri;

                    // Return the modified request
                    return request;
                }"),
                FunctionName = "GeoRedirectFunction"
            });

            // Create a CloudFront distribution to serve the static website from S3
            var distribution = new Distribution(this, "SiteDistribution", new DistributionProps
            {
                DefaultBehavior = new BehaviorOptions
                {
                    Origin = new S3Origin(siteBucket),
                    OriginRequestPolicy = new OriginRequestPolicy(this, "OriginRequestPolicy", new OriginRequestPolicyProps
                    {
                        Comment = "Origin request policy for geolocation",
                        HeaderBehavior = OriginRequestHeaderBehavior.AllowList("CloudFront-Viewer-Country")
                    }),
                    ViewerProtocolPolicy = ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                    FunctionAssociations = new IFunctionAssociation[] {
                        new FunctionAssociation {
                            EventType = FunctionEventType.VIEWER_REQUEST,
                            Function = geoRedirectFunction,
                        }
                    }
                }
            });

            // Output the url to the distribution index.
            new CfnOutput(this, "DistributionURL", new CfnOutputProps
            {
                Value = string.Format("https://{0}/index.html", distribution.DistributionDomainName),
            });
        }
    }
}
