using Amazon.CDK;
using Amazon.CDK.AWS.DynamoDB;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.Lambda.EventSources;
using Amazon.CDK.AWS.Logs;
using Constructs;

namespace Cdk
{
    public class CdkStack : Stack
    {
        internal CdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            var lambdaFunctionName = "dynamodbLambdaFunction";
            // Create DynamoDB Table
            var dynamoDbTable = new Table(this, "CdkTable", new TableProps
            {
                PartitionKey = new Attribute { Name = "PK", Type = AttributeType.STRING },
                SortKey = new Attribute { Name = "SK", Type = AttributeType.STRING },
                BillingMode = BillingMode.PAY_PER_REQUEST,
                Stream = StreamViewType.NEW_AND_OLD_IMAGES
            });

            //Lambda Function IAM role
            var lambdaIAMRole = new Role(this, "DynamoDBLambdaRole", new RoleProps
            {
                AssumedBy = new ServicePrincipal("lambda.amazonaws.com"),
                Description = "IAM Role for the lambda function"
            });
            
            // Lambda Function Build Commands
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

            //Lambda function
            var lambdaFunction = new Function(this, "LambdaFunction", new FunctionProps
            {
                FunctionName= lambdaFunctionName,
                MemorySize = 512,
                Timeout = Duration.Seconds(30),
                Runtime = Runtime.DOTNET_6,
                Handler = "dynamodb-lambda::dynamodb_lambda.Function::FunctionHandler",
                Role = lambdaIAMRole,                
                Code = Code.FromAsset("../lambda/dynamodb-lambda/", new Amazon.CDK.AWS.S3.Assets.AssetOptions
                {
                    Bundling = buildOption
                })
            });
            
            lambdaFunction.AddEventSource(new DynamoEventSource(dynamoDbTable, new DynamoEventSourceProps
            {
                StartingPosition = StartingPosition.LATEST
            }));

            // CloudWatch Log Group
            var cloudWatchLogGroup = new LogGroup(this, "CloudWatchLogs", new LogGroupProps
            {
                LogGroupName = $"/aws/lambda/{lambdaFunctionName}",
                RemovalPolicy = RemovalPolicy.DESTROY,
                Retention = RetentionDays.ONE_DAY
            });

            //Grant Cloudwatch permission
            cloudWatchLogGroup.GrantWrite(lambdaFunction);
            //Grant DynamoDB stream read access
            dynamoDbTable.GrantStreamRead(lambdaIAMRole);
        }
    }
}