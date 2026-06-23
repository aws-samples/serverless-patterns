import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam';

export class LambdaDsqlMultiRegionStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Amazon Aurora DSQL cluster — serverless PostgreSQL with no VPC, no passwords
    const cluster = new cdk.CfnResource(this, 'DsqlCluster', {
      type: 'AWS::DSQL::Cluster',
      properties: {
        DeletionProtectionEnabled: false,
        Tags: [{ Key: 'Pattern', Value: 'lambda-dsql-multi-region-cdk' }],
      },
    });

    const clusterEndpoint = cluster.getAtt('Endpoint').toString();
    const clusterArn = cluster.getAtt('ResourceArn').toString();

    // AWS Lambda function for Amazon Aurora DSQL connectivity
    const fn = new lambda.Function(this, 'DsqlFunction', {
      runtime: lambda.Runtime.PYTHON_3_12,
      handler: 'index.handler',
      code: lambda.Code.fromAsset('src/handler', {
        bundling: {
          image: lambda.Runtime.PYTHON_3_12.bundlingImage,
          command: [
            'bash', '-c',
            'pip install psycopg2-binary -t /asset-output && cp -au . /asset-output',
          ],
        },
      }),
      timeout: cdk.Duration.seconds(30),
      environment: {
        CLUSTER_ENDPOINT: clusterEndpoint,
        CLUSTER_REGION: this.region,
      },
    });

    // Grant the AWS Lambda function permission to generate Amazon Aurora DSQL IAM auth tokens
    fn.addToRolePolicy(new iam.PolicyStatement({
      actions: ['dsql:DbConnect', 'dsql:DbConnectAdmin'],
      resources: [clusterArn],
    }));

    // Outputs
    new cdk.CfnOutput(this, 'ClusterEndpoint', {
      value: clusterEndpoint,
      description: 'Amazon Aurora DSQL cluster endpoint',
    });
    new cdk.CfnOutput(this, 'ClusterArn', {
      value: clusterArn,
      description: 'Amazon Aurora DSQL cluster ARN (use with MultiRegionProperties.Clusters to link regions)',
    });
    new cdk.CfnOutput(this, 'FunctionName', {
      value: fn.functionName,
      description: 'AWS Lambda function name',
    });
  }
}
