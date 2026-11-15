using Amazon.CDK;
using Amazon.CDK.AWS.Events;
using Amazon.CDK.AWS.Events.Targets;
using Amazon.CDK.AWS.Logs;
using Constructs;
using EventBus = Amazon.CDK.AWS.Events.EventBus;
using EventBusProps = Amazon.CDK.AWS.Events.EventBusProps;
using LogGroupProps = Amazon.CDK.AWS.Logs.LogGroupProps;

namespace EventBridgeCloudWatchDotnetCdk
{
    public class EventBridgeCloudWatchDotnetCdkStack : Stack
    {
        internal EventBridgeCloudWatchDotnetCdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // CloudWatch Log Group
            var cloudWatchLogGroup = new LogGroup(this, "CloudWatchLogs", new LogGroupProps
            {
                RemovalPolicy = RemovalPolicy.DESTROY,
                Retention = RetentionDays.ONE_DAY
            });

            // EventBridge Event Bus
            var eventBus = new EventBus(this, "MyCloudWatchEventBus", new EventBusProps
            {
                EventBusName = "MyCloudWatchEventBus"
            });
            
            // EventBridge Rule
            var cloudWatchLogsRule = new Rule(this, "cloudWatchLogsRule", new RuleProps
            {
                Description = "CloudWatch Logs Event Bus Rule",
                EventPattern = new EventPattern
                {
                    Source = new[] { "cdk.myapp" }
                },
                EventBus = eventBus
            });
            
            cloudWatchLogsRule.AddTarget(new CloudWatchLogGroup(cloudWatchLogGroup));
            
            // CDK Outputs
            new CfnOutput(this, "LogGroupName", new CfnOutputProps
            {
                Value = cloudWatchLogGroup.LogGroupName!,
                Description = "CloudWatch Log Group Name"
            });
        }
    }
}
