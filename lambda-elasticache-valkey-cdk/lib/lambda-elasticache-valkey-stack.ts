import * as cdk from 'aws-cdk-lib';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as elasticache from 'aws-cdk-lib/aws-elasticache';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import { Construct } from 'constructs';

export class LambdaElasticacheValkeyStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const vpc = ec2.Vpc.fromLookup(this, 'Vpc', { isDefault: true });

    const sg = new ec2.SecurityGroup(this, 'ValkeySG', { vpc, allowAllOutbound: true });
    sg.addIngressRule(sg, ec2.Port.tcp(6379), 'Allow Valkey access from Lambda');

    // ElastiCache Serverless with Valkey engine (requires 2-3 subnets)
    const subnets = vpc.publicSubnets.slice(0, 2);
    const cache = new elasticache.CfnServerlessCache(this, 'ValkeyCache', {
      serverlessCacheName: 'valkey-session-store',
      engine: 'valkey',
      majorEngineVersion: '8',
      securityGroupIds: [sg.securityGroupId],
      subnetIds: subnets.map(s => s.subnetId)
    });

    const fn = new lambda.Function(this, 'CacheFn', {
      runtime: lambda.Runtime.NODEJS_22_X,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('src'),
      vpc,
      securityGroups: [sg],
      allowPublicSubnet: true,
      environment: { CACHE_ENDPOINT: cache.attrEndpointAddress, CACHE_PORT: cache.attrEndpointPort },
      timeout: cdk.Duration.seconds(15)
    });

    const fnUrl = fn.addFunctionUrl({ authType: lambda.FunctionUrlAuthType.AWS_IAM });

    new cdk.CfnOutput(this, 'FunctionUrl', { value: fnUrl.url });
    new cdk.CfnOutput(this, 'CacheEndpoint', { value: cache.attrEndpointAddress });
  }
}
