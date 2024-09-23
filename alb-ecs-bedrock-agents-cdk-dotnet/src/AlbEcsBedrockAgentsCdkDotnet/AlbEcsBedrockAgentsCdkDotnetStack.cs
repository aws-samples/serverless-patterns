using System.Collections.Generic;
using AlbEcsBedrockAgentsCdkDotnet.BedrockAgent;
using Amazon.CDK;
using Constructs;

namespace AlbEcsBedrockAgentsCdkDotnet
{
    public class AlbEcsBedrockAgentsCdkDotnetStack : Stack
    {
        internal AlbEcsBedrockAgentsCdkDotnetStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            var bedrockAgentWithKnowledgeBaseStack = new BedrockAgentKnowledgeBaseStack(
                this, 
                "BedrockAgentWithKnowledgeBaseStack", 
                new NestedStackProps
                {
                    Description = "Nested stack to create a Bedrock Agent with a Knowledge Base and Vector Database",
                    RemovalPolicy = RemovalPolicy.DESTROY,
                    Timeout = Duration.Minutes(30),
                    Parameters = new Dictionary<string, string> {}
                });


            // Output the Agent ID
            _ = new CfnOutput(this, "AgentId", new CfnOutputProps
            {
                Description = "Bedrock Agent ID",
                Value = bedrockAgentWithKnowledgeBaseStack.BedrockAgent.AttrAgentId
            });

            // Outpuit Agent Alias Id
            _ = new CfnOutput(this, "AgentAliasId", new CfnOutputProps
            {
                Description = "Bedrock Agent Alias ID",
                Value = bedrockAgentWithKnowledgeBaseStack.AgentAliasId
            });

            // Output the Knowledge Base ID
            _ = new CfnOutput(this, "KnowledgeBaseId", new CfnOutputProps
            {
                Description = "Knowledge Base ID",
                Value = bedrockAgentWithKnowledgeBaseStack.KnowledgeBase.AttrKnowledgeBaseId
            });

            // Output OSS Collection Endpoint
            _ = new CfnOutput(this, "OssCollectionEndpoint", new CfnOutputProps
            {
                Description = "OSS Collection Endpoint",
                Value = bedrockAgentWithKnowledgeBaseStack.OssCollection.AttrDashboardEndpoint
            });

            // Output Knowledge Base S3 Bucket
            _ = new CfnOutput(this, "KnowledgeBaseBucket", new CfnOutputProps
            {
                Description = "Knowledge Base S3 Bucket",
                Value = bedrockAgentWithKnowledgeBaseStack.KnowledgeBaseBucket.BucketName
            });

            // Output Knowledge Base Data Source
            _ = new CfnOutput(this, "KnowledgeBaseDataSource", new CfnOutputProps
            {
                Description = "Knowledge Base Data Source",
                Value = bedrockAgentWithKnowledgeBaseStack.KnowledgeBaseDataSource.AttrDataSourceId
            });
        }
    }
}
