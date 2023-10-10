import * as cdk from 'aws-cdk-lib';
import * as sns from 'aws-cdk-lib/aws-sns';
import * as subscriptions from 'aws-cdk-lib/aws-sns-subscriptions';
import * as events from 'aws-cdk-lib/aws-events';
import * as rds from 'aws-cdk-lib/aws-rds';
import * as iam from 'aws-cdk-lib/aws-iam';

import { Construct } from 'constructs';

export class RdsSnsEventNotificationCdkTsStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    // Parameters
    const snsEndpoint = new cdk.CfnParameter(this, 'SNSEndpoint', {
        type: 'String',
        description: 'Provide your email address to receive notification from SNS'
    });
    const rdsInstanceName = new cdk.CfnParameter(this, 'RDSInstanceName', {
        type: 'String',
        description: 'Provide name of your existing RDS Instance for which you want to receive event notifications'
    });
    // SNS Topic for RDS Event Subscription
    const topic = new sns.Topic(this, 'SnsForRdsEventSubscription', {
        displayName: 'rds-subscription-topic'
    });
    const awsAccountId = cdk.Fn.ref('AWS::AccountId');
    // SNS Topic Policy
    const topicPolicy = new sns.TopicPolicy(this, 'SnsTopicPolicyEventRule', {
        topics: [topic]
    });
    topicPolicy.document.addStatements(
        new iam.PolicyStatement({
            actions: [
                "SNS:GetTopicAttributes",
                "SNS:SetTopicAttributes",
                "SNS:AddPermission",
                "SNS:RemovePermission",
                "SNS:DeleteTopic",
                "SNS:Subscribe",
                "SNS:ListSubscriptionsByTopic",
                "SNS:Publish",
                "SNS:Receive"
            ],
            principals: [new iam.AccountPrincipal(awsAccountId)],
            resources: [topic.topicArn],
            conditions: {
                StringEquals: {
                    "aws:SourceOwner": awsAccountId
                }
            }
        }),
        new iam.PolicyStatement({
            effect: iam.Effect.ALLOW,
            actions: ["sns:Publish"],
            resources: [topic.topicArn],
            principals: [new iam.ServicePrincipal("events.rds.amazonaws.com")]
        })
    );
    topic.addSubscription(new subscriptions.EmailSubscription(snsEndpoint.valueAsString, { json: true }));
    // RDS Event Subscription
    new rds.CfnEventSubscription(this, 'RdsEventSubscription', {
        enabled: true,
        snsTopicArn: topic.topicArn,
        sourceIds: [rdsInstanceName.valueAsString],
        sourceType: 'db-instance',
        eventCategories: ['failure', 'low storage', 'availability']
    });
    // Outputs
    new cdk.CfnOutput(this, 'MySnsTopicName', {
        value: topic.topicName,
        description: 'SNS topic name'
    });
    new cdk.CfnOutput(this, 'RDSInstanceNames', {
        value: rdsInstanceName.valueAsString
    });
}
}