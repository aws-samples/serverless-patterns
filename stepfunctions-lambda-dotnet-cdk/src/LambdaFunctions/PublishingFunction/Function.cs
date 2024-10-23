using Amazon.Lambda.Core;
using Amazon.Lambda.RuntimeSupport;
using Amazon.Lambda.Serialization.SystemTextJson;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace PublishingFunction;

public class Function
{
    /// <summary>
    /// The main entry point for the Lambda function. The main function is called once during the Lambda init phase. It
    /// initializes the .NET Lambda runtime client passing in the function handler to invoke for each Lambda event and
    /// the JSON serializer to use for converting Lambda JSON format to the .NET types. 
    /// </summary>
    private static async Task Main()
    {
        Func<PublishingInput, ILambdaContext, PublishingResult> handler = FunctionHandler;
        await LambdaBootstrapBuilder.Create(handler, new SourceGeneratorLambdaJsonSerializer<LambdaFunctionJsonSerializerContext>())
            .Build()
            .RunAsync();
    }

    /// <summary>
    /// A simple function that takes a string and does a ToUpper.
    ///
    /// To use this handler to respond to an AWS event, reference the appropriate package from 
    /// https://github.com/aws/aws-lambda-dotnet#events
    /// and change the string input parameter to the desired event type. When the event type
    /// is changed, the handler type registered in the main method needs to be updated and the LambdaFunctionJsonSerializerContext 
    /// defined below will need the JsonSerializable updated. If the return type and event type are different then the 
    /// LambdaFunctionJsonSerializerContext must have two JsonSerializable attributes, one for each type.
    ///
    // When using Native AOT extra testing with the deployed Lambda functions is required to ensure
    // the libraries used in the Lambda function work correctly with Native AOT. If a runtime 
    // error occurs about missing types or methods the most likely solution will be to remove references to trim-unsafe 
    // code or configure trimming options. This sample defaults to partial TrimMode because currently the AWS 
    // SDK for .NET does not support trimming. This will result in a larger executable size, and still does not 
    // guarantee runtime trimming errors won't be hit. 
    /// </summary>
    /// <param name="input">The event for the Lambda function handler to process.</param>
    /// <param name="context">The ILambdaContext that provides methods for logging and describing the Lambda environment.</param>
    /// <returns></returns>
    public static PublishingResult FunctionHandler(PublishingInput input, ILambdaContext context)
    {
        context.Logger.LogInformation($"Publishing blog post: {JsonSerializer.Serialize(input, LambdaFunctionJsonSerializerContext.Default.PublishingInput)}");

        // Simulate publishing process
        var result = new PublishingResult
        {
            IsPublished = true,
            PublishedUrl = $"https://example.com/blog/{input.BlogPost.Id}",
            PublishedAt = DateTime.UtcNow
        };

        context.Logger.LogInformation($"Publishing result: {JsonSerializer.Serialize(result, LambdaFunctionJsonSerializerContext.Default.PublishingResult)}");
        return result;
    }
}

public class PublishingInput
{
    public required BlogPost BlogPost { get; set; }
    public required ValidationResult ValidationResult { get; set; }
    public required ImageProcessingResult ImageProcessingResult { get; set; }
}

public class BlogPost
{
    public required string Id { get; set; }
    public required string Title { get; set; }
    public required string Content { get; set; }
    public required string AuthorName { get; set; }
    public required DateTime CreatedAt { get; set; }
}

public class ValidationResult
{
    public bool IsValid { get; set; }
    public List<string>? Errors { get; set; }
}

public class ImageProcessingResult
{
    public required List<ProcessedImage> ProcessedImages { get; set; }
}

public class ProcessedImage
{
    public required string OriginalUrl { get; set; }
    public required string ProcessedUrl { get; set; }
    public int Width { get; set; }
    public int Height { get; set; }
}

public class PublishingResult
{
    public bool IsPublished { get; set; }
    public required string PublishedUrl { get; set; }
    public DateTime PublishedAt { get; set; }
}

/// <summary>
/// This class is used to register the input event and return type for the FunctionHandler method with the System.Text.Json source generator.
/// There must be a JsonSerializable attribute for each type used as the input and return type or a runtime error will occur 
/// from the JSON serializer unable to find the serialization information for unknown types.
/// </summary>
[JsonSerializable(typeof(string))]
[JsonSerializable(typeof(PublishingInput))]
[JsonSerializable(typeof(BlogPost))]
[JsonSerializable(typeof(ValidationResult))]
[JsonSerializable(typeof(ImageProcessingResult))]
[JsonSerializable(typeof(ProcessedImage))]
[JsonSerializable(typeof(PublishingResult))]
public partial class LambdaFunctionJsonSerializerContext : JsonSerializerContext
{
    // By using this partial class derived from JsonSerializerContext, we can generate reflection free JSON Serializer code at compile time
    // which can deserialize our class and properties. However, we must attribute this class to tell it what types to generate serialization code for.
    // See https://docs.microsoft.com/en-us/dotnet/standard/serialization/system-text-json-source-generation
}