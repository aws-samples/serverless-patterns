import { App, Duration, Stack, StackProps, CfnOutput } from 'aws-cdk-lib';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as events from 'aws-cdk-lib/aws-events';
import * as targets from 'aws-cdk-lib/aws-events-targets';
import * as ec2 from 'aws-cdk-lib/aws-ec2';
import * as ecs from 'aws-cdk-lib/aws-ecs';
import * as iam from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';
import { AdjustmentType } from 'aws-cdk-lib/aws-autoscaling';

export class EbSqsEcsStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);
    //Create Queue
    const queue = new sqs.Queue(this, 'EbSqsEcsQueue', {
      visibilityTimeout: Duration.seconds(300)
    });
    
    //Create Event bus and rule
    var custom_bus = new events.EventBus(this, "bus", {
      "eventBusName": "test-bus-cdk"
    });
    const rule = new events.Rule(this, "rule", {
      "eventBus": custom_bus
    });
    rule.addEventPattern({
      "source": ["eb-sqs-ecs"],
      "detailType": ["message-for-queue"]
    });
    rule.addTarget(new targets.SqsQueue(queue));
    new CfnOutput(this, "QueueURL", {
      "description": "URL of SQS Queue",
      "value": queue.queueUrl
    });
    
    //Create ECS cluster
    const natGatewayProvider = ec2.NatProvider.instance({
      instanceType: new ec2.InstanceType("t3.nano"),
    });

    const vpc = new ec2.Vpc(this, "FargateVPC", {
      natGatewayProvider,
      natGateways: 1,
    });

    const cluster = new ecs.Cluster(this, "Cluster", { vpc });
    //End- Create ECS cluster
    
    // Create a task role that will be used within the container
    const EcsTaskRole = new iam.Role(this, "EcsTaskRole", {
      assumedBy: new iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
    });

    EcsTaskRole.attachInlinePolicy(
      new iam.Policy(this, "SQSAdminAccess", {
        statements: [
          new iam.PolicyStatement({
            actions: ["sqs:*"],
            effect: iam.Effect.ALLOW,
            resources: [queue.queueArn],
          }),
        ],
      })
    );    

    // Create task definition
    const fargateTaskDefinition = new ecs.FargateTaskDefinition(
      this,
      "FargateTaskDef",
      {
        memoryLimitMiB: 4096,
        cpu: 2048,
        taskRole: EcsTaskRole
      }
    );

    // create a task definition with CloudWatch Logs
    const logging = new ecs.AwsLogDriver({
      streamPrefix: "myapplication",
    });

    // Create container from local `Dockerfile`
    const appContainer = fargateTaskDefinition.addContainer("Container", {
      image: ecs.ContainerImage.fromAsset("./python-app"), 
      environment: {
          queueUrl: queue.queueUrl,
          region: process.env.CDK_DEFAULT_REGION!,
        },
      logging,
    });

    // Create service
    const service = new ecs.FargateService(this, "Service", {
      cluster,
      taskDefinition: fargateTaskDefinition,
      desiredCount: 0,
    });
    
    // Configure task auto-scaling
    const scaling = service.autoScaleTaskCount({
      minCapacity: 0,
      maxCapacity: 1,
    });

    // Setup scaling metric and cooldown period
    scaling.scaleOnMetric("QueueMessagesVisibleScaling", {
      metric: queue.metricApproximateNumberOfMessagesVisible(),
      adjustmentType: AdjustmentType.CHANGE_IN_CAPACITY,
      cooldown: Duration.seconds(300),
      scalingSteps: [
        { upper: 0, change: -1 },
        { lower: 1, change: +1 },
      ],
    });
    

    
    
  }
}
