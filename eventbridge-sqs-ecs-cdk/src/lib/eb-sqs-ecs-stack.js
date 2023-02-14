"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.EbSqsEcsStack = void 0;
const aws_cdk_lib_1 = require("aws-cdk-lib");
const sqs = require("aws-cdk-lib/aws-sqs");
const events = require("aws-cdk-lib/aws-events");
const targets = require("aws-cdk-lib/aws-events-targets");
const ec2 = require("aws-cdk-lib/aws-ec2");
const ecs = require("aws-cdk-lib/aws-ecs");
const iam = require("aws-cdk-lib/aws-iam");
const aws_autoscaling_1 = require("aws-cdk-lib/aws-autoscaling");
class EbSqsEcsStack extends aws_cdk_lib_1.Stack {
    constructor(scope, id, props) {
        super(scope, id, props);
        //Create Queue
        const queue = new sqs.Queue(this, 'EbSqsEcsQueue', {
            visibilityTimeout: aws_cdk_lib_1.Duration.seconds(300)
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
        new aws_cdk_lib_1.CfnOutput(this, "QueueURL", {
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
        EcsTaskRole.attachInlinePolicy(new iam.Policy(this, "SQSAdminAccess", {
            statements: [
                new iam.PolicyStatement({
                    actions: ["sqs:*"],
                    effect: iam.Effect.ALLOW,
                    resources: [queue.queueArn],
                }),
            ],
        }));
        // Create task definition
        const fargateTaskDefinition = new ecs.FargateTaskDefinition(this, "FargateTaskDef", {
            memoryLimitMiB: 4096,
            cpu: 2048,
            taskRole: EcsTaskRole
        });
        // create a task definition with CloudWatch Logs
        const logging = new ecs.AwsLogDriver({
            streamPrefix: "myapplication",
        });
        // Create container from local `Dockerfile`
        const appContainer = fargateTaskDefinition.addContainer("Container", {
            image: ecs.ContainerImage.fromAsset("./python-app"),
            environment: {
                queueUrl: queue.queueUrl,
                region: process.env.CDK_DEFAULT_REGION,
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
            adjustmentType: aws_autoscaling_1.AdjustmentType.CHANGE_IN_CAPACITY,
            cooldown: aws_cdk_lib_1.Duration.seconds(300),
            scalingSteps: [
                { upper: 0, change: -1 },
                { lower: 1, change: +1 },
            ],
        });
    }
}
exports.EbSqsEcsStack = EbSqsEcsStack;
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiZWItc3FzLWVjcy1zdGFjay5qcyIsInNvdXJjZVJvb3QiOiIiLCJzb3VyY2VzIjpbImViLXNxcy1lY3Mtc3RhY2sudHMiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6Ijs7O0FBQUEsNkNBQTBFO0FBQzFFLDJDQUEyQztBQUMzQyxpREFBaUQ7QUFDakQsMERBQTBEO0FBQzFELDJDQUEyQztBQUMzQywyQ0FBMkM7QUFDM0MsMkNBQTJDO0FBRTNDLGlFQUE2RDtBQUU3RCxNQUFhLGFBQWMsU0FBUSxtQkFBSztJQUN0QyxZQUFZLEtBQWdCLEVBQUUsRUFBVSxFQUFFLEtBQWtCO1FBQzFELEtBQUssQ0FBQyxLQUFLLEVBQUUsRUFBRSxFQUFFLEtBQUssQ0FBQyxDQUFDO1FBQ3hCLGNBQWM7UUFDZCxNQUFNLEtBQUssR0FBRyxJQUFJLEdBQUcsQ0FBQyxLQUFLLENBQUMsSUFBSSxFQUFFLGVBQWUsRUFBRTtZQUNqRCxpQkFBaUIsRUFBRSxzQkFBUSxDQUFDLE9BQU8sQ0FBQyxHQUFHLENBQUM7U0FDekMsQ0FBQyxDQUFDO1FBRUgsMkJBQTJCO1FBQzNCLElBQUksVUFBVSxHQUFHLElBQUksTUFBTSxDQUFDLFFBQVEsQ0FBQyxJQUFJLEVBQUUsS0FBSyxFQUFFO1lBQ2hELGNBQWMsRUFBRSxjQUFjO1NBQy9CLENBQUMsQ0FBQztRQUNILE1BQU0sSUFBSSxHQUFHLElBQUksTUFBTSxDQUFDLElBQUksQ0FBQyxJQUFJLEVBQUUsTUFBTSxFQUFFO1lBQ3pDLFVBQVUsRUFBRSxVQUFVO1NBQ3ZCLENBQUMsQ0FBQztRQUNILElBQUksQ0FBQyxlQUFlLENBQUM7WUFDbkIsUUFBUSxFQUFFLENBQUMsWUFBWSxDQUFDO1lBQ3hCLFlBQVksRUFBRSxDQUFDLG1CQUFtQixDQUFDO1NBQ3BDLENBQUMsQ0FBQztRQUNILElBQUksQ0FBQyxTQUFTLENBQUMsSUFBSSxPQUFPLENBQUMsUUFBUSxDQUFDLEtBQUssQ0FBQyxDQUFDLENBQUM7UUFDNUMsSUFBSSx1QkFBUyxDQUFDLElBQUksRUFB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O2dCQUNaLEVBQUUsS0FBSyxFQUFFLENBQUMsRUFBRSxNQUFNLEVBQUUsQ0FBQyxDQUFDLEVBQUU7Z0JBQ3hCLEVBQUUsS0FBSyxFQUFFLENBQUMsRUFBRSxNQUFNLEVBQUUsQ0FBQyxDQUFDLEVBQUU7YUFDekI7U0FDRixDQUFDLENBQUM7SUFLTCxDQUFDO0NBQ0Y7QUE3R0Qsc0NBNkdDIiwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IHsgQXBwLCBEdXJhdGlvbiwgU3RhY2ssIFN0YWNrUHJvcHMsIENmbk91dHB1dCB9IGZyb20gJ2F3cy1jZGstbGliJztcbmltcG9ydCAqIGFzIHNxcyBmcm9tICdhd3MtY2RrLWxpYi9hd3Mtc3FzJztcbmltcG9ydCAqIGFzIGV2ZW50cyBmcm9tICdhd3MtY2RrLWxpYi9hd3MtZXZlbnRzJztcbmltcG9ydCAqIGFzIHRhcmdldHMgZnJvbSAnYXdzLWNkay1saWIvYXdzLWV2ZW50cy10YXJnZXRzJztcbmltcG9ydCAqIGFzIGVjMiBmcm9tICdhd3MtY2RrLWxpYi9hd3MtZWMyJztcbmltcG9ydCAqIGFzIGVjcyBmcm9tICdhd3MtY2RrLWxpYi9hd3MtZWNzJztcbmltcG9ydCAqIGFzIGlhbSBmcm9tICdhd3MtY2RrLWxpYi9hd3MtaWFtJztcbmltcG9ydCB7IENvbnN0cnVjdCB9IGZyb20gJ2NvbnN0cnVjdHMnO1xuaW1wb3J0IHsgQWRqdXN0bWVudFR5cGUgfSBmcm9tICdhd3MtY2RrLWxpYi9hd3MtYXV0b3NjYWxpbmcnO1xuXG5leHBvcnQgY2xhc3MgRWJTcXNFY3NTdGFjayBleHRlbmRzIFN0YWNrIHtcbiAgY29uc3RydWN0b3Ioc2NvcGU6IENvbnN0cnVjdCwgaWQ6IHN0cmluZywgcHJvcHM/OiBTdGFja1Byb3BzKSB7XG4gICAgc3VwZXIoc2NvcGUsIGlkLCBwcm9wcyk7XG4gICAgLy9DcmVhdGUgUXVldWVcbiAgICBjb25zdCBxdWV1ZSA9IG5ldyBzcXMuUXVldWUodGhpcywgJ0ViU3FzRWNzUXVldWUnLCB7XG4gICAgICB2aXNpYmlsaXR5VGltZW91dDogRHVyYXRpb24uc2Vjb25kcygzMDApXG4gICAgfSk7XG4gICAgXG4gICAgLy9DcmVhdGUgRXZlbnQgYnVzIGFuZCBydWxlXG4gICAgdmFyIGN1c3RvbV9idXMgPSBuZXcgZXZlbnRzLkV2ZW50QnVzKHRoaXMsIFwiYnVzXCIsIHtcbiAgICAgIFwiZXZlbnRCdXNOYW1lXCI6IFwidGVzdC1idXMtY2RrXCJcbiAgICB9KTtcbiAgICBjb25zdCBydWxlID0gbmV3IGV2ZW50cy5SdWxlKHRoaXMsIFwicnVsZVwiLCB7XG4gICAgICBcImV2ZW50QnVzXCI6IGN1c3RvbV9idXNcbiAgICB9KTtcbiAgICBydWxlLmFkZEV2ZW50UGF0dGVybih7XG4gICAgICBcInNvdXJjZVwiOiBbXCJlYi1zcXMtZWNzXCJdLFxuICAgICAgXCJkZXRhaWxUeXBlXCI6IFtcIm1lc3NhZ2UtZm9yLXF1ZXVlXCJdXG4gICAgfSk7XG4gICAgcnVsZS5hZGRUYXJnZXQobmV3IHRhcmdldHMuU3FzUXVldWUocXVldWUpKTtcbiAgICBuZXcgQ2ZuT3V0cHV0KHRoaXMsIFwiUXVldWVVUkxcIiwge1xuICAgICAgXCJkZXNjcmlwdGlvblwiOiBcIlVSTCBvZiBTUVMgUXVldWVcIixcbiAgICAgIFwidmFsdWVcIjogcXVldWUucXVldWVVcmxcbiAgICB9KTtcbiAgICBcbiAgICAvL0NyZWF0ZSBFQ1MgY2x1c3RlclxuICAgIGNvbnN0IG5hdEdhdGV3YXlQcm92aWRlciA9IGVjMi5OYXRQcm92aWRlci5pbnN0YW5jZSh7XG4gICAgICBpbnN0YW5jZVR5cGU6IG5ldyBlYzIuSW5zdGFuY2VUeXBlKFwidDMubmFub1wiKSxcbiAgICB9KTtcblxuICAgIGNvbnN0IHZwYyA9IG5ldyBlYzIuVnBjKHRoaXMsIFwiRmFyZ2F0ZVZQQ1wiLCB7XG4gICAgICBuYXRHYXRld2F5UHJvdmlkZXIsXG4gICAgICBuYXRHYXRld2F5czogMSxcbiAgICB9KTtcblxuICAgIGNvbnN0IGNsdXN0ZXIgPSBuZXcgZWNzLkNsdXN0ZXIodGhpcywgXCJDbHVzdGVyXCIsIHsgdnBjIH0pO1xuICAgIC8vRW5kLSBDcmVhdGUgRUNTIGNsdXN0ZXJcbiAgICBcbiAgICAvLyBDcmVhdGUgYSB0YXNrIHJvbGUgdGhhdCB3aWxsIGJlIHVzZWQgd2l0aGluIHRoZSBjb250YWluZXJcbiAgICBjb25zdCBFY3NUYXNrUm9sZSA9IG5ldyBpYW0uUm9sZSh0aGlzLCBcIkVjc1Rhc2tSb2xlXCIsIHtcbiAgICAgIGFzc3VtZWRCeTogbmV3IGlhbS5TZXJ2aWNlUHJpbmNpcGFsKFwiZWNzLXRhc2tzLmFtYXpvbmF3cy5jb21cIiksXG4gICAgfSk7XG5cbiAgICBFY3NUYXNrUm9sZS5hdHRhY2hJbmxpbmVQb2xpY3koXG4gICAgICBuZXcgaWFtLlBvbGljeSh0aGlzLCBcIlNRU0FkbWluQWNjZXNzXCIsIHtcbiAgICAgICAgc3RhdGVtZW50czogW1xuICAgICAgICAgIG5ldyBpYW0uUG9saWN5U3RhdGVtZW50KHtcbiAgICAgICAgICAgIGFjdGlvbnM6IFtcInNxczoqXCJdLFxuICAgICAgICAgICAgZWZmZWN0OiBpYW0uRWZmZWN0LkFMTE9XLFxuICAgICAgICAgICAgcmVzb3VyY2VzOiBbcXVldWUucXVldWVBcm5dLFxuICAgICAgICAgIH0pLFxuICAgICAgICBdLFxuICAgICAgfSlcbiAgICApOyAgICBcblxuICAgIC8vIENyZWF0ZSB0YXNrIGRlZmluaXRpb25cbiAgICBjb25zdCBmYXJnYXRlVGFza0RlZmluaXRpb24gPSBuZXcgZWNzLkZhcmdhdGVUYXNrRGVmaW5pdGlvbihcbiAgICAgIHRoaXMsXG4gICAgICBcIkZhcmdhdGVUYXNrRGVmXCIsXG4gICAgICB7XG4gICAgICAgIG1lbW9yeUxpbWl0TWlCOiA0MDk2LFxuICAgICAgICBjcHU6IDIwNDgsXG4gICAgICAgIHRhc2tSb2xlOiBFY3NUYXNrUm9sZVxuICAgICAgfVxuICAgICk7XG5cbiAgICAvLyBjcmVhdGUgYSB0YXNrIGRlZmluaXRpb24gd2l0aCBDbG91ZFdhdGNoIExvZ3NcbiAgICBjb25zdCBsb2dnaW5nID0gbmV3IGVjcy5Bd3NMb2dEcml2ZXIoe1xuICAgICAgc3RyZWFtUHJlZml4OiBcIm15YXBwbGljYXRpb25cIixcbiAgICB9KTtcblxuICAgIC8vIENyZWF0ZSBjb250YWluZXIgZnJvbSBsb2NhbCBgRG9ja2VyZmlsZWBcbiAgICBjb25zdCBhcHBDb250YWluZXIgPSBmYXJnYXRlVGFza0RlZmluaXRpb24uYWRkQ29udGFpbmVyKFwiQ29udGFpbmVyXCIsIHtcbiAgICAgIGltYWdlOiBlY3MuQ29udGFpbmVySW1hZ2UuZnJvbUFzc2V0KFwiLi9weXRob24tYXBwXCIpLCBcbiAgICAgIGVudmlyb25tZW50OiB7XG4gICAgICAgICAgcXVldWVVcmw6IHF1ZXVlLnF1ZXVlVXJsLFxuICAgICAgICAgIHJlZ2lvbjogcHJvY2Vzcy5lbnYuQ0RLX0RFRkFVTFRfUkVHSU9OISxcbiAgICAgICAgfSxcbiAgICAgIGxvZ2dpbmcsXG4gICAgfSk7XG5cbiAgICAvLyBDcmVhdGUgc2VydmljZVxuICAgIGNvbnN0IHNlcnZpY2UgPSBuZXcgZWNzLkZhcmdhdGVTZXJ2aWNlKHRoaXMsIFwiU2VydmljZVwiLCB7XG4gICAgICBjbHVzdGVyLFxuICAgICAgdGFza0RlZmluaXRpb246IGZhcmdhdGVUYXNrRGVmaW5pdGlvbixcbiAgICAgIGRlc2lyZWRDb3VudDogMCxcbiAgICB9KTtcbiAgICBcbiAgICAvLyBDb25maWd1cmUgdGFzayBhdXRvLXNjYWxpbmdcbiAgICBjb25zdCBzY2FsaW5nID0gc2VydmljZS5hdXRvU2NhbGVUYXNrQ291bnQoe1xuICAgICAgbWluQ2FwYWNpdHk6IDAsXG4gICAgICBtYXhDYXBhY2l0eTogMSxcbiAgICB9KTtcblxuICAgIC8vIFNldHVwIHNjYWxpbmcgbWV0cmljIGFuZCBjb29sZG93biBwZXJpb2RcbiAgICBzY2FsaW5nLnNjYWxlT25NZXRyaWMoXCJRdWV1ZU1lc3NhZ2VzVmlzaWJsZVNjYWxpbmdcIiwge1xuICAgICAgbWV0cmljOiBxdWV1ZS5tZXRyaWNBcHByb3hpbWF0ZU51bWJlck9mTWVzc2FnZXNWaXNpYmxlKCksXG4gICAgICBhZGp1c3RtZW50VHlwZTogQWRqdXN0bWVudFR5cGUuQ0hBTkdFX0lOX0NBUEFDSVRZLFxuICAgICAgY29vbGRvd246IER1cmF0aW9uLnNlY29uZHMoMzAwKSxcbiAgICAgIHNjYWxpbmdTdGVwczogW1xuICAgICAgICB7IHVwcGVyOiAwLCBjaGFuZ2U6IC0xIH0sXG4gICAgICAgIHsgbG93ZXI6IDEsIGNoYW5nZTogKzEgfSxcbiAgICAgIF0sXG4gICAgfSk7XG4gICAgXG5cbiAgICBcbiAgICBcbiAgfVxufVxuIl19