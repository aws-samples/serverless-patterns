using Amazon.CDK;
using Amazon.CDK.AWS.DynamoDB;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Lambda;
using Constructs;

namespace Cdk
{
    public class CdkStack : Stack
    {
        private string sourceTableName = "SourceDynamoDB";
        private string targetTableName = "TargetDynamoDB";
        private string functionName = "ProcessDynamoDBRecords";

        internal CdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            var buildOption = new BundlingOptions()
            {
                Image = Runtime.DOTNET_6.BundlingImage,
                User = "root",
                OutputType = BundlingOutput.ARCHIVED,
                Command = new string[]{
               "/bin/sh",
                "-c",
                " dotnet tool install -g Amazon.Lambda.Tools"+
                " && dotnet build"+
                " && dotnet lambda package --output-package /asset-output/function.zip"
                }
            };

            // Create a source DynamoDB Table
            // Note: RemovalPolicy.DESTROY will delete the DynamoDB table when you run cdk destroy command
            // Enable the DynamoDB stream
            Table sourceDynamoDBTable = new Table(this, "SourceDynamoDBTable", new TableProps
            {
                TableName = sourceTableName,
                PartitionKey = new Attribute { Name = "Id", Type = AttributeType.STRING },
                RemovalPolicy = RemovalPolicy.DESTROY,
                Stream = StreamViewType.NEW_IMAGE
            });

            // Create Lambda execution role
            Role lambdaExecutionRole = new Role(this, functionName + "-execution-role", new RoleProps
            {
                RoleName = functionName + "-execution-role",
                AssumedBy = new ServicePrincipal("lambda.amazonaws.com")
            });

            // Add AWS Managed Policies
            // Best practice is to provide least privilege access
            lambdaExecutionRole.AddManagedPolicy(ManagedPolicy.FromAwsManagedPolicyName("AmazonDynamoDBFullAccess"));
            lambdaExecutionRole.AddManagedPolicy(ManagedPolicy.FromAwsManagedPolicyName("service-role/AWSLambdaBasicExecutionRole"));

            // Create a Lambda function to process the DynamoDB stream
            Function processDynamoDBFunc = new Function(this, "ProcessDynamoDBRecordsFunction", new FunctionProps
            {
                FunctionName = functionName,
                Runtime = Runtime.DOTNET_6,
                Code = Code.FromAsset("code/src/AddItemsDynamoDB", new Amazon.CDK.AWS.S3.Assets.AssetOptions()
                {
                    Bundling = buildOption
                }),
                Handler = "AddItemsDynamoDB::AddItemsDynamoDB.Function::FunctionHandler",
                Role = lambdaExecutionRole,
                Timeout = Duration.Seconds(120)
            });

            // Add an event source in AWS Lambda
            EventSourceMapping eventSourceMapping = new EventSourceMapping(this, "EventSourceMapping", new EventSourceMappingProps
            {
                Target = processDynamoDBFunc,
                BatchSize = 100,
                StartingPosition = StartingPosition.LATEST,
                EventSourceArn = sourceDynamoDBTable.TableStreamArn
            });
            eventSourceMapping.Node.AddDependency(processDynamoDBFunc);
            eventSourceMapping.Node.AddDependency(sourceDynamoDBTable);

            // Create a Target DynamoDB Table
            // Note: RemovalPolicy.DESTROY will delete the DynamoDB table when you run cdk destroy command
            Table targetDynamoDBTable = new Table(this, "TargetDynamoDBTable", new TableProps
            {
                TableName = targetTableName,
                PartitionKey = new Attribute { Name = "Id", Type = AttributeType.STRING },
                RemovalPolicy = RemovalPolicy.DESTROY
            });
        }
    }
}