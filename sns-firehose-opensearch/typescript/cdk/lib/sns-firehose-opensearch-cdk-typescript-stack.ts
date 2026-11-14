import * as cdk from 'aws-cdk-lib';
import * as sns from 'aws-cdk-lib/aws-sns';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as iam from 'aws-cdk-lib/aws-iam';
import * as firehose from 'aws-cdk-lib/aws-kinesisfirehose';
import { aws_opensearchserverless as openSearch } from 'aws-cdk-lib';
import { Construct } from 'constructs';

export class SnsFirehoseOpensearchCdkTypescriptStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Change the resources' name or use parameters
    // https://docs.aws.amazon.com/cdk/v2/guide/parameters.html
    const collectionName = 'my-app-collection';
    const streamName = 'my-app-delivery-stream';
    const indexName = 'test-index';
    const topicName = 'my-app-topic';
    // user who can access the OpenSearch Dashboard
    const adminUserArn = `arn:aws:iam::${this.account}:user/admin`;

    // OpenSearch collection
    const collection = new openSearch.CfnCollection(this, 'OpenSearchCollection', {
      name: `${collectionName}`,
      type: 'SEARCH',
      description: `${collectionName}`
    });

    // Encryption policy, use AWS owned key.
    const encryptionPolicy = new openSearch.CfnSecurityPolicy(this, 'CollectionEncryptionPolicy', {
      name: `encryption-policy`,
      type: 'encryption',
      description: 'Encryption policy for test collection',
      policy: `{"Rules":[{"ResourceType":"collection","Resource":["collection/${collectionName}"]}],"AWSOwnedKey":true}`
    });

    // Security policy, allow public network access.
    // Other policies refer to https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opensearchserverless-securitypolicy.html
    const networkPolicy = new openSearch.CfnSecurityPolicy(this, 'CollectionNetworkPolicy', {
      name: `network-policy`,
      type: 'network',
      description: 'Network policy for test collection',
      policy: `[{"Rules":[{"ResourceType":"collection","Resource":["collection/${collectionName}"]}, {"ResourceType":"dashboard","Resource":["collection/${collectionName}"]}],"AllowFromPublic":true}]`
    });

    // User access policy
    const userAccessPolicy = new openSearch.CfnAccessPolicy(this, 'CollectionUserAccessPolicy', {
      name: `user-access-policy`,
      type: 'data',
      description: 'Access policy for test collection',
      policy: `[{"Description":"Access for test-user","Rules":[{"ResourceType":"index","Resource":["index/*/*"],"Permission":["aoss:*"]}, {"ResourceType":"collection","Resource":["collection/${collectionName}"],"Permission":["aoss:*"]}], "Principal":["${adminUserArn}"]}]`
    });

    collection.addDependency(encryptionPolicy);
    collection.addDependency(networkPolicy);
    collection.addDependency(userAccessPolicy);

    // S3 bucket
    const bucket = new s3.Bucket(this, 'S3Bucket');

    // Firehose delivery stream role
    // https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-serverless
    const streamRole = new iam.Role(this, 'FirehoseDeliveryStreamRole', {
      roleName: `${streamName}-role`,
      assumedBy: new iam.ServicePrincipal('firehose.amazonaws.com'),
      description: 'An IAM role for firehose delivery to OpenSearch collection',
      inlinePolicies: {
        StreamPolicy: new iam.PolicyDocument({
          statements: [
            new iam.PolicyStatement({
              effect: iam.Effect.ALLOW,
              resources: [
                bucket.bucketArn,
                `${bucket.bucketArn}/*`
              ],
              actions: [
                "s3:AbortMultipartUpload",
                "s3:GetBucketLocation",
                "s3:GetObject",
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads",
                "s3:PutObject"
              ]
            }),
            new iam.PolicyStatement({
              effect: iam.Effect.ALLOW,
              resources: ['*'],
              actions: [
                "logs:PutLogEvents"
              ]
            }),
            new iam.PolicyStatement({
              effect: iam.Effect.ALLOW,
              resources: [`*`],
              actions: [
                'aoss:APIAccessAll'
              ]
            })
          ]
        })
      }
    });

    // OpenSearch access policy for Firehose delivery stream
    const firehoseAccessPolicy = new openSearch.CfnAccessPolicy(this, 'CollectionFirehoseAccessPolicy', {
      name: 'firehose-access-policy',
      type: 'data',
      description: 'Access policy for firehose',
      policy: `[{"Description":"Access for Kinesis","Rules":[{"ResourceType":"index","Resource":["index/${collectionName}/${indexName}"],"Permission":["aoss:*"]}, {"ResourceType":"collection","Resource":["collection/${collectionName}"],"Permission":["aoss:*"]}], "Principal":["${streamRole.roleArn}"]}]`
    });

    collection.addDependency(firehoseAccessPolicy);

    // Firehose delivery stream
    const stream = new firehose.CfnDeliveryStream(this, 'FirehoseDeliveryStream', {
      deliveryStreamName: `${streamName}`,
      amazonOpenSearchServerlessDestinationConfiguration: {
        indexName: `${indexName}`,
        roleArn: streamRole.roleArn,
        s3Configuration: {
          bucketArn: bucket.bucketArn,
          roleArn: streamRole.roleArn
        },
        collectionEndpoint: collection.attrCollectionEndpoint,
        retryOptions: {
          durationInSeconds: 300
        },
        bufferingHints: {
          intervalInSeconds: 300,
          sizeInMBs: 5
        },
      }
    });

    // SNS topic and subscription
    const snsTopic = new sns.Topic(this, 'SnsTopic', {
      topicName: `${topicName}`
    });

    const subscriptionRole = new iam.Role(this, 'SnsTopicSubscriptionRole', {
      roleName: `${topicName}-subscription-role`,
      assumedBy: new iam.ServicePrincipal('sns.amazonaws.com'),
      description: 'An IAM role for SNS topic to send messages to a firehose delivery stream',
      inlinePolicies: {
        SendMessagesToFirehoseDeliveryStream: new iam.PolicyDocument({
          statements: [
            new iam.PolicyStatement({
              effect: iam.Effect.ALLOW,
              resources: [stream.attrArn],
              actions: [
                "firehose:DescribeDeliveryStream",
                "firehose:ListDeliveryStreams",
                "firehose:ListTagsForDeliveryStream",
                "firehose:PutRecord",
                "firehose:PutRecordBatch"
              ]
            })
          ]
        })
      }
    });

    new sns.Subscription(this, 'SnsTopicSubscription', {
      topic: snsTopic,
      endpoint: stream.attrArn,
      protocol: sns.SubscriptionProtocol.FIREHOSE,
      subscriptionRoleArn: subscriptionRole.roleArn
    });

    // Output resources' ARN
    new cdk.CfnOutput(this, 'snsTopicArn', {
      value: snsTopic.topicArn,
      description: 'SNS topic ARN',
      exportName: 'snsTopicArn'
    });

    new cdk.CfnOutput(this, 's3BucketArn', {
      value: bucket.bucketArn,
      description: 'Back up S3 bucket',
      exportName: 's3BucketArn'
    });

    new cdk.CfnOutput(this, 'firehoseStreamArn', {
      value: stream.attrArn,
      description: 'Firehose delivery stream ARN',
      exportName: 'firehoseStreamArn'
    });

    new cdk.CfnOutput(this, 'openSearchCollectionArn', {
      value: collection.attrArn,
      description: 'OpenSearch collection ARN',
      exportName: 'openSearchCollectionArn'
    });

    new cdk.CfnOutput(this, 'openSearchDashboardUrl', {
      value: collection.attrDashboardEndpoint,
      description: 'OpenSearch dashboard URL',
      exportName: 'openSearchDashboardUrl'
    });
  }
}
