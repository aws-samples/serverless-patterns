using System.Diagnostics;
using Amazon.CDK;
using Amazon.CDK.AWS.APIGateway;
using Amazon.CDK.AWS.DynamoDB;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.SNS;
using Constructs;

namespace Infra;

internal sealed class InfraStack : Stack
{
    internal InfraStack(Construct scope, string id, IStackProps? props = null)
        : base(scope, id, props)
    {
        // ──────────────────────────────────────────────────────────────────
        // DynamoDB Table — device registry and status
        // ──────────────────────────────────────────────────────────────────
        var deviceTable = new Table(this, "DeviceTable", new TableProps
        {
            PartitionKey = new Amazon.CDK.AWS.DynamoDB.Attribute
            {
                Name = "DeviceId",
                Type = AttributeType.STRING
            },
            BillingMode = BillingMode.PAY_PER_REQUEST,
            RemovalPolicy = RemovalPolicy.DESTROY
        });

        // ──────────────────────────────────────────────────────────────────
        // SNS Topic — device-offline alerts
        // ──────────────────────────────────────────────────────────────────
        var alertTopic = new Topic(this, "DeviceOfflineAlertTopic", new TopicProps
        {
            DisplayName = "IoT Device Offline Alerts"
        });

        // ──────────────────────────────────────────────────────────────────
        // Lambda: Heartbeat Monitor — eternal durable orchestration
        // ──────────────────────────────────────────────────────────────────
        var publishOutputPath = PublishLambdaProject("src/HeartbeatMonitor/HeartbeatMonitor.csproj");

        var monitorFunction = new Function(this, "HeartbeatMonitorFunction", new FunctionProps
        {
            Runtime = Runtime.DOTNET_10,
            Handler = "HeartbeatMonitor::HeartbeatMonitor.HeartbeatMonitorHandler::Handler",
            Code = Code.FromAsset(publishOutputPath),
            MemorySize = 256,
            Timeout = Duration.Seconds(900),
            DurableConfig = new DurableConfig
            {
                ExecutionTimeout = Duration.Days(365),
                RetentionPeriod = Duration.Days(3)
            },
            Environment = new Dictionary<string, string>
            {
                ["DEVICE_TABLE_NAME"] = deviceTable.TableName,
                ["ALERT_TOPIC_ARN"] = alertTopic.TopicArn
            },
            Description = "Durable Function: IoT heartbeat monitor (eternal orchestration)"
        });

        deviceTable.GrantReadWriteData(monitorFunction);
        alertTopic.GrantPublish(monitorFunction);

        // Allow the monitor to self-invoke for continue-as-new.
        monitorFunction.AddToRolePolicy(new Amazon.CDK.AWS.IAM.PolicyStatement(new Amazon.CDK.AWS.IAM.PolicyStatementProps
        {
            Actions = ["lambda:InvokeFunction"],
            Resources = [FormatArn(new ArnComponents
            {
                Service = "lambda",
                Resource = "function",
                ResourceName = "*",
                ArnFormat = ArnFormat.COLON_RESOURCE_NAME
            })]
        }));

        // ──────────────────────────────────────────────────────────────────
        // Lambda: Heartbeat Receiver — API for devices to send heartbeats
        // ──────────────────────────────────────────────────────────────────
        var receiverFunction = new Function(this, "HeartbeatReceiverFunction", new FunctionProps
        {
            Runtime = Runtime.DOTNET_10,
            Handler = "HeartbeatMonitor::HeartbeatMonitor.HeartbeatReceiverHandler::Handler",
            Code = Code.FromAsset(publishOutputPath),
            MemorySize = 256,
            Timeout = Duration.Seconds(30),
            Environment = new Dictionary<string, string>
            {
                ["DEVICE_TABLE_NAME"] = deviceTable.TableName
            },
            Description = "Receives heartbeat signals from IoT devices"
        });

        deviceTable.GrantReadWriteData(receiverFunction);

        // ──────────────────────────────────────────────────────────────────
        // API Gateway — REST API with API Key authentication
        // Simplest device auth: devices include x-api-key header
        // ──────────────────────────────────────────────────────────────────
        var api = new RestApi(this, "HeartbeatApi", new RestApiProps
        {
            RestApiName = "IoT Heartbeat API",
            Description = "API for IoT devices to send heartbeat signals",
            ApiKeySourceType = ApiKeySourceType.HEADER
        });

        var heartbeatResource = api.Root.AddResource("heartbeat");
        heartbeatResource.AddMethod("POST", new LambdaIntegration(receiverFunction), new MethodOptions
        {
            ApiKeyRequired = true
        });

        // Create a usage plan and API key for device authentication
        var usagePlan = api.AddUsagePlan("DeviceUsagePlan", new UsagePlanProps
        {
            Name = "DeviceHeartbeatPlan",
            Description = "Usage plan for IoT device heartbeats",
            Throttle = new ThrottleSettings
            {
                RateLimit = 100,
                BurstLimit = 200
            }
        });

        usagePlan.AddApiStage(new UsagePlanPerApiStage
        {
            Api = api,
            Stage = api.DeploymentStage
        });

        var apiKey = api.AddApiKey("DeviceApiKey", new ApiKeyOptions
        {
            ApiKeyName = "iot-device-heartbeat-key",
            Description = "API key for IoT devices to authenticate heartbeat requests"
        });

        usagePlan.AddApiKey(apiKey);

        // ──────────────────────────────────────────────────────────────────
        // Outputs
        // ──────────────────────────────────────────────────────────────────
        _ = new CfnOutput(this, "DeviceTableName", new CfnOutputProps
        {
            Value = deviceTable.TableName,
            Description = "DynamoDB table for device registry"
        });

        _ = new CfnOutput(this, "AlertTopicArn", new CfnOutputProps
        {
            Value = alertTopic.TopicArn,
            Description = "SNS topic for offline device alerts"
        });

        _ = new CfnOutput(this, "HeartbeatMonitorFunctionArn", new CfnOutputProps
        {
            Value = monitorFunction.FunctionArn,
            Description = "ARN of the heartbeat monitor durable function"
        });

        _ = new CfnOutput(this, "HeartbeatApiUrl", new CfnOutputProps
        {
            Value = api.Url,
            Description = "API Gateway URL for device heartbeats"
        });

        _ = new CfnOutput(this, "ApiKeyId", new CfnOutputProps
        {
            Value = apiKey.KeyId,
            Description = "API Key ID (use 'aws apigateway get-api-key --api-key <id> --include-value' to get the value)"
        });
    }

    private static string PublishLambdaProject(string projectPath)
    {
        var publishDir = Path.Combine(
            Path.GetDirectoryName(projectPath)!,
            "bin", "Release", "net10.0", "publish");

        var process = Process.Start(new ProcessStartInfo
        {
            FileName = "dotnet",
            Arguments = $"publish \"{projectPath}\" -c Release -r linux-x64 --self-contained false -o \"{publishDir}\"",
            RedirectStandardOutput = true,
            RedirectStandardError = true,
            UseShellExecute = false,
        }) ?? throw new InvalidOperationException("Failed to start dotnet publish process.");

        var stdout = process.StandardOutput.ReadToEnd();
        var stderr = process.StandardError.ReadToEnd();
        process.WaitForExit();

        if (process.ExitCode != 0)
        {
            throw new InvalidOperationException(
                $"dotnet publish failed for '{projectPath}' (exit code {process.ExitCode}):\n{stderr}\n{stdout}");
        }

        return publishDir;
    }
}
