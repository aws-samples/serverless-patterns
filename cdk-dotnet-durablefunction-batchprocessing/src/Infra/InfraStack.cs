using System.Diagnostics;
using Amazon.CDK;
using Amazon.CDK.AWS.DynamoDB;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.S3;
using Constructs;

namespace Infra;

internal sealed class InfraStack : Stack
{
    internal InfraStack(Construct scope, string id, IStackProps? props = null)
        : base(scope, id, props)
    {
        // ──────────────────────────────────────────────────────────────────
        // S3 Bucket — stores input files and the summary report
        // ──────────────────────────────────────────────────────────────────
        var filesBucket = new Bucket(this, "FilesBucket", new BucketProps
        {
            RemovalPolicy = RemovalPolicy.DESTROY,
            AutoDeleteObjects = true,
            BlockPublicAccess = BlockPublicAccess.BLOCK_ALL,
            Encryption = BucketEncryption.S3_MANAGED
        });

        // ──────────────────────────────────────────────────────────────────
        // DynamoDB Table — stores per-file processing results
        // ──────────────────────────────────────────────────────────────────
        var resultsTable = new Table(this, "ResultsTable", new TableProps
        {
            PartitionKey = new Amazon.CDK.AWS.DynamoDB.Attribute
            {
                Name = "BatchId",
                Type = AttributeType.STRING
            },
            SortKey = new Amazon.CDK.AWS.DynamoDB.Attribute
            {
                Name = "FileName",
                Type = AttributeType.STRING
            },
            BillingMode = BillingMode.PAY_PER_REQUEST,
            RemovalPolicy = RemovalPolicy.DESTROY
        });

        // ──────────────────────────────────────────────────────────────────
        // Lambda Function — Durable batch file processing workflow
        // ──────────────────────────────────────────────────────────────────
        var publishOutputPath = PublishLambdaProject("src/BatchProcessor/BatchProcessor.csproj");

        var batchProcessorFunction = new Function(this, "BatchProcessorFunction", new FunctionProps
        {
            Runtime = Runtime.DOTNET_10,
            Handler = "BatchProcessor::BatchProcessor.BatchProcessorHandler::Handler",
            Code = Code.FromAsset(publishOutputPath),
            MemorySize = 512,
            Timeout = Duration.Seconds(900),
            DurableConfig = new DurableConfig
            {
                ExecutionTimeout = Duration.Minutes(60),
                RetentionPeriod = Duration.Days(7)
            },
            Environment = new Dictionary<string, string>
            {
                ["RESULTS_TABLE_NAME"] = resultsTable.TableName,
                ["FILES_BUCKET_NAME"] = filesBucket.BucketName
            },
            Description = "Durable Function: Batch file processing with dynamic fan-out/fan-in"
        });

        // Grant permissions
        filesBucket.GrantReadWrite(batchProcessorFunction);
        resultsTable.GrantWriteData(batchProcessorFunction);

        // ──────────────────────────────────────────────────────────────────
        // Outputs
        // ──────────────────────────────────────────────────────────────────
        _ = new CfnOutput(this, "FilesBucketName", new CfnOutputProps
        {
            Value = filesBucket.BucketName,
            Description = "S3 bucket for input files and summary reports"
        });

        _ = new CfnOutput(this, "ResultsTableName", new CfnOutputProps
        {
            Value = resultsTable.TableName,
            Description = "DynamoDB table storing per-file processing results"
        });

        _ = new CfnOutput(this, "BatchProcessorFunctionArn", new CfnOutputProps
        {
            Value = batchProcessorFunction.FunctionArn,
            Description = "ARN of the batch processor Lambda function"
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
