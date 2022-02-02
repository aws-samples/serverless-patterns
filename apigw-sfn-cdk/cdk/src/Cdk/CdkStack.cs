using System.Collections.Generic;
using Amazon.CDK;
using Amazon.CDK.AWS.APIGateway;
using Amazon.CDK.AWS.Apigatewayv2;
using Amazon.CDK.AWS.DynamoDB;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.Logs;
using Amazon.CDK.AWS.SAM;
using Amazon.CDK.AWS.StepFunctions;
using AssetOptions = Amazon.CDK.AWS.S3.Assets.AssetOptions;
using Constructs;

namespace Cdk
{
    public class CdkStack : Stack
    {
        internal CdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            var startState = new Pass(this, "StartState");

            var logGroup = new LogGroup(this, "HttpExpressWorkflowLogGroup");

            var stepFunction = new StateMachine(this, "HttpExpressWorkflow", new StateMachineProps()
            {
                StateMachineName = "HttpExpressWorkflowExample",
                StateMachineType = StateMachineType.EXPRESS,
                Definition = startState,
                Logs = new LogOptions()
                {
                    Destination = logGroup,
                    Level = LogLevel.ALL
                },
                TracingEnabled = true
            });

            var apiGatewayRole = new Role(this, "ApiGatewayRole", new RoleProps()
            {
                AssumedBy = new ServicePrincipal("apigateway.amazonaws.com")
            });

            apiGatewayRole.AddToPolicy(new PolicyStatement(new PolicyStatementProps()
            {
                Effect = Effect.ALLOW,
                Sid = "AllowStepFunctionExecution",
                Actions = new string[1] {"states:StartSyncExecution"},
                Resources = new string[1] {stepFunction.StateMachineArn}
            }));

            var httpApi = new CfnHttpApi(this, "HttpApi", new CfnHttpApiProps()
            {
                StageName = "Main",
            });

            var integration = new CfnIntegration(this, "StepFunctionIntegration", new CfnIntegrationProps()
            {
                ApiId = httpApi.Ref,
                IntegrationType = "AWS_PROXY",
                IntegrationSubtype = "StepFunctions-StartSyncExecution",
                CredentialsArn = apiGatewayRole.RoleArn,
                RequestParameters = new Dictionary<string, string>(2)
                {
                    { "Input", "$request.body"},
                    { "StateMachineArn", stepFunction.StateMachineArn}
                },
                PayloadFormatVersion = "1.0",
                ConnectionType = "INTERNET"
            });

            var route = new CfnRoute(this, "StepFunctionRoute", new CfnRouteProps()
            {
                ApiId = httpApi.Ref,
                RouteKey = "POST /execute",
                Target = $"integrations/{integration.Ref}"
            });
        }
    }
}
