import { Aws, Duration, RemovalPolicy, Stack, StackProps, CfnParameter, CfnOutput } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as s3n from 'aws-cdk-lib/aws-s3-notifications'
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as iam from 'aws-cdk-lib/aws-iam'
import { Effect } from 'aws-cdk-lib/aws-iam';
import { BillingMode } from 'aws-cdk-lib/aws-dynamodb';

export class S3LambdaDynamodbCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    
    const dataObjectParam = new CfnParameter(this, 'dataObject', {
      type: 'String',
      description : 'Enter the name of the data object (For Example: product, customer, or order)',
      default: this.node.tryGetContext('dataObjectParam') ? this.node.tryGetContext('dataObjectParam') : 'object'
    });

    const bucket = new s3.Bucket(this, 's3-lambda-ddb-cdk', {
      removalPolicy: RemovalPolicy.DESTROY
    });
    const table = new dynamodb.Table(this, 'objects',{
      tableName: dataObjectParam.valueAsString,
      partitionKey: { name: 'id', type: dynamodb.AttributeType.STRING },
      billingMode: BillingMode.PAY_PER_REQUEST,
      removalPolicy: RemovalPolicy.DESTROY
    });
    const lambdaRole = new iam.Role(this, 'dataloadFnRole', {
      assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com')
    });
    const lambdaRolePolicy = lambdaRole.assumeRolePolicy;
    lambdaRolePolicy?.addStatements(new iam.PolicyStatement({
      principals: [new iam.ServicePrincipal('s3.amazonaws.com')],
      actions: ['sts:AssumeRole']
    }));
    lambdaRole.addManagedPolicy(iam.ManagedPolicy.fromManagedPolicyArn(this, "AWSLambdaBasicExecutionRole", 'arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'));
    lambdaRole.addManagedPolicy(iam.ManagedPolicy.fromManagedPolicyArn(this, "AmazonS3ReadOnlyAccess", 'arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'));
    lambdaRole.addManagedPolicy(iam.ManagedPolicy.fromManagedPolicyArn(this, "AWSLambdaInvocation-DynamoDB", 'arn:aws:iam::aws:policy/AWSLambdaInvocation-DynamoDB'));
    lambdaRole.addToPolicy(new iam.PolicyStatement({
      actions: [
        "dynamodb:PutItem",
        "dynamodb:BatchWriteItem"
      ],
      resources: ["*"],
      effect: Effect.ALLOW
    }));
    const lambdaFunction = new lambda.Function(this, 'dataload', {
      runtime: lambda.Runtime.PYTHON_3_7,
      handler: 'data-load.handler',
      code: lambda.Code.fromAsset('code'),
      role: lambdaRole,
      environment: {
        bucket: bucket.bucketName,
        key: dataObjectParam.valueAsString + '.csv',
        table: table.tableName
      },
      timeout: Duration.minutes(5)
    });
    lambdaFunction.grantInvoke(new iam.ServicePrincipal('s3.amazonaws.com').withConditions({
      ArnLike: {
        'aws:SourceArn': bucket.bucketArn,
      },
      StringEquals: {
        'aws:SourceAccount': Aws.ACCOUNT_ID,
      }
    }));
    bucket.addEventNotification(s3.EventType.OBJECT_CREATED, new s3n.LambdaDestination(lambdaFunction), {prefix: dataObjectParam.valueAsString + '.csv'});

    new CfnOutput(this, 'Bucket Name', { value: bucket.bucketName });
  }
}
