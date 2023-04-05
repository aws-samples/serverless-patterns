using Amazon.CDK;
using Amazon.CDK.AWS.DynamoDB;
using Amazon.CDK.AWS.Events;
using Amazon.CDK.AWS.Events.Targets;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Lambda;
using Constructs;

namespace Cdk
{
    public class CdkStack : Stack
    {
        private string tableName = "Users";
        private string functionName = "AddItemFunction";
        private string ruleName = "ScheduleAddItemFunction";

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

            // Create a DynamoDB Table
            // Note: RemovalPolicy.DESTROY will delete the DynamoDB table when you run cdk destroy command
            new Table(this, "Users", new TableProps
            {
                TableName = tableName,
                PartitionKey = new Attribute { Name = "Id", Type = AttributeType.STRING },
                RemovalPolicy = RemovalPolicy.DESTROY,
                TimeToLiveAttribute = "TTL"
            });

� � � � � � // Create Lambda execution role
� � � � � � Role lambdaExecutionRole = new Role(this, functionName + "-execution-role", new RoleProps
            {
                AssumedBy = new ServicePrincipal("lambda.amazonaws.com")
            });

� � � � � � // Add AWS Managed Policies
� � � � � � // Note: For demonstartion purpose DynamoDB Full access is provided.
� � � � � � // THIS IS NOT RECOMMENDED FOR PRODUCTION ENVIRONMENT
� � � � � � // Best practice is to provide least privilege access
� � � � � � lambdaExecutionRole.AddManagedPolicy(ManagedPolicy.FromAwsManagedPolicyName("service-role/AWSLambdaBasicExecutionRole"));
            lambdaExecutionRole.AddManagedPolicy(ManagedPolicy.FromAwsManagedPolicyName("AmazonDynamoDBFullAccess"));

� � � � � � // Create a Lambda function to add item to DynamoDB            
            Function addItemFunction = new Function(this, functionName, new FunctionProps
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

� � � � � � // Run every minute. NOTE: THIS SCHEDULE IS ONLY FOR DEMO PURPOSE
� � � � � � // Refer https://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html for more details
� � � � � � var rule = new Rule(this, "Rule", new RuleProps
            {
                RuleName = ruleName,
                Schedule = Schedule.Expression("cron(0/1 * ? * * *)"),
            });

            rule.AddTarget(new LambdaFunction(addItemFunction));
        }
    }
}