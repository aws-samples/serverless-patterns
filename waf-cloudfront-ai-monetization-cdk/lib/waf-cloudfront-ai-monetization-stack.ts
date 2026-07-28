import * as cdk from 'aws-cdk-lib';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as cloudfront from 'aws-cdk-lib/aws-cloudfront';
import * as origins from 'aws-cdk-lib/aws-cloudfront-origins';
import * as wafv2 from 'aws-cdk-lib/aws-wafv2';
import { Construct } from 'constructs';

export class WafCloudfrontAiMonetizationStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Amazon S3 bucket for sample content
    const contentBucket = new s3.Bucket(this, 'ContentBucket', {
      removalPolicy: cdk.RemovalPolicy.DESTROY,
      autoDeleteObjects: true,
    });

    // WAF WebACL with Bot Control and AI Traffic Monetization
    const webAcl = new wafv2.CfnWebACL(this, 'AiMonetizationWebAcl', {
      defaultAction: { allow: {} },
      scope: 'CLOUDFRONT',
      visibilityConfig: {
        cloudWatchMetricsEnabled: true,
        metricName: 'AiMonetizationWebAcl',
        sampledRequestsEnabled: true,
      },
      rules: [
        {
          name: 'AWSManagedRulesBotControlRuleSet',
          priority: 0,
          overrideAction: { count: {} },
          statement: {
            managedRuleGroupStatement: {
              vendorName: 'AWS',
              name: 'AWSManagedRulesBotControlRuleSet',
              managedRuleGroupConfigs: [
                {
                  awsManagedRulesBotControlRuleSet: {
                    inspectionLevel: 'TARGETED',
                    enableMachineLearning: true,
                  },
                },
              ],
            },
          },
          visibilityConfig: {
            cloudWatchMetricsEnabled: true,
            metricName: 'BotControlRuleSet',
            sampledRequestsEnabled: true,
          },
        },
        {
          name: 'MonetizeAiBots',
          priority: 1,
          action: { count: {} }, // Placeholder — overridden below
          statement: {
            labelMatchStatement: {
              scope: 'LABEL',
              key: 'awswaf:managed:aws:bot-control:bot:category:ai',
            },
          },
          visibilityConfig: {
            cloudWatchMetricsEnabled: true,
            metricName: 'MonetizeAiBots',
            sampledRequestsEnabled: true,
          },
        },
      ],
    });

    // Override the MonetizeAiBots rule action with Monetize (not yet in CDK types)
    webAcl.addPropertyDeletionOverride('Rules.1.Action.Count');
    webAcl.addPropertyOverride('Rules.1.Action.Monetize', {
      PriceMultiplier: 10,
    });

    // Add MonetizationConfig to the WebACL (not yet in CDK types)
    // Using TEST mode with Base Sepolia testnet — no real money involved
    webAcl.addPropertyOverride('MonetizationConfig', {
      CurrencyMode: 'TEST',
      CryptoConfig: {
        PaymentNetworks: [
          {
            Chain: 'BASE_SEPOLIA',
            WalletAddress: '0x0000000000000000000000000000000000000000', // Replace with your testnet wallet
            Prices: [
              {
                Amount: '0.001',
                Currency: 'USDC',
              },
            ],
          },
        ],
      },
    });

    // CloudFront distribution with WAF protection
    const distribution = new cloudfront.Distribution(this, 'Distribution', {
      defaultBehavior: {
        origin: origins.S3BucketOrigin.withOriginAccessControl(contentBucket),
        viewerProtocolPolicy: cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
      },
      webAclId: webAcl.attrArn,
    });

    // Outputs
    new cdk.CfnOutput(this, 'DistributionDomainName', {
      value: distribution.distributionDomainName,
      description: 'Amazon CloudFront distribution domain name',
    });

    new cdk.CfnOutput(this, 'ContentBucketName', {
      value: contentBucket.bucketName,
      description: 'Amazon S3 bucket for sample content',
    });

    new cdk.CfnOutput(this, 'WebAclArn', {
      value: webAcl.attrArn,
      description: 'AWS WAF WebACL ARN',
    });
  }
}
