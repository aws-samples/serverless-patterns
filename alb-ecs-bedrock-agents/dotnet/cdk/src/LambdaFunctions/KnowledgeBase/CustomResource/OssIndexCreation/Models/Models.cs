// This file contains the models used by the Lambda function to handle the custom resource request and response.
namespace OssIndexCreation.Models;

public class CfnRequest
{
    public string RequestType { get; set; } = string.Empty;
    
    public string ResponseURL { get; set; } = string.Empty;
    
    public string StackId { get; set; } = string.Empty;
    
    public string RequestId { get; set; } = string.Empty;
    
    public string ResourceType { get; set; } = string.Empty;
    
    public string LogicalResourceId { get; set; } = string.Empty;

    public string PhysicalResourceId { get; set; } = string.Empty;
    
    public ResourceProperties ResourceProperties { get; set; } = new ResourceProperties();
}

public class CfnResponse
{
    public string Status { get; set; } = string.Empty;
    
    public string Reason { get; set; } = string.Empty;
    
    public string PhysicalResourceId { get; set; } = string.Empty;
    
    public string StackId { get; set; } = string.Empty;
    
    public string RequestId { get; set; } = string.Empty;
    
    public string LogicalResourceId { get; set; } = string.Empty;

    public bool NoEcho { get; set; } = false;
    
    public Dictionary<string, string>? Data {get;set;} = null;
}

public sealed class ResourceProperties
{
    public string ServiceToken { get; set; } = string.Empty;

    public string Region { get; set; } = string.Empty;

    public string AOSSIndexName { get; set; } = string.Empty;

    public string AOSSHost { get; set; } = string.Empty;

    public string AOSSMetadataFieldName { get; set; } = string.Empty;

    public string AOSSTextFieldName { get; set; } = string.Empty;

    public string AOSSVectorFieldName { get; set; } = string.Empty;
}