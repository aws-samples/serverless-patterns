namespace ActionGroupLambdaFunction.Models;

public class VectorSearchConfiguration
{
    public int NumberOfResults { get; set; }

    public string? OverrideSearchType { get; set; }

    public string? Filter { get; set; }
}

public class RetrievalConfiguration
{
    public VectorSearchConfiguration? VectorSearchConfiguration { get; set; }
}

public class KnowledgeBasesConfiguration
{
    public string? KnowledgeBaseId { get; set; }

    public RetrievalConfiguration? RetrievalConfiguration { get; set; }
}

public class ResponseBody
{
    public string? body { get; set; }
}

public class Response
{
    public string? actionGroup { get; set; }

    public string? apiPath { get; set; }
    
    public string? httpMethod { get; set; }
    
    public int httpStatusCode { get; set; }
    
    public Dictionary<string, ResponseBody>? responseBody { get; set; }
}

public class ApiResponse
{
    public string? messageVersion { get; set; }

    public Response? response { get; set; }
    
    public Dictionary<string,string>? sessionAttributes { get; set; }
    
    public Dictionary<string,string>? promptSessionAttributes { get; set; }
    
    public List<KnowledgeBasesConfiguration>? knowledgeBasesConfiguration { get; set; }
}



