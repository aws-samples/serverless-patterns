using Amazon.CDK;
using Amazon.CDK.AWS.Apigatewayv2;
using Amazon.CDK.AWS.Events;
using EventTargets = Amazon.CDK.AWS.Events.Targets;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Logs;
using Constructs;
using Amazon.CDK.AWS.Apigatewayv2.Alpha;
using System.Collections.Generic;

namespace ApigwHttpApiEventbridgeDotnetCdk
{
    public class ApigwHttpApiEventbridgeDotnetCdkStack : Stack
    {
        internal ApigwHttpApiEventbridgeDotnetCdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            var eventBus = new EventBus(this, "MyEventBus", new EventBusProps
            {
                EventBusName = "MyEventBus"
            });

            // Logging
            var eventLoggerRule = new Rule(this, "EventLoggerRule", new RuleProps
            {
                Description = "Log all events",
                EventPattern = new EventPattern
                {
                    Region = new string[] { "us-west-2" }
                },
                EventBus = eventBus
            });

            var logGroup = new LogGroup(this, "EventLogGroup", new LogGroupProps
            {
                LogGroupName = "/aws/events/MyEventBus",
            });

            eventLoggerRule.AddTarget(new EventTargets.CloudWatchLogGroup(logGroup));

            // API
            var httpApi = new HttpApi(this, "MyHttpApi");

            // There"s no Eventbridge integration available as CDK L2 yet, so we have to use L1 and create Role, Integration and Route
            var apiRole = new Role(this, "EventBridgeIntegrationRole", new RoleProps
            {
                AssumedBy = new ServicePrincipal("apigateway.amazonaws.com"),
            });

            apiRole.AddToPolicy(
            new PolicyStatement(new PolicyStatementProps
            {
                Effect = Effect.ALLOW,
                Resources = new string[] { eventBus.EventBusArn },
                Actions = new string[] { "events:PutEvents" },
            })
            );

            var eventbridgeIntegration = new CfnIntegration(
                this,
                "EventBridgeIntegration",
                new CfnIntegrationProps
                {
                    ApiId = httpApi.HttpApiId,
                    IntegrationType = "AWS_PROXY",
                    IntegrationSubtype = "EventBridge-PutEvents",
                    CredentialsArn = apiRole.RoleArn,
                    RequestParameters = new Dictionary<string, object>
                    {
                        ["Source"] = "WebApp",
                        ["DetailType"] = "MyDetailType",
                        ["Detail"] = "$request.body",
                        ["EventBusName"] = eventBus.EventBusArn
                    },
                    PayloadFormatVersion = "1.0",
                    TimeoutInMillis = 10000,
                }
            );

            new CfnRoute(this, "EventRoute", new CfnRouteProps
            {
                ApiId = httpApi.HttpApiId,
                RouteKey = "POST /",
                Target = $"integrations/{eventbridgeIntegration.Ref}",
            });

            new CfnOutput(this, "apiUrl", new CfnOutputProps { Value = httpApi.Url!, Description = "HTTP API endpoint URL" });
        }
    }
}
