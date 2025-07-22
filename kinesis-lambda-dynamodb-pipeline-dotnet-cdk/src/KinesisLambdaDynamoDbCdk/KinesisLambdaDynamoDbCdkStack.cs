using Amazon.CDK;
using Amazon.CDK.AWS.Kinesis;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.Lambda.EventSources;
using Constructs;
using System.Collections.Generic;
using Amazon.CDK.AWS.Logs;
using System.Runtime.InteropServices;
using Amazon.CDK.AWS.DynamoDB;
using Attribute = Amazon.CDK.AWS.DynamoDB.Attribute;

namespace KinesisLambdaDynamoDbCdk
{   
    public class KinesisLambdaDynamoDbCdkStack : Stack
    {
        public KinesisLambdaDynamoDbCdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // Create Kinesis Data Stream
            var dataStream = new Stream(this, "AnalyticsDataStream", new StreamProps
            {
                StreamName = "AnalyticsDataStream",
                ShardCount = 1,
                RemovalPolicy = RemovalPolicy.DESTROY,
                RetentionPeriod = Duration.Days(1),
                Encryption = StreamEncryption.MANAGED,
                StreamMode = StreamMode.PROVISIONED
            });

            // Create DynamoDB table for processed data
            var table = new Table(this, "ProcessedDataTable", new TableProps
            {
                PartitionKey = new Attribute { Name = "Id", Type = AttributeType.STRING },
                BillingMode = BillingMode.PAY_PER_REQUEST,
                TableName = "processed-data-table",
                RemovalPolicy = RemovalPolicy.DESTROY,
                DeletionProtection = false,
                PointInTimeRecovery = false,
                Encryption = TableEncryption.AWS_MANAGED
            });

            // Build options for Lambda functions
            var buildOption = new BundlingOptions()
            {
                Image = Runtime.DOTNET_8.BundlingImage,
                User = "root",
                OutputType = BundlingOutput.ARCHIVED,
                Command = [
                    "/bin/sh",
                    "-c",
                    "dotnet tool install -g Amazon.Lambda.Tools && " +
                    "dotnet build && " +
                    "dotnet lambda package " +
                    "--function-architecture " + (RuntimeInformation.ProcessArchitecture == System.Runtime.InteropServices.Architecture.X64 ? "x86_64" : "arm64") + " " +
                    "--output-package /asset-output/function.zip"
                ],

            };

            // Create Lambda function for data processing
            var processFunction = new Function(this, "DataProcessFunction", new FunctionProps
            {
                Runtime = Runtime.DOTNET_8,
                MemorySize = 512,
                Timeout = Duration.Seconds(300),
                Architecture = RuntimeInformation.ProcessArchitecture == System.Runtime.InteropServices.Architecture.X64
                    ? Amazon.CDK.AWS.Lambda.Architecture.X86_64
                    : Amazon.CDK.AWS.Lambda.Architecture.ARM_64,
                FunctionName = "DataProcessFunction",
                Description = "Function to process data from Kinesis Data Stream",

                Handler = "DataProcessFunction",
                Code = Code.FromAsset(
                    "src/LambdaFunctions/DataProcessFunction/src",
                    new Amazon.CDK.AWS.S3.Assets.AssetOptions
                    {
                        Bundling = buildOption
                    }),

                Environment = new Dictionary<string, string>
                {
                    ["PROCESSED_TABLE_NAME"] = table.TableName
                },
                RetryAttempts = 0
            });

            // Add Kinesis as an event source for the process function
            processFunction.AddEventSource(new KinesisEventSource(dataStream, new KinesisEventSourceProps
            {
                BatchSize = 100,
                StartingPosition = StartingPosition.LATEST,
                BisectBatchOnError = false,
                Enabled = true,
                RetryAttempts = 1,
                ParallelizationFactor = 1,
                MaxBatchingWindow = Duration.Seconds(0),
                ReportBatchItemFailures = true
            }));

            // Grant permissions
            dataStream.GrantRead(processFunction);
            table.GrantWriteData(processFunction);

            // Output the stream name
            _ = new CfnOutput(this, "KinesisStreamName", new CfnOutputProps
            {
                Value = dataStream.StreamName,
                Description = "Kinesis Data Stream Name",
            });

            // Output the process function name
            _ = new CfnOutput(this, "DataProcessFunctionName", new CfnOutputProps
            {
                Value = processFunction.FunctionName,
                Description = "Process Function Name",
            });

            // Output the processed data table name
            _ = new CfnOutput(this, "ProcessedDataTableName", new CfnOutputProps
            {
                Value = table.TableName,
                Description = "Processed Data Table Name",
            });
        }
    }
}