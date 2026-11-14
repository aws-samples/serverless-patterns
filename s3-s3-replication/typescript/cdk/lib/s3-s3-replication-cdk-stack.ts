import { aws_s3 as s3, aws_iam as iam, CfnOutput, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class S3S3ReplicationCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const sourceBucketName = 'my-source-bucket-' + Stack.of(this).region + '-' + Stack.of(this).account;
    const firstDestinationBucketName = 'my-destination-bucket-1-' + Stack.of(this).region + '-' + Stack.of(this).account;
    const secondDestinationBucketName = 'my-destination-bucket-2-' + Stack.of(this).region + '-' + Stack.of(this).account;

    const sourceBucket = new s3.Bucket(this, 'SourceBucket', {
      versioned: true,
      bucketName: sourceBucketName,
    });

    const firstDestinationBucket = new s3.Bucket(this, 'FirstDestinationBucket', {
      versioned: true,
      bucketName: firstDestinationBucketName,
    });

    const secondDestinationBucket = new s3.Bucket(this, 'SecondDestinationBucket', {
      versioned: true,
      bucketName: secondDestinationBucketName,
    });

    const S3Permissions = new iam.PolicyDocument({
      statements: [
        new iam.PolicyStatement({
          actions: [
            's3:ListBucket',
            's3:GetReplicationConfiguration',
            's3:GetObjectVersionForReplication',
            's3:GetObjectVersionAcl',
            's3:GetObjectVersionTagging',
            's3:GetObjectRetention',
            's3:GetObjectLegalHold'
          ],
          resources: [
            'arn:aws:s3:::'+sourceBucketName,
            'arn:aws:s3:::'+sourceBucketName+'/*',
            'arn:aws:s3:::'+firstDestinationBucketName,
            'arn:aws:s3:::'+firstDestinationBucketName+'/*',
            'arn:aws:s3:::'+secondDestinationBucketName,
            'arn:aws:s3:::'+secondDestinationBucketName+'/*',
          ],
        }),
        new iam.PolicyStatement({
          actions: [
            's3:ReplicateObject',
            's3:ReplicateDelete',
            's3:ReplicateTags',
            's3:ObjectOwnerOverrideToBucketOwner'
          ],
          resources: [
            'arn:aws:s3:::'+sourceBucketName+'/*',
            'arn:aws:s3:::'+firstDestinationBucketName+'/*',
            'arn:aws:s3:::'+secondDestinationBucketName+'/*',
          ],
        })
      ]
    });

    const replicationRole = new iam.Role(this, 'S3ReplicationRole', {
      assumedBy: new iam.ServicePrincipal('s3.amazonaws.com'),
      inlinePolicies: {
        S3Permissions: S3Permissions
      }
    });

    const cfnBucket = sourceBucket.node.defaultChild as s3.CfnBucket;
    cfnBucket.replicationConfiguration = {
      role: replicationRole.roleArn,
      rules: [
        {
          destination: {
            bucket: firstDestinationBucket.bucketArn,
          },
          priority: 1,
          filter: {
            prefix: 'images/',
          },
          deleteMarkerReplication: {
            status: 'Enabled',
          },
          status: 'Enabled',
        },
        {
          destination: {
            bucket: secondDestinationBucket.bucketArn,
          },
          priority: 2,
          filter: {
            prefix: 'data/',
          },
          deleteMarkerReplication: {
            status: 'Enabled',
          },
          status: 'Enabled',
        }
      ]
    }

    // Output
    new CfnOutput(this, 'sourceBucket', {
      value: sourceBucket.bucketName,
      description: 'Source Bucket Name',
      exportName: 'sourceBucketName',
    });
    new CfnOutput(this, 'firstDestinationBucket', {
      value: firstDestinationBucket.bucketName,
      description: 'First Destination Bucket Name',
      exportName: 'firstDestinationBucketName',
    });
    new CfnOutput(this, 'secondDestinationBucket', {
      value: secondDestinationBucket.bucketName,
      description: 'Second Destination Bucket Name',
      exportName: 'secondDestinationBucketName',
    });
  }
}
