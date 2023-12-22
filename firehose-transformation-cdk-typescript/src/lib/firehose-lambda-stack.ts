import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import {
  aws_iam as iam,
  aws_s3 as s3,
  aws_kinesisfirehose as firehose,
  aws_lambda_nodejs as lambda,
  aws_lambda as lambda_,
} from 'aws-cdk-lib';


export class FirehoseLambdaStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
   
    const lambda_role = new iam.Role(this, 'firehose-lambda-role', {
      assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com')
    });

    lambda_role.addManagedPolicy(
      iam.ManagedPolicy.fromAwsManagedPolicyName(
        "service-role/AWSLambdaBasicExecutionRole"
      )
    );

    lambda_role.addToPolicy(
        new iam.PolicyStatement({
          resources: ['*'],
          actions: [
            "firehose:DescribeDeliveryStream",
            "firehose:PutRecord",
            "firehose:StartDeliveryStreamEncryption",
            "firehose:PutRecordBatch",
            "firehose:ListDeliveryStreams"
          ],
          effect: iam.Effect.ALLOW
        })
    );
    
    const lambdaFn = new lambda.NodejsFunction(this, 'firehose-lambda-function', {
      entry: 'lambda/index.ts',
      handler: 'handler',
      runtime: lambda_.Runtime.NODEJS_18_X,
      architecture: lambda_.Architecture.X86_64,
      role: lambda_role,
      timeout: cdk.Duration.seconds(60)
      });
    

    const bucket = new s3.Bucket(this, 'firehost-destination-bucket', {
      encryption: s3.BucketEncryption.S3_MANAGED,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL
    });

    const firehose_role = new iam.Role(this, 'firehose-role', {
      assumedBy: new iam.ServicePrincipal('firehose.amazonaws.com')
    });

    firehose_role.addToPolicy(
      new iam.PolicyStatement({
        resources: [bucket.bucketArn, bucket.bucketArn + '/*'],
        actions: ['s3:AbortMultipartUpload', 's3:GetBucketLocation', 's3:GetObject', 's3:ListBucket', 's3:ListBucketMultipartUploads', 's3:PutObject'],
        effect: iam.Effect.ALLOW
      })
    );

    firehose_role.addToPolicy(
      new iam.PolicyStatement({
        resources: [lambdaFn.functionArn],
        actions: ['lambda:InvokeFunction', 'lambda:GetFunctionConfiguration'],
        effect: iam.Effect.ALLOW
      })
    );
    firehose_role.addToPolicy( 
      new iam.PolicyStatement({
        resources: ['*'],
        actions: ['logs:*'],
        effect: iam.Effect.ALLOW
      })
    );
       
    const firehose_delivery_stream = new firehose.CfnDeliveryStream(this, 'firehose-stream', {
      deliveryStreamType: 'DirectPut',
      extendedS3DestinationConfiguration: {
        bucketArn: bucket.bucketArn,
        bufferingHints: {
          intervalInSeconds: 60,
          sizeInMBs: 1
        },
        roleArn: firehose_role.roleArn,
        processingConfiguration: {
          enabled: true,
          processors: [{
            type: 'Lambda',
            parameters: [{
              parameterName: 'LambdaArn',
              parameterValue: lambdaFn.functionArn
            }]
          }]
        },
        encryptionConfiguration: {
          noEncryptionConfig: 'NoEncryption'
        }
      }
    }
    );


    new cdk.CfnOutput(this, "S3 Destination Bucket", {
      value: bucket.bucketName,
      description: "S3 Destination Bucket"
    });

  }
}
