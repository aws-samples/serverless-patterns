using Amazon.CDK;
using Amazon.CDK.AWS.APIGateway;
using Amazon.CDK.AWS.Batch;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.Logs;
using Amazon.CDK.AWS.S3;
using Amazon.CDK.AWS.StepFunctions;
using Amazon.CDK.AWS.StepFunctions.Tasks;
using Constructs;
using System.Collections.Generic;
using System.Security;

namespace cdk
{
    public class CdkStack : Stack
    {
        internal CdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            var storeTaskTokenBucket = new Amazon.CDK.AWS.S3.Bucket(this, "token-store-bucket", new BucketProps
            {
                EnforceSSL = true,
                BlockPublicAccess = BlockPublicAccess.BLOCK_ALL,
                Encryption = BucketEncryption.S3_MANAGED,
                ServerAccessLogsPrefix = "Logs",
                ServerAccessLogsBucket = new Amazon.CDK.AWS.S3.Bucket(this, "server-access-logs-bucket", new BucketProps
                {
                    EnforceSSL = true,
                    BlockPublicAccess = BlockPublicAccess.BLOCK_ALL,
                    Encryption = BucketEncryption.S3_MANAGED
                })
            });

            storeTaskTokenBucket.AddLifecycleRule(new LifecycleRule()
            {
                Expiration=Duration.Days(3)
            });


            var processOrderFunction = new Amazon.CDK.AWS.Lambda.Function(this, "ListFilesFunction", new FunctionProps()
            {
                Runtime = Runtime.DOTNET_6,
                Code = Code.FromAsset("processOrderFunction/bin/Release/net6.0/publish"),
                Handler = "processOrderFunction::processOrderFunction.Function::FunctionHandler",
                Timeout = Duration.Minutes(10)
            });

            var completeOrderFunction = new Amazon.CDK.AWS.Lambda.Function(this, "completeOrderFunction", new FunctionProps()
            {
                Runtime = Runtime.DOTNET_6,
                Code = Code.FromAsset("completeOrderFunction/bin/Release/net6.0/publish"),
                Handler = "completeOrderFunction::completeOrderFunction.Function::FunctionHandler",
                Timeout = Duration.Minutes(10)
            });

            var storeTaskTokenFunction = new Amazon.CDK.AWS.Lambda.Function(this, "storeTaskTokenFunction", new FunctionProps()
            {
                Runtime = Runtime.DOTNET_6,
                Code = Code.FromAsset("storeTaskTokenFunction/bin/Release/net6.0/publish"),
                Handler = "storeTaskTokenFunction::storeTaskTokenFunction.Function::FunctionHandler",
                Timeout = Duration.Minutes(3),
                Environment = new Dictionary<string, string>() { { "TokenStoreBucket", storeTaskTokenBucket.BucketName } }
            });

            storeTaskTokenBucket.GrantReadWrite(storeTaskTokenFunction);

            var workflowAPIFunction = new Amazon.CDK.AWS.Lambda.Function(this, "callbackPatternAPIFunction", new FunctionProps()
            {
                Runtime = Runtime.DOTNET_6,
                Code = Code.FromAsset("CallbackPatternSample.API/bin/Release/net6.0/publish"),
                Handler = "CallbackPatternSample.API::CallbackPatternSample.API.LambdaEntryPoint::FunctionHandlerAsync",
                Timeout = Duration.Minutes(10),
                Environment = new Dictionary<string, string>() { { "TokenStoreBucket", storeTaskTokenBucket.BucketName } }
            });
            storeTaskTokenBucket.GrantRead(workflowAPIFunction);


            var sfnLog = new LogGroup(this, "sfnLog", new LogGroupProps
            {
                LogGroupName = "sfnLogGroup",
                RemovalPolicy = RemovalPolicy.DESTROY,
                Retention = RetentionDays.ONE_WEEK
            });

            var stateMachine = new StateMachine(this, "OrderStateMachine", new StateMachineProps
            {
                Logs = new LogOptions
                {
                    Destination = sfnLog,
                    IncludeExecutionData = true,
                    Level = LogLevel.ALL
                },
                TracingEnabled = true,
                Definition = new Amazon.CDK.AWS.StepFunctions.Tasks.LambdaInvoke(this, "ProcessOrder", new LambdaInvokeProps
                {
                    LambdaFunction = processOrderFunction,
                    OutputPath = "$.Payload"
                }
                ).Next(
                    new Amazon.CDK.AWS.StepFunctions.Tasks.LambdaInvoke(this, "WaitForConfirmation",
                        new LambdaInvokeProps
                        {
                            LambdaFunction = storeTaskTokenFunction,
                            IntegrationPattern = IntegrationPattern.WAIT_FOR_TASK_TOKEN,
                            Payload = TaskInput.FromObject(new Dictionary<string, object> {
                                {"TaskToken", JsonPath.TaskToken},
                                {"Input.$","$" }})
                        })
                    ).Next(
                       new Amazon.CDK.AWS.StepFunctions.Tasks.LambdaInvoke(this, "CompleteOrder",
                        new LambdaInvokeProps
                        {
                            LambdaFunction = completeOrderFunction
                        })
                       )
            }) ;

            workflowAPIFunction.AddEnvironment("OrdersStateMachine", stateMachine.StateMachineArn);
            stateMachine.Grant(workflowAPIFunction, "states:ListExecutions", "states:StartExecution", "states:SendTaskSuccess", "states:SendTaskFailure");

            var devLogGroup = new Amazon.CDK.AWS.Logs.LogGroup(this, "devLogGroup");

            var api = new LambdaRestApi(this, "OrderAppAPIGateway", new LambdaRestApiProps
            {
                Description = "Order App API Gateway",
                DeployOptions = new StageOptions() { StageName = "dev", TracingEnabled=true, LoggingLevel=MethodLoggingLevel.ERROR,AccessLogDestination= new LogGroupLogDestination(devLogGroup), AccessLogFormat= AccessLogFormat.JsonWithStandardFields() },
                Handler = workflowAPIFunction,
                ApiKeySourceType = ApiKeySourceType.HEADER,
                Proxy = true,
                CloudWatchRole=true

            });
            
            api.AddApiKey("x-api-key", new ApiKeyOptions() { ApiKeyName = "x-api-key", Value = "K37BiZoU6T9eTLIkTMIvE1C0JKvEvibe5wvzeFdQ" });
        }
    }
}
