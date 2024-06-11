import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { CfnOutput, Duration, RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import * as acm from 'aws-cdk-lib/aws-certificatemanager';
import * as cloudfront from 'aws-cdk-lib/aws-cloudfront';
import * as origins from 'aws-cdk-lib/aws-cloudfront-origins';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as route53 from 'aws-cdk-lib/aws-route53';
import * as route53targets from 'aws-cdk-lib/aws-route53-targets';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as s3deploy from 'aws-cdk-lib/aws-s3-deployment';
import { ViewerProtocolPolicy } from 'aws-cdk-lib/aws-cloudfront';


export class WebApplicationWithCloudfrontStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    //// Defining CloudFormation input parameters
    const websiteBucketNameParam = new cdk.CfnParameter(this, "websiteBucketNameParam", {
      type: "String",
      description: "The name of the Amazon S3 bucket where to store static web application."
    });

    const hostedZoneIdParam = new cdk.CfnParameter(this, "hostedZoneIdParam", {
      type: "String",
      description: "The Route53 hosted zone id."
    });

    const domainNameParam = new cdk.CfnParameter(this, "domainNameParam", {
      type: "String",
      description: "The domainName from Route53 hosted zone."
    });

    const websitePrefixParam = new cdk.CfnParameter(this, "websitePrefixParam", {
      type: "String",
      description: "The prefix of the website. This is used in front of the domain name. ",
      default: "electronics-spa"
    });

    //// Handle the Route53 zone. If the public hosted zone is passed as parameter use it, otherwise create a new one
    let zone
    if (hostedZoneIdParam != null && hostedZoneIdParam.valueAsString.length > 0) {
      zone = route53.HostedZone.fromHostedZoneAttributes(this, 'hostedZone', {
        hostedZoneId: hostedZoneIdParam.valueAsString,
        zoneName: domainNameParam.valueAsString
      });
    } else {
      zone = new route53.PublicHostedZone(this, 'HostedZone', {
        zoneName: domainNameParam.valueAsString,
      });
    }


    // The base domain name for the web application
    const domainName = domainNameParam.valueAsString;
    // The prefix of the website.
    const websitePrefix = websitePrefixParam.valueAsString
    // The full domain name (prefix+base domain name)
    const websiteDomainName = `${websitePrefix}.${domainName}`
    
    // Create the S3 bucket that will be used to deploy the static web application
    const bucketName = websiteBucketNameParam.valueAsString
    const staticWebappBucket = new s3.Bucket(this, 'staticWebappBucket', {
      bucketName: bucketName,
      publicReadAccess: false,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      removalPolicy: RemovalPolicy.DESTROY,
      accessControl: s3.BucketAccessControl.PRIVATE,
      objectOwnership: s3.ObjectOwnership.BUCKET_OWNER_ENFORCED,
      encryption: s3.BucketEncryption.S3_MANAGED, enforceSSL: true,
    });

    //// The SSL certificate to be configured in the cloudfront distribution for the configured doamain name
    const certificate = new acm.Certificate(this, "https-certificate", {
      domainName: domainName,
      subjectAlternativeNames: [websiteDomainName],
      validation: acm.CertificateValidation.fromDns(zone),
    });

    //// CloudFront Origins
    // Create the static content origin
    const s3Prefix = "website"
    const staticResourceOrigin = new origins.S3Origin(staticWebappBucket, {
      originPath: `/${s3Prefix}`,

    });


    //// Define url paths variables for dynamic content
    const REST_BACKEND_ORIGIN_DOMAIN = "chroniclingamerica.loc.gov"
    const ROOT_BACKEND_PATH = "/search"
    // Create the dynamic content origin
    const restApiOrigin = new origins.HttpOrigin(REST_BACKEND_ORIGIN_DOMAIN, {

    });



    //// The CloudFront Distribution with default behavior for static resources
    
    const cloudfrontDistribution = new cloudfront.Distribution(this, 'CloudFrontDistribution', {
      comment: 'Web application with Amazon CloudFront',
      httpVersion: cloudfront.HttpVersion.HTTP2_AND_3,
      enableIpv6: true,
      certificate: certificate,
      domainNames: [domainName, websiteDomainName],
      errorResponses: [
        {
          httpStatus: 403,
          responseHttpStatus: 200,
          responsePagePath: '/error.html',
          ttl: Duration.minutes(30),
        },
        {
          httpStatus: 404,
          responseHttpStatus: 200,
          responsePagePath: '/error.html',
          ttl: Duration.minutes(30),
        },
      ],
      defaultRootObject: 'index.html',
      defaultBehavior: {
        //This behavior represents all the static content
        origin: staticResourceOrigin,
        allowedMethods: cloudfront.AllowedMethods.ALLOW_GET_HEAD_OPTIONS,
        cachePolicy: cloudfront.CachePolicy.CACHING_DISABLED,
        viewerProtocolPolicy: ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
        compress: true
      },
    });



    //// Configure OAC for S3 bucket and CloudFront
    const oac = new cloudfront.CfnOriginAccessControl(this, 'WebsiteOriginAccessControl', {
      originAccessControlConfig: {
        name: 'WebsiteOriginAccessControl',
        originAccessControlOriginType: 's3',
        signingBehavior: 'always',
        signingProtocol: 'sigv4'
      }
    });

    //// Configure S3 Bucket to be accessed by Cloudfront only
    const allowCloudFrontReadOnlyPolicy = new iam.PolicyStatement({
      sid: 'allowCloudFrontReadOnlyPolicy',
      actions: ['s3:GetObject'],
      principals: [new iam.ServicePrincipal('cloudfront.amazonaws.com')],
      effect: iam.Effect.ALLOW,
      conditions: {
        'StringEquals': {
          "AWS:SourceArn": "arn:aws:cloudfront::" + this.account + ":distribution/" + cloudfrontDistribution.distributionId
        }
      },
      resources: [staticWebappBucket.bucketArn, staticWebappBucket.bucketArn.concat('/').concat('*')]
    });
    staticWebappBucket.addToResourcePolicy(allowCloudFrontReadOnlyPolicy)

    //// OAC is not supported by CDK L2 construct yet. L1 construct is required
    const cfnDistribution = cloudfrontDistribution.node.defaultChild as cloudfront.CfnDistribution
    // Enable OAC
    cfnDistribution.addPropertyOverride(
      'DistributionConfig.Origins.0.OriginAccessControlId',
      oac.getAtt('Id')
    )
    // Disable OAI
    cfnDistribution.addPropertyOverride(
      'DistributionConfig.Origins.0.S3OriginConfig.OriginAccessIdentity',
      '',
    )


    //// Handle dynamic resources
    cloudfrontDistribution.addBehavior(`${ROOT_BACKEND_PATH}/*`, restApiOrigin, {
      viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
      allowedMethods: cloudfront.AllowedMethods.ALLOW_ALL,
      cachePolicy: cloudfront.CachePolicy.CACHING_DISABLED,
      originRequestPolicy: cloudfront.OriginRequestPolicy.ALL_VIEWER_EXCEPT_HOST_HEADER,

      compress: true
    });



    //// Create the Route53 DNS records for the Cloudfront distribution
    new route53.ARecord(this, 'ARecord', {
      recordName: websiteDomainName,
      target: route53.RecordTarget.fromAlias(new route53targets.CloudFrontTarget(cloudfrontDistribution)),
      zone
    });
    new route53.AaaaRecord(this, 'AaaaRecord', {
      recordName: websiteDomainName,
      target: route53.RecordTarget.fromAlias(new route53targets.CloudFrontTarget(cloudfrontDistribution)),
      zone
    });

    //// Deploy sample data
    new s3deploy.DeployTimeSubstitutedFile(this, 'DeploySampleData', {
      source: 'resources/index.html',
      destinationBucket: staticWebappBucket,
      destinationKey: `${s3Prefix}/index.html`, // optional prefix in destination bucket
      substitutions: {
        webappDomainName: websiteDomainName,
      },      
    });    

    //// CloudFormation Outputs
    new CfnOutput(this, id = "CloudFrontDistributionID", {
      value: cloudfrontDistribution.distributionId,
      description: "CloudFront distribution ID",
      exportName:"CloudFrontDistributionID",
    })    
    new CfnOutput(this, id = "CloudFrontDistributionDomainName", {
      value: cloudfrontDistribution.distributionDomainName,
      description: "CloudFront distribution Domain Name",
      exportName:"CloudFrontDistributionDomainName",
    })
    new CfnOutput(this, id = "WebApplicationDomainName", {
      value: `https://${websiteDomainName}`,
      description: "Web Application Domain Name",
      exportName:"WebApplicationDomainName",
    })    

  }
}