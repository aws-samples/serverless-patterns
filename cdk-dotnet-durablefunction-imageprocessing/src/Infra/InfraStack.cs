using System.Diagnostics;
using Amazon.CDK;
using Amazon.CDK.AWS.DynamoDB;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.S3;
using Amazon.CDK.AWS.S3.Notifications;
using Constructs;

namespace Infra;

internal sealed class InfraStack : Stack
{
    internal InfraStack(Construct scope, string id, IStackProps? props = null)
        : base(scope, id, props)
    {
        // ──────────────────────────────────────────────────────────────────
        // S3 Bucket — stores source images and processed outputs
        // ──────────────────────────────────────────────────────────────────
        var imagesBucket = new Bucket(this, "ImagesBucket", new BucketProps
        {
            RemovalPolicy = RemovalPolicy.DESTROY,
            AutoDeleteObjects = true,
            BlockPublicAccess = BlockPublicAccess.BLOCK_ALL,
            Encryption = BucketEncryption.S3_MANAGED,
            LifecycleRules =
            [
                new LifecycleRule
                {
                    Id = "ExpireProcessedImages",
                    Prefix = "thumbnails/",
                    Expiration = Duration.Days(90)
                },
                new LifecycleRule
                {
                    Id = "ExpireWatermarked",
                    Prefix = "watermarked/",
                    Expiration = Duration.Days(90)
                }
            ]
        });

        // ──────────────────────────────────────────────────────────────────
        // DynamoDB Table — stores aggregated pipeline results
        // ──────────────────────────────────────────────────────────────────
        var resultsTable = new Table(this, "ResultsTable", new TableProps
        {
            PartitionKey = new Amazon.CDK.AWS.DynamoDB.Attribute
            {
                Name = "ImageId",
                Type = AttributeType.STRING
            },
            BillingMode = BillingMode.PAY_PER_REQUEST,
            RemovalPolicy = RemovalPolicy.DESTROY,
            PointInTimeRecoverySpecification = new PointInTimeRecoverySpecification
            {
                PointInTimeRecoveryEnabled = true
            }
        });

        // ──────────────────────────────────────────────────────────────────
        // Lambda Function — Durable image processing workflow
        // ──────────────────────────────────────────────────────────────────
        var publishOutputPath = PublishLambdaProject("src/ImageProcessor/ImageProcessor.csproj");

        var imageProcessorFunction = new Function(this, "ImageProcessorFunction", new FunctionProps
        {
            Runtime = Runtime.DOTNET_10,
            Handler = "ImageProcessor::ImageProcessor.ImageProcessorHandler::Handler",
            Code = Code.FromAsset(publishOutputPath),
            MemorySize = 1024,
            Timeout = Duration.Seconds(900),
            DurableConfig = new DurableConfig
            {
                ExecutionTimeout = Duration.Minutes(15),
                RetentionPeriod = Duration.Days(7)
            },
            Environment = new Dictionary<string, string>
            {
                ["RESULTS_TABLE_NAME"] = resultsTable.TableName
            },
            Description = "Durable Function: Image processing pipeline with fan-out/fan-in"
        });

        // Grant the Lambda function permissions
        imagesBucket.GrantReadWrite(imageProcessorFunction);
        resultsTable.GrantWriteData(imageProcessorFunction);

        // ──────────────────────────────────────────────────────────────────
        // S3 Trigger Function — invoked on upload, starts durable execution
        // ──────────────────────────────────────────────────────────────────
        var s3TriggerFunction = new Function(this, "S3TriggerFunction", new FunctionProps
        {
            Runtime = Runtime.DOTNET_10,
            Handler = "ImageProcessor::ImageProcessor.S3TriggerHandler::Handler",
            Code = Code.FromAsset(publishOutputPath),
            MemorySize = 256,
            Timeout = Duration.Seconds(30),
            Environment = new Dictionary<string, string>
            {
                ["IMAGE_PROCESSOR_FUNCTION_ARN"] = imageProcessorFunction.FunctionArn
            },
            Description = "S3 trigger: starts durable image processing on upload"
        });

        // Grant the trigger permission to invoke the durable function
        imageProcessorFunction.GrantInvoke(s3TriggerFunction);

        // S3 event notification: trigger on object creation in uploads/ prefix
        imagesBucket.AddEventNotification(
            Amazon.CDK.AWS.S3.EventType.OBJECT_CREATED,
            new Amazon.CDK.AWS.S3.Notifications.LambdaDestination(s3TriggerFunction),
            new NotificationKeyFilter { Prefix = "uploads/" });

        // ──────────────────────────────────────────────────────────────────
        // Outputs
        // ──────────────────────────────────────────────────────────────────
        _ = new CfnOutput(this, "ImagesBucketName", new CfnOutputProps
        {
            Value = imagesBucket.BucketName,
            Description = "S3 bucket for uploading source images"
        });

        _ = new CfnOutput(this, "ResultsTableName", new CfnOutputProps
        {
            Value = resultsTable.TableName,
            Description = "DynamoDB table storing pipeline results"
        });

        _ = new CfnOutput(this, "ImageProcessorFunctionArn", new CfnOutputProps
        {
            Value = imageProcessorFunction.FunctionArn,
            Description = "ARN of the image processor Lambda function"
        });
    }

    /// <summary>
    /// Publishes a .NET Lambda project in Release configuration and returns the output path.
    /// Called during CDK synthesis so that `cdk deploy` doesn't require a separate publish step.
    /// </summary>
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
