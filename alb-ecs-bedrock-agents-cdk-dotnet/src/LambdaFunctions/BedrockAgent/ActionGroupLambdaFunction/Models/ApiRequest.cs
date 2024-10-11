using System.Text.Json.Serialization;

namespace ActionGroupLambdaFunction.Models;

public class Parameter
{
    public string? Name { get; set; }
    public string? Type { get; set; }
    public string? Value { get; set; }
}

public class Property
{
    public string? Name { get; set; }
    public string? Type { get; set; }
    public string? Value { get; set; }
}

public class JsonProperties
{
    public List<Property>? Properties { get; set; }
}

public class Content
{
    [JsonPropertyName("application/json")]
    public JsonProperties? JsonProperties { get; set; }
}

public class RequestBody
{
    public Content? Content { get; set; }
}

public class SessionAttributes
{
}

public class PromptSessionAttributes
{
}

public class Agent
{
    public string? Name { get; set; }
    public string? Id { get; set; }
    public string? Alias { get; set; }
    public string? Version { get; set; }
}

public class ApiRequest
{
    public string? MessageVersion { get; set; }
    public Agent? Agent { get; set; }
    public string? InputText { get; set; }
    public string? SessionId { get; set; }
    public string? ExecutionType { get; set; }
    public string? ActionGroup { get; set; }
    public string? ApiPath { get; set; }
    public string? HttpMethod { get; set; }
    public List<Parameter>? Parameters { get; set; }
    public RequestBody? RequestBody { get; set; }
    public SessionAttributes? SessionAttributes { get; set; }
    public PromptSessionAttributes? PromptSessionAttributes { get; set; }
}

