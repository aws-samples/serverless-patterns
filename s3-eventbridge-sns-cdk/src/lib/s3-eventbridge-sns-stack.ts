import { RemovalPolicy, CfnOutput, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as events from 'aws-cdk-lib/aws-events';
import { Topic } from 'aws-cdk-lib/aws-sns';
import { SnsTopic } from 'aws-cdk-lib/aws-events-targets';

export class S3EventbridgeSnsStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

   //Create S3 bucket
    const bucket = new s3.Bucket(this, 'sample-s3eventbridgesns-bucket', {
      eventBridgeEnabled: true,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      removalPolicy: RemovalPolicy.DESTROY
    });

    //Create SNS Topic
    const mySnsTopic = new Topic(this, 'my-sns-topic');
    
    //Create EventBridge Rule
    const rule = new events.Rule(this, 'rule', {
      eventPattern: {
        source: ['aws.s3'],
        detailType: [
          'Object Created'
        ],
        detail: {
          bucket: {
            name: [
              bucket.bucketName
            ]
          }
        }
      },
    });

    //Add SNS Topic as target to EventBridge Rule
    rule.addTarget(new SnsTopic(mySnsTopic));

    new CfnOutput(this, 'S3BucketName', { value: bucket.bucketName });
    new CfnOutput(this, 'SnsTopicARN', { value: mySnsTopic.topicArn });
    new CfnOutput(this, 'EventBridgeRuleARN', { value: rule.ruleArn });
  }
}