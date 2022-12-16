import { Stack, StackProps } from 'aws-cdk-lib';
import { S3UploadPresignedUrlApi } from 'cdk-s3-upload-presignedurl-api';
import { Construct } from 'constructs';

export class S3UploadPresignedURLAPIStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const uploadS3API = new S3UploadPresignedUrlApi(this, 'API');
  }
}
