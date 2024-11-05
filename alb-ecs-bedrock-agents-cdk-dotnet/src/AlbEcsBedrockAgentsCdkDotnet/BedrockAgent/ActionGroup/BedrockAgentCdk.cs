using System.Collections.Generic;
using System.IO;
using System.Runtime.InteropServices;
using AlbEcsBedrockAgentsCdkDotnet.Common;
using Amazon.CDK;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AwsBedrock;

namespace AlbEcsBedrockAgentsCdkDotnet.BedrockAgent.ActionGroup;

/// <summary>
/// This class provides the functionality to create Bedrock Agent
/// </summary>
internal sealed class BedrockAgentCdk
{
    private readonly Stack _stack;
    private readonly CfnKnowledgeBase _knowledgeBase;

    /// <summary>
    /// Initializes a new instance of <see cref="Bedrock    AgentCdk"/>
    /// </summary>
    /// <param name="stack">CDK <see cref="Stack"/></param>
    /// <param name="knowledgeBase">Bedrock Knowledge Base(<see cref="CfnKnowledgeBase"/>)</param>
    internal BedrockAgentCdk(Stack stack, CfnKnowledgeBase knowledgeBase)
    {
        _stack = stack;
        _knowledgeBase = knowledgeBase;
    }

    /// <summary>
    /// Gets Bedrock Agent
    /// </summary>
    /// <value>Agent</value>
    internal CfnAgent BedrockAgent { get; private set; }

    /// <summary>
    /// Gets Action Group Lambda Function
    /// </summary>
    /// <value>Lambda Function</value>
    internal Function ActionGroupLambdaFunction { get; private set; }

    /// <summary>
    /// Gets Create Agent Alias Custom Resource
    /// </summary>
    /// <value>Custom Resource</value>
    internal CustomResource CreateAgentAliasCustomResource { get; private set; }

    /// <summary>
    /// Gets Agent Alias Id
    /// </summary>
    /// <value>AliasId</value>
    internal string AgentAliasId { get; private set; }

    /// <summary>
    /// Gets Agent Alias Arn
    /// </summary>
    /// <value>Agent Alias ARN</value>
    internal string AgentAliasArn { get; private set; }

    /// <summary>
    /// Create Bedrock Agent
    /// </summary>
    /// <returns><see cref="CfnAgent"/></returns>
    internal CfnAgent CreateBedrockAgent()
    {
        // Create lambda function for Bedrock Agent's action group
        ActionGroupLambdaFunction = CreateLambdaFunctionForBedrockAgents(_stack);

        // Create Bedrock Agent
        BedrockAgent = CreateBedrockAgent(ActionGroupLambdaFunction.FunctionArn);

        // Add resource-based policy to lambda function to allow Bedrock to invoke the Lambda function
        ActionGroupLambdaFunction.AddPermission(
            "ChatBotBedrockInvokePermission", 
            new Permission
            {
                Principal = new ServicePrincipal("bedrock.amazonaws.com"),
                Action = "lambda:InvokeFunction",
                SourceArn = BedrockAgent.AttrAgentArn
            });

        // Create Agent Alias
        CreateAgentAliasCustomResource = CreateAgentAlias();

        // Return Bedrock Agent
        return BedrockAgent;
    }

    /// <summary>
    /// Create Bedrock Agent
    /// </summary>
    /// <param name="lambdaFunctionArn">Action group lambda function</param>
    /// <returns><see cref="CfnAgent"/></returns>
    private CfnAgent CreateBedrockAgent(string lambdaFunctionArn)
    {
        // Create role for Bedrock Agent
        var agentRole = CreateRoleForBedrockAgent();

        // Read the API schema from file
        var apiSchemaContent = File.ReadAllText(Path.Combine("./src/AlbEcsBedrockAgentsCdkDotnet/BedrockAgent/ActionGroup/api-schema.json"));
        var promptContent = File.ReadAllText(Path.Combine("./src/AlbEcsBedrockAgentsCdkDotnet/BedrockAgent/ActionGroup/agent-prompt.txt"));

        return new CfnAgent(
            _stack, 
            "ChatBotBedrockAgent", 
            new CfnAgentProps
            {
                AgentName = $"chatbot-bedrock-agent-{Utils.GenerateRandomStringFromStackId(_stack.StackId)}",
                Description = "Bedrock Agent for GlobalTrek Adventures.",
                AgentResourceRoleArn = agentRole.RoleArn,
                Instruction = promptContent,
                IdleSessionTtlInSeconds = 300,
                FoundationModel = Constants.Bedrock_FoundationModel_Claude3_5_Haiku,
                KnowledgeBases = new[]
                {
                    new CfnAgent.AgentKnowledgeBaseProperty
                    {
                        KnowledgeBaseId = _knowledgeBase.AttrKnowledgeBaseId,
                        Description = "You have access to GlobalTrek Adventures' policies and travel info. Use this to answer questions accurately. If unsure, say you'll check.",
                        KnowledgeBaseState = "ENABLED"
                    }
                },
                ActionGroups = new[]
                {
                    new CfnAgent.AgentActionGroupProperty
                    {
                        ActionGroupName = $"chatbot-action-group-{Utils.GenerateRandomStringFromStackId(_stack.StackId)}",
                        Description = "Action group for Bedrccok Agent",
                        ActionGroupExecutor = new CfnAgent.ActionGroupExecutorProperty
                        {
                            Lambda = lambdaFunctionArn
                        },
                        ApiSchema = new CfnAgent.APISchemaProperty
                        {
                            Payload = apiSchemaContent
                        },
                        ActionGroupState = "ENABLED"
                    }
                },
                AutoPrepare = true,
                // GuardrailConfiguration = new CfnAgent.GuardrailConfigurationProperty
                // {
                //     GuardrailIdentifier = "bedrock-agent-guardrail",
                //     GuardrailVersion = "1.0",
                // },
                SkipResourceInUseCheckOnDelete = false
            });
    }

    /// <summary>
    /// Create role for Bedrock Agent
    /// </summary>
    /// <returns><see cref="Role"/></returns>
    private Role CreateRoleForBedrockAgent()
    {
        // Create an IAM role for the Knowledge Base
        var agentRole = new Role(
            _stack, 
            "ChatBotBedrockAgentRole", 
            new RoleProps
            {
                RoleName = "ChatBot_AmazonBedrockExecutionRoleForAgents_" + Utils.GenerateRandomStringFromStackId(_stack.StackId),
                Path = "/service-role/",
                Description = "Bedrock Agent Role",                
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
                                ["aws:SourceArn"] = $"arn:aws:bedrock:{_stack.Region}:{_stack.Account}:agent/*"
                            }
                        }
                    }),
                MaxSessionDuration = Duration.Minutes(60),
                InlinePolicies = new Dictionary<string, PolicyDocument>
                {
                    ["AmazonBedrockAgentBedrockFoundationModelPolicy_" + Utils.GenerateRandomStringFromStackId(_stack.StackId)] = 
                        new PolicyDocument(new PolicyDocumentProps
                        {
                            Statements =
                            [
                                new PolicyStatement(new PolicyStatementProps
                                {
                                    Sid = "AmazonBedrockAgentBedrockFoundationModelPolicyProd",
                                    Effect = Effect.ALLOW,
                                    Actions = ["bedrock:InvokeModel"],
                                    Resources = [Utils.GetCluade35HaikuFMArn(_stack.Region)],
                                })
                            ]
                        }),

                    ["AmazonBedrockAgentRetrieveKnowledgeBasePolicy_" + Utils.GenerateRandomStringFromStackId(_stack.StackId)] = 
                        new PolicyDocument(new PolicyDocumentProps
                        {
                            Statements =
                            [
                                new PolicyStatement(new PolicyStatementProps
                                {
                                    Sid = "AmazonBedrockAgentRetrieveKnowledgeBasePolicyProd",
                                    Effect = Effect.ALLOW,
                                    Actions = ["bedrock:Retrieve"],
                                    Resources = [_knowledgeBase.AttrKnowledgeBaseArn]
                                })
                            ]
                        })
                }
            });

        return agentRole;
    }

    /// <summary>
    /// Creates Lambda function for Bedrock Agents
    /// </summary>
    /// <returns><see cref="Function"/></returns>
    private Function CreateLambdaFunctionForBedrockAgents(Stack stack)
    {
        // Create Lambda functions for resolvers
        return new Function(
            stack, 
            "ChatBotBedrockActionGroupLambdaFunction", 
            new FunctionProps
            {
                FunctionName = $"chatbot-bedrock-agent-action-group-{Utils.GenerateRandomStringFromStackId(_stack.StackId)}",
                Runtime = Runtime.DOTNET_8,
                MemorySize = 512,
                Timeout = Duration.Seconds(300),
                Architecture = RuntimeInformation.ProcessArchitecture == System.Runtime.InteropServices.Architecture.X64
                    ? Amazon.CDK.AWS.Lambda.Architecture.X86_64
                    : Amazon.CDK.AWS.Lambda.Architecture.ARM_64,
                Description = "Function for Bedrock Agent's action group",
                Handler = "ActionGroupLambdaFunction",
                Code = Code.FromAsset(
                    "src/LambdaFunctions/BedrockAgent/ActionGroupLambdaFunction",
                    new Amazon.CDK.AWS.S3.Assets.AssetOptions
                    {
                        Bundling = LambdaFunctionsCdkUtils.GetBuildingOptions()
                    })
            });
    }

    /// <summary>
    /// Creates a custom resource to prepare the Knowledge Base for Bedrock Agent
    /// </summary>
    /// <returns><see cref="CustomResource"/></returns>    
    private CustomResource CreateAgentAlias()
    {
        // Create Lambda function for Bedrock Agent Alias Creation
        var aliasCreationLambdaFunction = CreateLambdaFunctionForAliasCreation();

        // Create custom resource to invoke the Lambda function
        var customResource = new CustomResource(
            _stack, 
            "ChatBotAgentAliasCreationCustomResource", 
            new CustomResourceProps
            {
                ServiceToken = aliasCreationLambdaFunction.FunctionArn,
                Properties = new Dictionary<string, object>
                {
                    ["Region"] = _stack.Region,
                    ["AliasName"] = "BedrockAgentCdkAlias",
                    ["AgentId"] = BedrockAgent.AttrAgentId,
                    ["description"] = "Alias for Bedrock Agent"
                }
            });

        // Once resource is created, use  Fn::GetAtt to get values of AliasId and AliasArn
        AgentAliasId = customResource.GetAttString("AliasId");
        AgentAliasArn = customResource.GetAttString("AliasArn");

        return customResource;
    } 

    /// <summary>
    /// Creates Lambda function for Bedrock Agent Alias Creation
    /// </summary>
    /// <returns><see cref="Function"/></returns>
    private Function CreateLambdaFunctionForAliasCreation()
    { 
        // Create Lambda functions
        var aliasCreationLambda = new Function(
            _stack, 
            "ChatBotBedrockAgentAliasCreationLambdaFunction", 
            new FunctionProps
            {
                FunctionName = $"chatbot-bedrock-agent-alias-creation-{Utils.GenerateRandomStringFromStackId(_stack.StackId)}",
                Runtime = Runtime.DOTNET_8,
                MemorySize = 512,
                Timeout = Duration.Seconds(180),
                Architecture = RuntimeInformation.ProcessArchitecture == System.Runtime.InteropServices.Architecture.X64
                    ? Amazon.CDK.AWS.Lambda.Architecture.X86_64
                    : Amazon.CDK.AWS.Lambda.Architecture.ARM_64,
                Description = "Function to create Bedrock Agent Alias",
                Handler = "BedrockAgentAliasCreation",
                Code = Code.FromAsset(
                    "src/LambdaFunctions/BedrockAgent/CustomResource/BedrockAgentAliasCreation",
                    new Amazon.CDK.AWS.S3.Assets.AssetOptions
                    {
                        Bundling = LambdaFunctionsCdkUtils.GetBuildingOptions()
                    })
            });


        // Add resource-based policy to lambda function to allow Bedrock to invoke the Lambda function
        aliasCreationLambda.AddToRolePolicy(
            new PolicyStatement(
                new PolicyStatementProps
                {
                    Sid = "BedrockAliasCreatePermission",
                    Effect = Effect.ALLOW,
                    Actions = [
                        "bedrock:CreateAgentAlias",
                        "bedrock:GetAgentAlias",
                        "bedrock:UpdateAgentAlias",
                        "bedrock:DeleteAgentAlias",
				        "bedrock:ListAgentAliases"
                    ],
                    Resources = [
                        BedrockAgent.AttrAgentArn,
                        $"arn:aws:bedrock:{_stack.Region}:{_stack.Account}:agent-alias/{BedrockAgent.AttrAgentId}/*"
                    ]
                }));


        return aliasCreationLambda;
    }
}