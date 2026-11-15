using System.Collections.Generic;
using AlbEcsBedrockAgentsCdkDotnet.BedrockAgent;
using AlbEcsBedrockAgentsCdkDotnet.ECS;
using Amazon.CDK;
using Constructs;

namespace AlbEcsBedrockAgentsCdkDotnet
{
    /// <summary>
    /// Class to define the stack for the Bedrock Agent with Knowledge Base and ECS service with ALB
    /// </summary>
    public class AlbEcsBedrockAgentsCdkDotnetStack : Stack
    {   
        /// <summary>
        /// Initializes a new instance of the <see cref="AlbEcsBedrockAgentsCdkDotnetStack"/> class.
        /// </summary>
        /// <param name="scope"><see cref="Construct"/></param>
        /// <param name="id">Stack Name</param>
        /// <param name="props">Stack properties</param>
        internal AlbEcsBedrockAgentsCdkDotnetStack(Construct scope, string id, IStackProps props = null) 
            : base(scope, id, props)
        {
            // Create Bedrock agent with Knowledge Base and Action Group
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

            // Create Fargate-based ECS service with Application Load Balancer
            var albEcsStack = new AlbEcsStack(
                this,
                "AlbEcsStack",
                new NestedStackProps
                {
                    Description = "Nested stack to create an ECS Cluster with an ALB",
                    RemovalPolicy = RemovalPolicy.DESTROY,
                    Timeout = Duration.Minutes(30),
                    Parameters = new Dictionary<string, string> 
                    {
                        { "AgentId", bedrockAgentWithKnowledgeBaseStack.BedrockAgent.AttrAgentId },
                        { "AgentAliasId", bedrockAgentWithKnowledgeBaseStack.AgentAliasId }
                    }                  
                });

            // Output the Agent Name
            _ = new CfnOutput(this, "AgentName", new CfnOutputProps
            {
                Description = "Bedrock Agent Name",
                Value = bedrockAgentWithKnowledgeBaseStack.BedrockAgent.AgentName
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

            // Output the Knowledge Base Name
            _ = new CfnOutput(this, "KnowledgeBaseName", new CfnOutputProps
            {
                Description = "Knowledge Base Name",
                Value = bedrockAgentWithKnowledgeBaseStack.KnowledgeBase.Name
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

            // Output ALB's Endpoint
            _ = new CfnOutput(this, "AlbEndpoint", new CfnOutputProps
            {
                Description = "Application Load Balancer Endpoint",
                Value = $"http://{albEcsStack.ApplicationLoadBalancer.LoadBalancerDnsName}"
            });
        }
    }
}
