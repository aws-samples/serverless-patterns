using Amazon.CDK;
using Amazon.CDK.AWS.AppSync;
using Amazon.CDK.AWS.DynamoDB;
using Amazon.CDK.AWS.S3;
using Amazon.CDK.AWS.Lambda;
using Constructs;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using Amazon.CDK.AWS.Logs;
using Amazon.CDK.AWS.Glue.Alpha;
using Amazon.CDK.AWS.IAM;

namespace AppsyncLambdaDynamodbDotnetCdk
{
    public class AppsyncLambdaDynamodbDotnetCdkStack : Stack
    {
        public AppsyncLambdaDynamodbDotnetCdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // Create DynamoDB table for hot data
            var hotDataTable = new Amazon.CDK.AWS.DynamoDB.Table(this, "HotDataTable", new Amazon.CDK.AWS.DynamoDB.TableProps
            {
                PartitionKey = new Attribute { Name = "id", Type = AttributeType.STRING },
                BillingMode = BillingMode.PAY_PER_REQUEST,
                TableName = "hot-data-table",
                RemovalPolicy = RemovalPolicy.DESTROY,
                DeletionProtection = false,
                PointInTimeRecovery = false,
                Encryption = Amazon.CDK.AWS.DynamoDB.TableEncryption.AWS_MANAGED
            });

            // Create S3 bucket for cold data
            var coldDataBucket = new Bucket(this, "ColdDataBucket", new BucketProps
            {
                BucketName = "cold-data-bucket-" + Account + "-" + Region,
                Versioned = true,
                RemovalPolicy = RemovalPolicy.DESTROY,
                AutoDeleteObjects = true
            });

            // Create Glue Database
            var glueDatabase = new Database(this, "ColdDataDatabase", new DatabaseProps
            {
                DatabaseName = "cold_data_db"
            });

            // Create Glue Table
            var glueTable = new S3Table(this, "ColdDataTable", new S3TableProps
            {
                Database = glueDatabase,
                TableName = "cold_data_table",
                Columns =
                [
                    new Column { Name = "id", Type = Schema.STRING },
                    new Column { Name = "content", Type = Schema.STRING },
                    new Column { Name = "timestamp", Type = Schema.STRING }
                ],
                DataFormat = DataFormat.CSV,
                Bucket = coldDataBucket,
                S3Prefix = "data/",
                Compressed = false // Set this according to your data
            });

            // Build options for Lambda functions
            var buildOption = new BundlingOptions()
            {
                Image = Amazon.CDK.AWS.Lambda.Runtime.DOTNET_8.BundlingImage,
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

            // Create Lambda functions for resolvers
            var hotDataResolver = new Function(this, "HotDataResolver", new FunctionProps
            {
                Runtime = Amazon.CDK.AWS.Lambda.Runtime.DOTNET_8,
                MemorySize = 512,
                LogRetention = RetentionDays.ONE_DAY,
                Timeout = Duration.Seconds(30),
                Architecture = RuntimeInformation.ProcessArchitecture == System.Runtime.InteropServices.Architecture.X64
                    ? Amazon.CDK.AWS.Lambda.Architecture.X86_64
                    : Amazon.CDK.AWS.Lambda.Architecture.ARM_64,
                FunctionName = "HotDataResolver",
                Description = "Function to resolve hot data",
                Handler = "HotDataResolver",
                Code = Amazon.CDK.AWS.Lambda.Code.FromAsset(
                    "src/LambdaFunctions/HotDataResolver/src",
                    new Amazon.CDK.AWS.S3.Assets.AssetOptions
                    {
                        Bundling = buildOption
                    }),
                Environment = new Dictionary<string, string>
                {
                    ["HOT_DATA_TABLE"] = hotDataTable.TableName
                }
            });

            var coldDataResolver = new Function(this, "ColdDataResolver", new FunctionProps
            {
                Runtime = Amazon.CDK.AWS.Lambda.Runtime.DOTNET_8,
                MemorySize = 512,
                LogRetention = RetentionDays.ONE_DAY,
                Timeout = Duration.Seconds(30),
                Architecture = RuntimeInformation.ProcessArchitecture == System.Runtime.InteropServices.Architecture.X64
                    ? Amazon.CDK.AWS.Lambda.Architecture.X86_64
                    : Amazon.CDK.AWS.Lambda.Architecture.ARM_64,
                FunctionName = "ColdDataResolver",
                Description = "Function to handle cold data requests",
                Handler = "ColdDataResolver",
                Code = Amazon.CDK.AWS.Lambda.Code.FromAsset(
                    "src/LambdaFunctions/ColdDataResolver/src",
                    new Amazon.CDK.AWS.S3.Assets.AssetOptions
                    {
                        Bundling = buildOption
                    }),
                Environment = new Dictionary<string, string>
                {
                    ["COLD_DATA_BUCKET"] = coldDataBucket.BucketName,
                    ["GLUE_DATABASE"] = glueDatabase.DatabaseName,
                    ["GLUE_TABLE"] = glueTable.TableName
                }
            });

            // Grant permissions
            hotDataTable.GrantReadWriteData(hotDataResolver);
            coldDataBucket.GrantReadWrite(coldDataResolver);

            // Grant Athena permissions to the Cold Data Resolver
            coldDataResolver.AddToRolePolicy(new PolicyStatement(new PolicyStatementProps
            {
                Actions = [
                    "athena:StartQueryExecution", 
                    "athena:GetQueryExecution", 
                    "athena:GetQueryResults"
                ],
                Resources = ["*"]
            }));

            // Grant Glue permissions to the Cold Data Resolver
            coldDataResolver.AddToRolePolicy(new PolicyStatement(new PolicyStatementProps
            {
                Actions = [
                    "glue:GetTable",
                    "glue:GetPartitions",
                    "glue:GetDatabase"
                ],
                Resources = [
                    glueDatabase.DatabaseArn,
                    glueTable.TableArn,
                    Arn.Format(new ArnComponents  // Permission for Glue Catalog
                    {
                        Service = "glue",
                        Resource = "catalog",
                        Account = Account
                    }, this)
                ]
            }));

            // Grant Athena permission to write to the results bucket
            coldDataBucket.AddToResourcePolicy(new PolicyStatement(new PolicyStatementProps
            {
                Effect = Effect.ALLOW,
                Actions = ["s3:PutObject"],
                Principals = [new ServicePrincipal("athena.amazonaws.com")],
                Resources = [coldDataBucket.BucketArn, coldDataBucket.ArnForObjects("*")]
            }));

            // Create AppSync API
            var api = new GraphqlApi(this, "HotColdDataApi", new GraphqlApiProps
            {
                Name = "HotColdDataApi",
                Definition = Definition.FromFile("./src/AppsyncLambdaDynamodbDotnetCdk/graphql/schema.graphql"),
                AuthorizationConfig = new AuthorizationConfig
                {
                    DefaultAuthorization = new AuthorizationMode
                    {
                        AuthorizationType = AuthorizationType.API_KEY
                    }
                }
            });

            // Create data sources
            var hotDataSource = api.AddLambdaDataSource("HotDataSource", hotDataResolver);
            var coldDataSource = api.AddLambdaDataSource("ColdDataSource", coldDataResolver);

            // Create resolvers
            hotDataSource.CreateResolver(
                "getHotData",
                new ResolverProps
                {
                    TypeName = "Query",
                    FieldName = "getHotData",
                    RequestMappingTemplate = MappingTemplate.FromFile("./src/AppsyncLambdaDynamodbDotnetCdk/graphql/getHotData.request.vtl"),
                    ResponseMappingTemplate = MappingTemplate.FromFile("./src/AppsyncLambdaDynamodbDotnetCdk/graphql/getHotData.response.vtl")
                });

            coldDataSource.CreateResolver(
                "getColdData",
                new ResolverProps
                {
                    TypeName = "Query",
                    FieldName = "getColdData",
                    RequestMappingTemplate = MappingTemplate.FromFile("./src/AppsyncLambdaDynamodbDotnetCdk/graphql/getColdData.request.vtl"),
                    ResponseMappingTemplate = MappingTemplate.FromFile("./src/AppsyncLambdaDynamodbDotnetCdk/graphql/getColdData.response.vtl")
                });

            // Output the API URL and API Key
            _ = new CfnOutput(this, "GraphQLApiUrl", new CfnOutputProps
            {
                Value = api.GraphqlUrl,
                Description = "GraphQL API URL"
            });

            _ = new CfnOutput(this, "GraphQLApiKey", new CfnOutputProps
            {
                Value = api.ApiKey,
                Description = "GraphQL API Key"
            });

            _ = new CfnOutput(this, "HotDataTableName", new CfnOutputProps
            {
                Value = hotDataTable.TableName,
                Description = "Hot Data Table Name"
            });

            _ = new CfnOutput(this, "ColdDataBucketName", new CfnOutputProps
            {
                Value = coldDataBucket.BucketName,
                Description = "Cold Data Bucket Name"
            });

            _ = new CfnOutput(this, "GlueDatabaseName", new CfnOutputProps
            {
                Value = glueDatabase.DatabaseName,
                Description = "Glue Database Name"
            });

            _ = new CfnOutput(this, "GlueTableName", new CfnOutputProps
            {
                Value = glueTable.TableName,
                Description = "Glue Table Name"
            });

            _ = new CfnOutput(this, "HotDataResolverName", new CfnOutputProps
            {
                Value = hotDataResolver.FunctionName,
                Description = "Hot Data Resolver Name"
            });

            _ = new CfnOutput(this, "ColdDataResolverName", new CfnOutputProps
            {
                Value = coldDataResolver.FunctionName,
                Description = "Cold Data Resolver Name"
            });

            _ = new CfnOutput(this, "HotDataResolverArn", new CfnOutputProps
            {
                Value = hotDataResolver.FunctionArn,
                Description = "Hot Data Resolver ARN"
            });

            _ = new CfnOutput(this, "ColdDataResolverArn", new CfnOutputProps
            {
                Value = coldDataResolver.FunctionArn,
                Description = "Cold Data Resolver ARN"
            });
        }
    }
}