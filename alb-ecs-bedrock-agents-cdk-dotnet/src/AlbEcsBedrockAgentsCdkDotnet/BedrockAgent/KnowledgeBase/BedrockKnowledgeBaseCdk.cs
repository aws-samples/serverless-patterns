using System.Collections.Generic;
using System.IO;
using System.Runtime.InteropServices;
using AlbEcsBedrockAgentsCdkDotnet.Common;
using Amazon.CDK;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.OpenSearchServerless;
using Amazon.CDK.AWS.S3;
using Amazon.CDK.AwsBedrock;
using Newtonsoft.Json.Linq;

namespace AlbEcsBedrockAgentsCdkDotnet.BedrockAgent.KnowledgeBase;

/// <summary>
/// This class provides the functionality to create Bedrock Knowledge Base
/// </summary>
internal sealed class BedrockKnowledgeBaseCdk
{
    private readonly Stack _stack;
    private readonly string _kbRoleName;

    /// <summary>
    /// Initializes a new instance of <see cref="BedrockKnowledgeBaseCdk"/>
    /// </summary>
    /// <param name="stack">CDK <see cref="Stack"/></param>
    internal BedrockKnowledgeBaseCdk(Stack stack)
    {
        _stack = stack;

        // Role name for the Knowledge Base
        _kbRoleName = "AmazonBedrockExecutionRoleForKnowledgeBase_" + Utils.GenerateRandomStringFromStackId(_stack.StackId);
    }

    /// <summary>
    /// Gets OpenSearch Serverless Collection
    /// </summary>
    /// <value><see cref="CfnCollection"/></value>
    internal CfnCollection OssCollection { get; private set; }

    /// <summary>
    /// Gets Knowledge Base S3 Bucket
    /// </summary>
    /// <value><see cref="Bucket"/></value>
    internal Bucket KnowledgeBaseBucket { get; private set; }

    /// <summary>
    /// Gets Knowledge Base
    /// </summary>
    /// <value><see cref="CfnKnowledgeBase"/></value>
    internal CfnKnowledgeBase KnowledgeBase { get; private set; }

    /// <summary>
    /// Gets Knowledge Base Data Source
    /// </summary>
    /// <value><see cref="CfnDataSource"/></value>
    internal CfnDataSource KnowledgeBaseDataSource { get; private set; }

    /// <summary>
    /// Gets Knowledge Base Sync Custom Resource
    /// </summary>
    /// <value><see cref="CustomResource"/></value>
    internal CustomResource KnowledgeBaseSyncCustomResource { get; private set; }

    /// <summary>
    /// Creates Knowledge Base
    /// </summary>
    /// <returns><see cref="CfnKnowledgeBase"/></returns>
    internal CfnKnowledgeBase CreateKnowledgeBase()
    {
        // Index creation Lambda function for OSS
        var indexCreateLambdaFunction = CreateLambdaFunctionForIndexCreation();

        // Create OpenSearch Serverless Collection for Bedrock KB's Vector Data
        OssCollection = CreateOpenSearchServerlessCollection(indexCreateLambdaFunction.Role.RoleArn);

        // Create an Index in OpenSearch Serverless using a custom resource
        var indexCreationCustomResource = CreateOssVectorIndexUsingCustomResource(indexCreateLambdaFunction);

        // Create S3 bucket for the Knowledge Base data
        KnowledgeBaseBucket = CreateKnowledgeBaseS3Bucket();

        // Create a Knowledge Base for Bedrock Agents
        KnowledgeBase = CreateKnowledgeBaseForBedrockAgents();

        // Add dependencies to the Knowledge Base to wait for Index Creation Lambda to complete
        KnowledgeBase.Node.AddDependency(indexCreationCustomResource);

        // Create a data source for the Knowledge Base
        KnowledgeBaseDataSource = CreateKnowledgeBaseDataSource();

        // Upload documents to the Knowledge Base and Sync the data source
        KnowledgeBaseSyncCustomResource = PrepareKnowledgeBase();

        // Return Knowledge Base
        return KnowledgeBase;
    }

    /// <summary>
    /// Creates OpenSearch Serverless Collection
    /// </summary>
    /// <returns><see cref="CfnCollection"/></returns>
    private CfnCollection CreateOpenSearchServerlessCollection(string createIndexLambdaFunctionRoleArn)
    {
        // Create an OpenSearch Serverless Collection
        var ossCollection = new CfnCollection(
            _stack, 
            "ChatBotBedrockKnowledgeBaseOpenSearchServerlessCollection", 
            new CfnCollectionProps
            {
                Name = $"chatbot-bedrock-kb-{Utils.GenerateRandomStringFromStackId(_stack.StackId)}",
                Description = "Collection for Bedrock Agents vector embeddings",
                Type = "VECTORSEARCH",
                StandbyReplicas = "DISABLED"
            });

        var ossPoliciesFilePath = Path.Combine("./src/AlbEcsBedrockAgentsCdkDotnet/BedrockAgent/KnowledgeBase/opensearch-policies.json");
        var policiesJson = File.ReadAllText(ossPoliciesFilePath);
        var policies = JObject.Parse(policiesJson);

        // Network Policy
        var networkPolicy = new CfnSecurityPolicy(
            _stack, 
            "ChatBotOssNetworkPolicy", 
            new CfnSecurityPolicyProps
            {
                Name = $"chatbot-bedrock-kb-{Utils.GenerateRandomStringFromStackId(_stack.StackId)}",
                Type = "network",
                Description = "Custom network policy created by Amazon Bedrock Knowledge Base service to allow a created IAM role " +
                              "to have permissions on Amazon Open Search collections and indexes.",
                Policy = Fn.Sub(
                    policies["networkPolicy"].ToString(),
                    new Dictionary<string, string>
                    {
                        { "CollectionName", ossCollection.Name }
                    })
            });

        // Encryption Policy
        var encryptionPolicy = new CfnSecurityPolicy(
            _stack, 
            "ChatBotOssEncryptionPolicy", 
            new CfnSecurityPolicyProps
            {
                Name = $"chatbot-bedrock-kb-{Utils.GenerateRandomStringFromStackId(_stack.StackId)}",
                Type = "encryption",
                Description = "Custom encryption policy created by Amazon Bedrock Knowledge Base service to allow a created IAM role " + 
                               "to have permissions on Amazon Open Search collections and indexes.",
                Policy = Fn.Sub(
                    policies["encryptionPolicy"].ToString(),
                    new Dictionary<string, string>
                    {
                        { "CollectionName", ossCollection.Name }
                    })
            });

        // Access Policy
        var accessPolicy = new CfnAccessPolicy(
            _stack, 
            "ChatBotOssAccessPolicy", 
            new CfnAccessPolicyProps
            {
                Name = $"chatbot-bedrock-kb-{Utils.GenerateRandomStringFromStackId(_stack.StackId)}",
                Type = "data",
                Description = "Custom data access policy created by Amazon Bedrock Knowledge Base service to allow a created IAM role " +
                              "to have permissions on Amazon Open Search collections and indexes.",
                Policy = Fn.Sub(
                    policies["dataAccessPolicy"].ToString(),
                    new Dictionary<string, string>
                    {
                        { "CollectionName", ossCollection.Name },
                        { "BedrockRoleArn",  $"arn:aws:iam::{_stack.Account}:role/service-role/{_kbRoleName}" },
                        { "CreateIndexLambdaFunctionRoleArn", createIndexLambdaFunctionRoleArn }
                    })
            });

        ossCollection.AddDependency(networkPolicy);
        ossCollection.AddDependency(encryptionPolicy);
        ossCollection.AddDependency(accessPolicy);

        return ossCollection;
    }

    /// <summary>
    /// Creates an Index in OpenSearch Serverless using a custom resource
    /// </summary>
    /// <param name="indexCreateLambdaFunction">Lambda function to create index</param>
    /// <returns><see cref="CustomResource"/></returns>
    private CustomResource CreateOssVectorIndexUsingCustomResource(Function indexCreateLambdaFunction)
    {
        // Grant permissions to Index Creation Lambda on AOSS
        indexCreateLambdaFunction.AddToRolePolicy(
            new PolicyStatement(
                new PolicyStatementProps
                {
                    Sid = "OpenSearchServerlessAPIAccessAllStatement",
                    Effect = Effect.ALLOW,
                    Actions = ["aoss:APIAccessAll"],
                    Resources = [OssCollection.AttrArn]
                })); 

        // Create custom resource to invoke Index Creation Lambda
        return new CustomResource(
            _stack, 
            "ChatBotIndexCreationCustomResource", 
            new CustomResourceProps
            {
                ServiceToken = indexCreateLambdaFunction.FunctionArn,
                Properties = new Dictionary<string, object>
                {
                    ["Region"] = _stack.Region,
                    ["AOSSHost"] = OssCollection.AttrCollectionEndpoint,
                    ["AOSSIndexName"] = Constants.Bedrock_KB_AOSS_IndexName,
                    ["AOSSMetadataFieldName"] = Constants.Bedrock_KB_AOSS_MetadataField_Name,
                    ["AOSSTextFieldName"] = Constants.Bedrock_KB_AOSS_TextField_Name,
                    ["AOSSVectorFieldName"] = Constants.Bedrock_KB_AOSS_VectorField_Name
                }
            });        
    }
    
    /// <summary>
    /// Creates S3 bucket for the Knowledge Base data
    /// </summary>
    /// <returns><see cref="Bucket"/></returns>
    private Bucket CreateKnowledgeBaseS3Bucket()
    {
        return new Bucket(
            _stack, 
            "ChatBotBedrockKnowledgeBaseBucket", 
            new BucketProps
            {
                BucketName = $"chatbot-bedrock-knowledge-base-{Utils.GenerateRandomStringFromStackId(_stack.StackId)}",
                Versioned = true,
                Encryption = BucketEncryption.S3_MANAGED,
                RemovalPolicy = RemovalPolicy.DESTROY, // Be cautious with this in production
                AutoDeleteObjects = true, // Be cautious with this in production
            });
    }

    /// <summary>
    /// Creates a Knowledge Base for Bedrock Agents
    /// </summary>
    /// <returns><see cref="CfnKnowledgeBase"/></returns>
    private CfnKnowledgeBase CreateKnowledgeBaseForBedrockAgents()
    {
        // Create an IAM role for the Knowledge Base
        var kbRole = CreateRoleForKnowledgeBaseForBedrockAgent();

        return new CfnKnowledgeBase(
            _stack, 
            "ChatBotBedrockKnowledgeBase", 
            new CfnKnowledgeBaseProps
            {
                Name = $"bedrock-knowledge-base-{Utils.GenerateRandomStringFromStackId(_stack.StackId)}",
                Description = "Knowledge base for my Bedrock Agent",
                RoleArn = kbRole.RoleArn,
                KnowledgeBaseConfiguration = new CfnKnowledgeBase.KnowledgeBaseConfigurationProperty
                {
                    Type = "VECTOR",
                    VectorKnowledgeBaseConfiguration = new CfnKnowledgeBase.VectorKnowledgeBaseConfigurationProperty
                    {
                        EmbeddingModelArn =  Utils.GetTitanV2FMArn(_stack.Region),
                    }
                },
                StorageConfiguration = new CfnKnowledgeBase.StorageConfigurationProperty
                {
                    Type = "OPENSEARCH_SERVERLESS",
                    OpensearchServerlessConfiguration = new CfnKnowledgeBase.OpenSearchServerlessConfigurationProperty
                    {
                        CollectionArn = OssCollection.AttrArn,
                        VectorIndexName = Constants.Bedrock_KB_AOSS_IndexName,
                        FieldMapping = new CfnKnowledgeBase.OpenSearchServerlessFieldMappingProperty
                        {
                            MetadataField = Constants.Bedrock_KB_AOSS_MetadataField_Name,
                            TextField = Constants.Bedrock_KB_AOSS_TextField_Name,
                            VectorField = Constants.Bedrock_KB_AOSS_VectorField_Name,
                        },
                    }
                }
            });
    }

    /// <summary>
    /// Creates an IAM role for the Knowledge Base
    /// </summary>
    /// <returns><see cref="Role"/></returns>
    private Role CreateRoleForKnowledgeBaseForBedrockAgent()
    {
        // Create an IAM role for the Knowledge Base
        var kbRole = new Role(
            _stack, 
            "ChatBotBedrockKnowledgeBaseRole",
            new RoleProps
            {
                RoleName = _kbRoleName,
                Path = "/service-role/",
                Description = "Bedrock Knowledge Base access",
                AssumedBy = new ServicePrincipal(
                    "bedrock.amazonaws.com",
                    new ServicePrincipalOpts
                    {
                        Conditions = new Dictionary<string, object>
                        {
                            ["StringEquals"] = new Dictionary<string, string>
                            {
                                ["aws:SourceAccount"] = _stack.Account,
                            },
                            ["ArnLike"] = new Dictionary<string, string>
                            {
                                ["aws:SourceArn"] = $"arn:aws:bedrock:{_stack.Region}:{_stack.Account}:knowledge-base/*"
                            }
                        }
                    }),
                MaxSessionDuration = Duration.Minutes(60),
                InlinePolicies = new Dictionary<string, PolicyDocument>
                {
                    // Access to Foundation Models
                    ["AmazonBedrockFoundationModelPolicyForKnowledgeBase_" + Utils.GenerateRandomStringFromStackId(_stack.StackId)] = 
                        new PolicyDocument(new PolicyDocumentProps
                        {
                            Statements =
                            [
                                new PolicyStatement(
                                    new PolicyStatementProps
                                    {
                                        Sid = "BedrockInvokeModelStatement",
                                        Effect = Effect.ALLOW,
                                        Actions = ["bedrock:InvokeModel"],
                                        Resources = [
                                            Utils.GetTitanV2FMArn(_stack.Region),
                                            Utils.GetCluade3HaikuFMArn(_stack.Region),
                                            Utils.GetCluade35HaikuFMArn(_stack.Region)
                                        ]
                                    })                            
                            ]
                        }),

                    // Policy to allow access to OpenSearch Serverless
                    ["AmazonBedrockOSSPolicyForKnowledgeBase_" + Utils.GenerateRandomStringFromStackId(_stack.StackId)] = 
                        new PolicyDocument(new PolicyDocumentProps
                        {
                            Statements =
                            [
                                new PolicyStatement(
                                    new PolicyStatementProps
                                    {
                                        Sid = "OpenSearchServerlessAPIAccessAllStatement",                                
                                        Effect = Effect.ALLOW,
                                        Actions =
                                        [
                                            "aoss:APIAccessAll"
                                        ],
                                        Resources = [
                                            OssCollection.AttrArn
                                        ]
                                    }),
                            ]
                        }),

                    ["AmazonBedrockS3PolicyForKnowledgeBase_" + Utils.GenerateRandomStringFromStackId(_stack.StackId)] = 
                        new PolicyDocument(new PolicyDocumentProps
                        {
                            Statements =
                            [
                                new PolicyStatement(
                                    new PolicyStatementProps
                                    {
                                        Sid = "S3ListBucketStatement",
                                        Effect = Effect.ALLOW,
                                        Actions = ["s3:ListBucket"],
                                        Resources = [KnowledgeBaseBucket.BucketArn],
                                        Conditions = new Dictionary<string, object>
                                        {
                                            ["StringEquals"] = new Dictionary<string, string>
                                            {
                                                ["aws:ResourceAccount"] = _stack.Account
                                            }
                                        }
                                    }),
                                new PolicyStatement(
                                    new PolicyStatementProps
                                    {
                                        Sid = "S3GetObjectStatement",
                                        Effect = Effect.ALLOW,
                                        Actions = ["s3:GetObject"],
                                        Resources = [KnowledgeBaseBucket.BucketArn + "/*"],
                                        Conditions = new Dictionary<string, object>
                                        {
                                            ["StringEquals"] = new Dictionary<string, string>
                                            {
                                                ["aws:ResourceAccount"] = _stack.Account
                                            }
                                        }
                                    }
                                )
                            ]
                        })
                }
            });

        return kbRole;
    }

    /// <summary>
    /// Creates a data source for the Knowledge Base
    /// </summary>
    /// <returns><see cref="CfnDataSource"/></returns>
    private CfnDataSource CreateKnowledgeBaseDataSource()
    {
        return new CfnDataSource(
            _stack, 
            "ChatBotBedrockKnowledgeBaseDataSource", 
            new CfnDataSourceProps
            {
                DataDeletionPolicy = "DELETE",
                Description = "Data source for Bedrock Knowledge Base",
                KnowledgeBaseId = KnowledgeBase.AttrKnowledgeBaseId,
                Name = $"chatbot-bedrock-knowledge-base-datasource-{Utils.GenerateRandomStringFromStackId(_stack.StackId)}",
                VectorIngestionConfiguration = new CfnDataSource.VectorIngestionConfigurationProperty
                {
                    ChunkingConfiguration = new CfnDataSource.ChunkingConfigurationProperty
                    {
                        ChunkingStrategy = "FIXED_SIZE",
                        FixedSizeChunkingConfiguration = new CfnDataSource.FixedSizeChunkingConfigurationProperty
                        {
                            MaxTokens = 300,
                            OverlapPercentage = 20
                        }
                    },
                    ParsingConfiguration = new CfnDataSource.ParsingConfigurationProperty
                    {
                        ParsingStrategy = "BEDROCK_FOUNDATION_MODEL",
                        BedrockFoundationModelConfiguration = new CfnDataSource.BedrockFoundationModelConfigurationProperty
                        {
                            ModelArn = Utils.GetCluade3HaikuFMArn(_stack.Region),
                            ParsingPrompt = new CfnDataSource.ParsingPromptProperty
                            {
                                ParsingPromptText = "You have access to GlobalTrek Adventures' policies and travel info. Use this to answer questions accurately. If unsure, say you'll check."
                            }
                        }
                    },
                },
                DataSourceConfiguration = new CfnDataSource.DataSourceConfigurationProperty
                {
                    Type = "S3",
                    S3Configuration = new CfnDataSource.S3DataSourceConfigurationProperty
                    {
                        BucketArn = KnowledgeBaseBucket.BucketArn,
                        BucketOwnerAccountId = _stack.Account
                    }
                }   
            });
    }

    /// <summary>
    /// Creates a custom resource to prepare the Knowledge Base for Bedrock Agent
    /// </summary>
    /// <returns><see cref="CustomResource"/></returns>    
    private CustomResource PrepareKnowledgeBase()
    {
        // Create lambda function for Bedrock Agent's knowledge base sync
        var knowledgeBaseSynclambdaFunction = CreateLambdaFunctionForBedrockAgentKnowledgeBaseSync();

        // Create custom resource to invoke Policy Document Ingestion and Data source sync
        return new CustomResource(
            _stack, 
            "ChatBotKnowledgeBasePrepareCustomResource", 
            new CustomResourceProps
            {
                ServiceToken = knowledgeBaseSynclambdaFunction.FunctionArn,
                Properties = new Dictionary<string, object>
                {
                    ["Region"] = _stack.Region,
                    ["KnowledgeBaseId"] = KnowledgeBase.AttrKnowledgeBaseId,
                    ["DataSourceId"] = KnowledgeBaseDataSource.AttrDataSourceId,
                    ["BucketName"] = KnowledgeBaseBucket.BucketName
                }
            });   
    } 

    /// <summary>
    /// Creates Lambda function for OpenSearch Serverless Index Creation
    /// </summary>
    /// <returns><see cref="Function"/></returns>
    private Function CreateLambdaFunctionForIndexCreation()
    { 
        // Create Lambda functions for resolvers
        var indexCreationLambda = new Function(
            _stack, 
            "ChatBotBedrockAgentsOssIndexCreationLambdaFunction", 
            new FunctionProps
            {
                FunctionName = $"chatbot-bedrock-knowledge-base-index-creation-{Utils.GenerateRandomStringFromStackId(_stack.StackId)}",
                Runtime = Runtime.DOTNET_8,
                MemorySize = 512,
                Timeout = Duration.Seconds(180),
                Architecture = RuntimeInformation.ProcessArchitecture == System.Runtime.InteropServices.Architecture.X64
                    ? Amazon.CDK.AWS.Lambda.Architecture.X86_64
                    : Amazon.CDK.AWS.Lambda.Architecture.ARM_64,
                Description = "Function to create OSS Index",
                Handler = "OssIndexCreation",
                Code = Code.FromAsset(
                    "src/LambdaFunctions/KnowledgeBase/CustomResource/OssIndexCreation",
                    new Amazon.CDK.AWS.S3.Assets.AssetOptions
                    {
                        Bundling = LambdaFunctionsCdkUtils.GetBuildingOptions()
                    })
            });

        return indexCreationLambda;
    }

    /// <summary>
    /// Creates Lambda function for Bedrock Agent's knowledge base data ingestion and sync
    /// </summary>
    /// <returns><see cref="Function"/></returns>
    private Function CreateLambdaFunctionForBedrockAgentKnowledgeBaseSync()
    { 
        // Create Lambda functions for resolvers
        var documentIngestionLambda = new Function(
            _stack, 
            "ChatBotBedrockAgentsKnowledgeBaseIngestionLambdaFunction", 
            new FunctionProps
            {
                FunctionName = $"chatbot-bedrock-knowledge-base-ingestion-{Utils.GenerateRandomStringFromStackId(_stack.StackId)}",
                Runtime = Runtime.DOTNET_8,
                MemorySize = 512,
                Timeout = Duration.Minutes(15),
                Architecture = RuntimeInformation.ProcessArchitecture == System.Runtime.InteropServices.Architecture.X64
                    ? Amazon.CDK.AWS.Lambda.Architecture.X86_64
                    : Amazon.CDK.AWS.Lambda.Architecture.ARM_64,
                Description = "Function to create OSS Index",
                Handler = "KnowledgeBaseIngestion",
                Code = Code.FromAsset(
                    "src/LambdaFunctions/KnowledgeBase/CustomResource/KnowledgeBaseIngestion",
                    new Amazon.CDK.AWS.S3.Assets.AssetOptions
                    {
                        Bundling = LambdaFunctionsCdkUtils.GetBuildingOptions()
                    })
            });

        // Grant permissions to Upload to S3 Bucket
        documentIngestionLambda.AddToRolePolicy(
            new PolicyStatement(
                new PolicyStatementProps
                {
                    Effect = Effect.ALLOW,
                    Actions = ["s3:PutObject"],
                    Resources = [
                        KnowledgeBaseBucket.BucketArn, 
                        KnowledgeBaseBucket.ArnForObjects("*")
                    ]
                }));

        // Grant permissions to Start and Get Ingestion Job
        documentIngestionLambda.AddToRolePolicy(
            new PolicyStatement(
                new PolicyStatementProps
                {
                    Effect = Effect.ALLOW,
                    Actions = [
                        "bedrock:StartIngestionJob",
                        "bedrock:GetIngestionJob",
                        "bedrock:ListIngestionJobs",
                    ],
                    Resources = [
                        KnowledgeBase.AttrKnowledgeBaseArn
                    ]
                }));

        return documentIngestionLambda;
    }
}