namespace AlbEcsBedrockAgentsCdkDotnet.Common;

internal static class Constants
{
    internal static readonly string Bedrock_FoundationModel_Titan_Embed_Text_V2 = "amazon.titan-embed-text-v2:0";

    internal static readonly string Bedrock_FoundationModel_Claude3_Haiku = "anthropic.claude-3-haiku-20240307-v1:0";

    internal static readonly string Bedrock_FoundationModel_Claude3_5_Haiku = "anthropic.claude-3-5-haiku-20241022-v1:0";

    internal static readonly string Bedrock_KB_AOSS_IndexName = "bedrock-knowledge-base-default-index";
    
    internal static readonly string Bedrock_KB_AOSS_MetadataField_Name = "AMAZON_BEDROCK_METADATA";

    internal static readonly string Bedrock_KB_AOSS_TextField_Name = "AMAZON_BEDROCK_TEXT_CHUNK";

    internal static readonly string Bedrock_KB_AOSS_VectorField_Name = "bedrock-knowledge-base-default-vector";

    internal static readonly string ResourceNamePrefix = "chatbot-alb-ecs-bedrockagents-cdk-dotnet";
}