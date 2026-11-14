/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */
import { Stack, StackProps, Duration, CfnOutput } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { aws_iam as iam } from 'aws-cdk-lib';
import { aws_lambda as lambda } from 'aws-cdk-lib';
import * as msk from '@aws-cdk/aws-msk-alpha';
import { aws_ec2 as ec2 } from 'aws-cdk-lib';
import { NodejsFunction } from "aws-cdk-lib/aws-lambda-nodejs";
import { Runtime } from "aws-cdk-lib/aws-lambda";
import { ManagedKafkaEventSource } from "aws-cdk-lib/aws-lambda-event-sources";

// The cluster has no client authentication and accepts TLS connections on this port.
const BROKER_TLS_PORT = 9094;
const KAFKA_CLIENT_VERSION = '4.1.2';

export class MskLambdaCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    let topicName: string;
    topicName = "transactions";

    const vpc = new ec2.Vpc(this, 'Vpc', {
      maxAzs: 2
    });

    // The brokers accept traffic only from this security group itself (used by the
    // Lambda event source mapping) and from the Kafka client instance.
    const brokerSecurityGroup = new ec2.SecurityGroup(this, 'BrokerSecurityGroup', {
      vpc,
      description: 'MSK brokers',
    });

    const cluster = new msk.Cluster(this, "Cluster", {
      clusterName: `${this.stackName}-cluster`,
      kafkaVersion: msk.KafkaVersion.V4_1_X_KRAFT,
      vpc: vpc,
      securityGroups: [brokerSecurityGroup],
      ebsStorageInfo: {
        volumeSize: 50,
      },
    })

    // The Lambda event source mapping connects to the brokers through the cluster's
    // security group, so the group must allow traffic from itself.
    brokerSecurityGroup.addIngressRule(brokerSecurityGroup, ec2.Port.tcp(BROKER_TLS_PORT),
      'Lambda event source mapping to brokers (TLS)');

    let transactionHandler = new NodejsFunction(this, "TransactionHandler", {
      runtime: Runtime.NODEJS_24_X,
      entry: 'lambda/transaction-handler.js',
      handler: 'handler',
      vpc: vpc,
      timeout: Duration.minutes(1),
    });

    // Allow lambda to interact with MSK
    transactionHandler.role?.addManagedPolicy(
      iam.ManagedPolicy.fromAwsManagedPolicyName(
        'service-role/AWSLambdaMSKExecutionRole',
      ),
    );

    transactionHandler.addEventSource(new ManagedKafkaEventSource({
      clusterArn: cluster.clusterArn,
      topic: topicName,
      batchSize: 100, // default
      startingPosition: lambda.StartingPosition.LATEST
    }));

    // Kafka client instance in a private subnet. Connect with Session Manager; there is no SSH.
    const clientSecurityGroup = new ec2.SecurityGroup(this, 'KafkaClientSecurityGroup', {
      vpc,
      description: 'Kafka client instance (no inbound rules; connect with Session Manager)',
    });
    brokerSecurityGroup.addIngressRule(clientSecurityGroup, ec2.Port.tcp(BROKER_TLS_PORT),
      'Kafka client instance to brokers (TLS)');

    const clientRole = new iam.Role(this, 'KafkaClientRole', {
      assumedBy: new iam.ServicePrincipal('ec2.amazonaws.com'),
      managedPolicies: [
        iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonSSMManagedInstanceCore'),
      ],
    });
    clientRole.addToPolicy(new iam.PolicyStatement({
      actions: ['kafka:DescribeClusterV2', 'kafka:GetBootstrapBrokers'],
      resources: [cluster.clusterArn],
    }));

    const userData = ec2.UserData.forLinux();
    userData.addCommands(
      'dnf install -y java-21-amazon-corretto-headless',
      'cd /home/ec2-user',
      `curl -sSfL -o kafka.tgz https://archive.apache.org/dist/kafka/${KAFKA_CLIENT_VERSION}/kafka_2.13-${KAFKA_CLIENT_VERSION}.tgz`,
      'tar -xzf kafka.tgz && rm kafka.tgz',
      `ln -s kafka_2.13-${KAFKA_CLIENT_VERSION} kafka`,
      'printf "security.protocol=SSL\\n" > kafka/client.properties',
      `echo "export CLUSTER_ARN=${cluster.clusterArn}" >> /home/ec2-user/.bashrc`,
      `echo "export AWS_REGION=${this.region}" >> /home/ec2-user/.bashrc`,
      `echo "export TOPIC=${topicName}" >> /home/ec2-user/.bashrc`,
      'chown -R ec2-user:ec2-user /home/ec2-user',
    );

    const clientInstance = new ec2.Instance(this, 'KafkaClientInstance', {
      vpc,
      vpcSubnets: { subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS },
      instanceType: ec2.InstanceType.of(ec2.InstanceClass.T3, ec2.InstanceSize.SMALL),
      machineImage: ec2.MachineImage.latestAmazonLinux2023(),
      securityGroup: clientSecurityGroup,
      role: clientRole,
      userData,
      requireImdsv2: true,
    });

    new CfnOutput(this, 'KafkaClientInstanceId', { value: clientInstance.instanceId });
    new CfnOutput(this, 'ClusterArn', { value: cluster.clusterArn });
    new CfnOutput(this, 'TransactionHandlerName', { value: transactionHandler.functionName });
  }
}
