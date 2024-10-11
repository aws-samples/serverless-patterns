using AlbEcsBedrockAgentsCdkDotnet.BedrockAgent.ActionGroup;
using AlbEcsBedrockAgentsCdkDotnet.BedrockAgent.KnowledgeBase;
using Amazon.CDK;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.OpenSearchServerless;
using Amazon.CDK.AWS.S3;
using Amazon.CDK.AwsBedrock;
using Constructs;

namespace AlbEcsBedrockAgentsCdkDotnet.BedrockAgent;

internal sealed class BedrockAgentKnowledgeBaseStack : NestedStack
{
    private readonly BedrockKnowledgeBaseCdk _bedrockKnowledgeBaseCdk;
    private readonly BedrockAgentCdk _bedrockAgentCdk;

    /// <summary>
    /// Initializes a new instance of <see cref="BedrockAgentKnowledgeBaseStack"/>
    /// </summary>
    /// <param name="scope"><see cref="Construct"/></param>
    /// <param name="id">Stack Name</param>
    /// <param name="props">Nested stack properties</param>        
    internal BedrockAgentKnowledgeBaseStack(Construct scope, string id, INestedStackProps props = null)
        : base(scope, id, props)
    {
        // Create a knowledge base
        _bedrockKnowledgeBaseCdk = new BedrockKnowledgeBaseCdk(this);
        KnowledgeBase = _bedrockKnowledgeBaseCdk.CreateKnowledgeBase();

        // Create a Bedrock Agent
        _bedrockAgentCdk = new BedrockAgentCdk(this, KnowledgeBase);
        BedrockAgent = _bedrockAgentCdk.CreateBedrockAgent();

        // Add dependencies to make sure knowledge base is created and sync'ed before agent
        BedrockAgent.Node.AddDependency(_bedrockKnowledgeBaseCdk.KnowledgeBaseSyncCustomResource);
    }
    
    /// <summary>
    /// Gets Bedrock Knowledge Base
    /// </summary>
    /// <value><see cref="CfnKnowledgeBase"/></value>
    internal CfnKnowledgeBase KnowledgeBase { get; }

    /// <summary>
    /// Gets OpenSearch Serverless Collection
    /// </summary>
    /// <value><see cref="CfnCollection"/></value>
    internal CfnCollection OssCollection => _bedrockKnowledgeBaseCdk.OssCollection;

    /// <summary>
    /// Gets Knowledge Base S3 Bucket
    /// </summary>
    /// <value><see cref="Bucket"/></value>
    internal Bucket KnowledgeBaseBucket => _bedrockKnowledgeBaseCdk.KnowledgeBaseBucket;

    /// <summary>
    /// Gets Knowledge Base Data Source
    /// </summary>
    /// <value><see cref="CfnDataSource"/></value>
    internal CfnDataSource KnowledgeBaseDataSource => _bedrockKnowledgeBaseCdk.KnowledgeBaseDataSource;

    /// <summary>
    /// Gets Knowledge Base Sync Custom Resource
    /// </summary>
    /// <value><see cref="CustomResource"/></value>
    internal CustomResource KnowledgeBaseSyncCustomResource => _bedrockKnowledgeBaseCdk.KnowledgeBaseSyncCustomResource;

    /// <summary>
    /// Gets Bedrock Agent
    /// </summary>
    /// <value><see cref="CfnAgent"/></value>
    internal CfnAgent BedrockAgent { get; }

    /// <summary>
    /// Gets Action Group Lambda Function
    /// </summary>
    /// <value>Lambda Function</value>
    internal Function ActionGroupLambdaFunction => _bedrockAgentCdk.ActionGroupLambdaFunction;

    /// <summary>
    /// Gets Create Agent Alias Custom Resource
    /// </summary>
    /// <value>Custom Resource</value>
    internal CustomResource CreateAgentAliasCustomResource => _bedrockAgentCdk.CreateAgentAliasCustomResource;

    /// <summary>
    /// Gets Agent Alias Id
    /// </summary>
    /// <value>AliasId</value>
    internal string AgentAliasId => _bedrockAgentCdk.AgentAliasId;

    /// <summary>
    /// Gets Agent Alias Arn
    /// </summary>
    /// <value>Agent Alias ARN</value>
    internal string AgentAliasArn => _bedrockAgentCdk.AgentAliasArn;
}