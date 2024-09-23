using System;
using System.Linq;

namespace AlbEcsBedrockAgentsCdkDotnet;

internal static class Utils
{
    /// <summary>
    /// 
    /// </summary>
    /// <returns></returns>
    internal static string GenerateRandomString()
    {
        const string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        var random = new Random();
        var randomString = new string(Enumerable.Repeat(chars, 5)
            .Select(s => s[random.Next(s.Length)]).ToArray());

        return randomString.ToLowerInvariant();
    }

    /// <summary>
    /// 
    /// </summary>
    /// <param name="region"></param>
    /// <returns></returns>
    internal static string GetTitanV2FMArn(string region)
    {
        return $"arn:aws:bedrock:{region}::" + "foundation-model/" + Constants.Bedrock_FoundationModel_Titan_Embed_Text_V2;
    }

    /// <summary>
    /// 
    /// </summary>
    /// <param name="region"></param>
    /// <returns></returns>
    internal static string GetCluade3HaikuFMArn(string region)
    {
        return $"arn:aws:bedrock:{region}::" + "foundation-model/" + Constants.Bedrock_FoundationModel_Claude3_Haiku;
    }    
}