import { CfnOutput, Construct, RemovalPolicy, Stack, StackProps} from '@aws-cdk/core';
import { BlockPublicAccess, Bucket, BucketEncryption, } from '@aws-cdk/aws-s3';

export class S3CdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const BUCKET_NAME = 'demo-bucket-serverless-patterns'

    var bucket = new Bucket(this, 'demoBucket', {
      blockPublicAccess: BlockPublicAccess.BLOCK_ALL,
      bucketName: BUCKET_NAME,
      enforceSSL: true,
      publicReadAccess: false,
      removalPolicy: RemovalPolicy.DESTROY,
      versioned: false,
      autoDeleteObjects: true
    });

    new CfnOutput(this, BUCKET_NAME, {
      value: bucket.bucketName,
      description: 'The name of the s3 bucket',
    });
  }
}