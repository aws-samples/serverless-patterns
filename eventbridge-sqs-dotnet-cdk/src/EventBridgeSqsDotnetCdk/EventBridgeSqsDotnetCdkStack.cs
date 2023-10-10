using Amazon.CDK;
using Amazon.CDK.AWS.Events;
using Amazon.CDK.AWS.Events.Targets;
using Amazon.CDK.AWS.SQS;
using Constructs;
using EventBus = Amazon.CDK.AWS.Events.EventBus;
using EventBusProps = Amazon.CDK.AWS.Events.EventBusProps;

namespace EventBridgeSqsDotnetCdk
{
    public class EventBridgeSqsDotnetCdkStack : Stack
    {
        internal EventBridgeSqsDotnetCdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // SQS Queue
            var myQueue = new Queue(this, "MyQueue");

            // Custom EventBridge Bus
            var eventBus = new EventBus(this, "MySQSEventBus", new EventBusProps
            {
                EventBusName = "MySQSEventBus"
            });

            // EventBridge Rule
            var rule = new Rule(this, "MySQSRule", new RuleProps
            {
                Description = "SQS Event Bus Rule",
                EventPattern = new EventPattern
                {
                    Source = new[] { "cdk.myapp" }
                },
                EventBus = eventBus
            });

            rule.AddTarget(new SqsQueue(myQueue));

            // CDK Outputs
            new CfnOutput(this, "MySQSUrl", new CfnOutputProps
            {
                Value = myQueue.QueueUrl!,
                Description = "SQS Queue URL"
            });
        }
    }
}
