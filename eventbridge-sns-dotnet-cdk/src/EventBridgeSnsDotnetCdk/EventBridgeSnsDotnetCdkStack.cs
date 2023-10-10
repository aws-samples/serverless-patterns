using Amazon.CDK;
using Amazon.CDK.AWS.Events;
using Amazon.CDK.AWS.Events.Targets;
using Amazon.CDK.AWS.SNS;
using Constructs;
using EventBus = Amazon.CDK.AWS.Events.EventBus;
using EventBusProps = Amazon.CDK.AWS.Events.EventBusProps;

namespace EventBridgeSNSDotnetCdk
{
    public class EventBridgeSnsDotnetCdkStack : Stack
    {
        internal EventBridgeSnsDotnetCdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // SNS Topic
            var mySnsTopic = new Topic(this, "MySNSTopic");

            // Custom EventBridge Bus
            var eventBus = new EventBus(this, "MySNSEventBus", new EventBusProps
            {
                EventBusName = "MySNSEventBus"
            });
            
            // EventBridge Rule
            var rule = new Rule(this, "MySNSRule", new RuleProps
            {
                Description = "SNS Event Bus Rule",
                EventPattern = new EventPattern
                {
                    Source = new[] { "cdk.myapp" }
                },
                EventBus = eventBus
            });
            
            rule.AddTarget(new SnsTopic(mySnsTopic));
            
            // CDK Outputs
            new CfnOutput(this, "SNSTopicName", new CfnOutputProps
            {
                Value = mySnsTopic.TopicName!,
                Description ="SNS topic name"
            });
            new CfnOutput(this, "SNSTopicARN", new CfnOutputProps
            {
                Value = mySnsTopic.TopicArn!,
                Description ="SNS topic ARN"
            });
        }
    }
}
