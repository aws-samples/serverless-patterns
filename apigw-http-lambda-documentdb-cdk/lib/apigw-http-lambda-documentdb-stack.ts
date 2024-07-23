import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as apigw from '@aws-cdk/aws-apigatewayv2-alpha'
import * as docdb from 'aws-cdk-lib/aws-docdb';
import { NodejsFunction } from 'aws-cdk-lib/aws-lambda-nodejs';
import { Runtime } from 'aws-cdk-lib/aws-lambda';
import * as path from 'path';
import { HttpLambdaIntegration } from '@aws-cdk/aws-apigatewayv2-integrations-alpha';

// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class ApiGwHttpLambdaDocumentDbStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const documentDbSecretName = 'documentDbSecretName';

    // Create VPC with public and private subnets
    const vpc = new ec2.Vpc(this, 'VPC-serverless-pattern', {
      ipAddresses: ec2.IpAddresses.cidr('10.0.0.0/16'),
      maxAzs: 2,
      subnetConfiguration: [
        { cidrMask: 24, name: 'PublicSubnet', subnetType: ec2.SubnetType.PUBLIC },
        { cidrMask: 24, name: 'PrivateSubnet', subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS },
      ],
      natGateways: 1
    });

    // Create API Gateway 
    const httpApi = new apigw.HttpApi(this, 'HttpApiGateway', {
      apiName: 'ApiGatewqyToLambda',
      description: 'Integration between API Gateway HTTP and the Lambda function',
    });

    // create Document DB in the private Subnet of the VPC
    const docDbcluster = new docdb.DatabaseCluster(this, 'Database', {
      masterUser: {
        username: 'myuser', // NOTE: 'admin' is reserved by DocumentDB
        excludeCharacters: "\"@/:", // optional, defaults to the set "\"@/" and is also used for eventually created rotations
        secretName: documentDbSecretName, // optional, if you prefer to specify the secret name
      },
      instanceType: ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.MEDIUM),
      vpcSubnets: {
        subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
      },
      vpc: vpc
    });

    // allow Document DB access from the VPC
    docDbcluster.connections.allowFrom(ec2.Peer.ipv4(vpc.vpcCidrBlock), ec2.Port.tcp(27017));
    
    
    // destroy Document DB cluster when stack is destroye - remove for production use
    docDbcluster.applyRemovalPolicy(cdk.RemovalPolicy.DESTROY);

    //AWS Secrets Manager secret for the DocumentDb 
    const dbSecret = docDbcluster.secret!;

    // Lambda function which is conncted to the DocumentDb
    const LambdaToDocumentDB = new NodejsFunction(this, 'LambdaToDocumentDB', {
      runtime: Runtime.NODEJS_18_X,
      handler: 'handler',
      timeout: cdk.Duration.seconds(300),
      entry: path.join(__dirname, '../lambda/app.ts'),
      environment: {
        DOCUMENTDB_SECRET_NAME: documentDbSecretName,
      },
      vpc: vpc, //Lambda needs to be in the VPC which has a route to the DocumentDB database
      vpcSubnets: {
        subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
      },      
      bundling: {
        commandHooks: {
          afterBundling: (inputDir: string, outputDir: string): string[] => [
            `cp ${inputDir}/lambda/global-bundle.pem ${outputDir}`,
          ],
          beforeBundling: (inputDir: string, outputDir: string): string[] => [],
          beforeInstall: (inputDir: string, outputDir: string): string[] => [],
        },
      },      
    });

    // Grant Lambda function access to AWS Secrets Manager secret
    LambdaToDocumentDB.addToRolePolicy(new cdk.aws_iam.PolicyStatement({
      actions: ['secretsmanager:GetSecretValue'],
      resources: [dbSecret.secretFullArn!],
      effect: cdk.aws_iam.Effect.ALLOW
    }));

    // Create an integration between the API Gateway and the Lambda function
    const lambdaIntegration = new HttpLambdaIntegration('MetaDataLinks', LambdaToDocumentDB);

    //create a default route to the LambdaFunction
    httpApi.addRoutes({
      path: '/',
      methods: [apigw.HttpMethod.ANY],
      integration: lambdaIntegration,
    });

   //output the url of the api gateway
   new cdk.CfnOutput(this, 'ApiGatewayUrl', {
    value: httpApi.apiEndpoint,
    description: 'The URL of the ApiGateway ',
    exportName: 'ApiGatewayUrl',
  });

  }
}
