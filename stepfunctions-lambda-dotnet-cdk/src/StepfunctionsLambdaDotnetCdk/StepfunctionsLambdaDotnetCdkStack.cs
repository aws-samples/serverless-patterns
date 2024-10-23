using System.Collections.Generic;
using System.Runtime.InteropServices;
using Amazon.CDK;
using Amazon.CDK.AWS.IAM;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.Logs;
using Amazon.CDK.AWS.StepFunctions;
using Amazon.CDK.AWS.StepFunctions.Tasks;
using Constructs;

namespace StepfunctionsLambdaDotnetCdk
{
    public class StepfunctionsLambdaDotnetCdkStack : Stack
    {
        private readonly string _randomString;

        internal StepfunctionsLambdaDotnetCdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            _randomString = GenerateRandomStringFromStackId(StackId);

            // Lambda Functions
            var contentCreationFunction = CreateContentCreationLambdaFunction();
            var contentValidationFunction = CreateContentValidationLambdaFunction();
            var imageProcessingFunction = CreateImageProcessingLambdaFunction();
            var publishingFunction = CreatePublishingLambdaFunction();

            // StepFunction Tasks
            var contentCreationTask = CreateContentCreationTask(contentCreationFunction);
            var contentValidationTask = CreateContentValidation(contentValidationFunction);
            var imageProcessingTask = CreateImageProcessingTask(imageProcessingFunction);
            var handleInvalidContentTask = CreateHandleInvalidContentTask();
            var invalidContentFailTask = CreateInvalidContentFailTask();
            var publishingTask = CreatePublishingTask(publishingFunction);
            var fallbackTask = CreateFallbackTask();
            var fallbackFailTask = CreateFallbackFailTask();

            // Content processing workflow
            var contentProcessingWorkflow = CreateContentProcessingWorkflow(
                contentValidationTask, 
                imageProcessingTask, 
                handleInvalidContentTask, 
                invalidContentFailTask, 
                publishingTask,
                fallbackTask,
                fallbackFailTask);
                
            // Blogpost processing map
            var processBlogPostsMap = CreateProcessBlogPostsMap();
            processBlogPostsMap.ItemProcessor(contentProcessingWorkflow);

            // Saga Pattern: Main Workflow with Compensation
            var sagaWorkflow = CreateSagaWorkflow(
                contentCreationTask, processBlogPostsMap);

            // Fail task
            var failTask = new Fail(this, "WorkflowFailTask", new FailProps
            {
                Comment = "Workflow failed",
                ErrorPath = JsonPath.StringAt("$.error")
            });
            
            // Step Functions Definition
            var definition = new Parallel(
                this,
                "MainParallel",
                new ParallelProps
                {
                    ResultPath = "$.overallOutput",
                    Comment = "Main parallel execution of saga and monitoring",
                    StateName = "MainWorkflowExecution"
                })
                .Branch(sagaWorkflow)
                .Branch(new Wait(
                    this, 
                    "ParallelWait", 
                    new WaitProps
                    {
                        Time = WaitTime.Duration(Duration.Seconds(30)),
                        Comment = "Parallel wait for monitoring or timeout purposes",
                        StateName = "MonitoringWait"
                    }))
                .AddCatch(failTask, new CatchProps
                {
                    ResultPath = "$.error",
                    Errors = ["States.ALL"]
                });

            // Create Step Functions State Machine
            var stateMachine = new StateMachine(
                this,
                "BlogProcessingStateMachine",
                new StateMachineProps
                {
                    DefinitionBody = DefinitionBody.FromChainable(definition),
                    Timeout = Duration.Hours(24),
                    TracingEnabled = true,
                    StateMachineType = StateMachineType.STANDARD,
                    Comment = "Blog post processing workflow with parallel execution, human approval, and error handling",
                    StateMachineName = "BlogPostProcessingWorkflow",
                    Logs = new LogOptions
                    {
                        Destination = new LogGroup(this, "BlogProcessingLogGroup"),
                        Level = LogLevel.ALL,
                        IncludeExecutionData = true
                    },
                    Role = new Role(this, "StateMachineRole", new RoleProps
                    {
                        AssumedBy = new ServicePrincipal("states.amazonaws.com")
                    })
                });

            // Output
            _ = new CfnOutput(this, "StateMachineArn", new CfnOutputProps
            {
                Value = stateMachine.StateMachineArn,
                Description = "ARN of the Blog Processing State Machine"
            });
        }

        /// <summary>
        /// Creates content processing workflow (Nested)
        /// </summary>
        /// <param name="contentValidationTask">Content validation task</param>
        /// <param name="imageProcessingTask">Image processing task</param>
        /// <param name="handleInvalidContentTask">Handle invalid content task</param>
        /// <param name="invalidContentFailTask">Invalid content Fail task</param>
        /// <param name="fallbackTask">Fallback task</param>
        /// <param name="errorFailTask">Fallback fail task</param>
        /// <returns><see cref="Chain"/></returns>
        private Chain CreateContentProcessingWorkflow(
            LambdaInvoke contentValidationTask, 
            LambdaInvoke imageProcessingTask, 
            Pass handleInvalidContentTask,
            Fail invalidContentFailTask,
            LambdaInvoke publishingTask,
            Pass fallbackTask,
            Fail errorFailTask)
        {
            // Chain
            handleInvalidContentTask.Next(invalidContentFailTask);
            fallbackTask.Next(errorFailTask);

            // Define the workflow for processing a single blog post
            var processSingleBlogPost = new Choice(this, "ValidateContentChoice")
                .When(Condition.BooleanEquals("$.validateContentOutput.Payload.IsValid", true), Chain.Start(imageProcessingTask).Next(publishingTask))
                .Otherwise(handleInvalidContentTask);

            // Nested Workflow: Content Processing
            return Chain
                .Start(contentValidationTask)
                .Next(new Parallel(
                    this,
                    "ParallelProcessing",
                    new ParallelProps
                    {
                        ResultPath = "$.parallelOutput",
                        Comment = "Process content and images in parallel",
                        StateName = "ParallelContentAndImageProcessing"
                    })
                    .Branch(processSingleBlogPost)
                    .Branch(new Wait(this, "ProcessingDelay", new WaitProps
                    {
                        Time = WaitTime.Duration(Duration.Seconds(10)),
                        Comment = "Artificial delay for demonstration purposes",
                        StateName = "ArtificialProcessingDelay"
                    }))
                    .AddCatch(fallbackTask, new CatchProps
                    {
                        ResultPath = "$.error",
                        Errors = ["States.ALL"]
                    }));
        }

        /// <summary>
        /// Creates blogpost processing map (Dynamic parallel)
        /// </summary>
        /// <returns><see cref="Map"/></returns>
        private Map CreateProcessBlogPostsMap()
        {
            // Dynamic Parallel: Process Multiple Blog Posts
            return new Map(
                this,
                "ProcessBlogPostsMap",
                new MapProps
                {
                    MaxConcurrency = 5,
                    ItemsPath = "$.contentCreationOutput.Payload",
                    ResultPath = "$.processedBlogPosts",
                    Comment = "Process multiple blog posts concurrently",
                    StateName = "ProcessMultipleBlogPosts"
                });
        }

        /// <summary>
        /// Creates main workflow - Saga Pattern: Main Workflow
        /// </summary>
        /// <param name="contentCreationTask">Content creation task</param>
        /// <param name="processBlogPostsMap">Process blogpost map</param>
        /// <returns><see cref="Chain"/></returns>
        private Chain CreateSagaWorkflow(
            LambdaInvoke contentCreationTask, 
            Map processBlogPostsMap)
        {

            // New Succeed task to output published blog IDs
            var succeedTask = new Succeed(
                this, 
                "SucceedTask", 
                new SucceedProps
                {
                    Comment = "Workflow completed successfully",
                    OutputPath = "$.publishedBlogIds"
                });

            // Task to extract published blog IDs
            var extractPublishedBlogIdsTask = new Pass(
                this, 
                "ExtractPublishedBlogIds", 
                new PassProps
                {
                    Parameters = new Dictionary<string, object>
                    {
                        { "publishedBlogIds.$", "$.processedBlogPosts[?(@.publishingOutput.Payload.Status == 'PUBLISHED')].publishingOutput.Payload.BlogId" }
                    },
                    ResultPath = "$.publishedBlogIds",
                    StateName = "ExtractPublishedBlogIds"
                });

            // Saga Pattern: Main Workflow
            return Chain
                .Start(contentCreationTask)
                .Next(processBlogPostsMap)
                .Next(extractPublishedBlogIdsTask)
                .Next(succeedTask);
        }

        /// <summary>
        /// Creates content creation task
        /// </summary>
        /// <param name="contentCreationFunction">Content creation function</param>
        /// <returns><see cref="LambdaInvoke"/></returns>
        private LambdaInvoke CreateContentCreationTask(Function contentCreationFunction)
        {
            // Step Functions Tasks
            return new LambdaInvoke(
                this,
                "ContentCreationTask",
                new LambdaInvokeProps
                {
                    LambdaFunction = contentCreationFunction,
                    ResultPath = "$.contentCreationOutput",
                    RetryOnServiceExceptions = true,
                    Payload = TaskInput.FromObject(
                        new Dictionary<string, object>
                        {
                            { "title", JsonPath.StringAt("$.title") },
                            { "content", JsonPath.StringAt("$.content") },
                            { "authorName", JsonPath.StringAt("$.authorName") }
                        }),
                    PayloadResponseOnly = null,
                    InvocationType = LambdaInvocationType.REQUEST_RESPONSE,
                    TaskTimeout = Timeout.Duration(Duration.Seconds(60)),
                    StateName = "CreateContent"
                });
        }

        /// <summary>
        /// Creates content validation task
        /// </summary>
        /// <param name="contentValidationFunction">Content validation function</param>
        /// <returns><see cref="LambdaInvoke"/></returns>
        private LambdaInvoke CreateContentValidation(Function contentValidationFunction)
        {
            return new LambdaInvoke(
                this,
                "ContentValidationTask",
                new LambdaInvokeProps
                {
                    LambdaFunction = contentValidationFunction,
                    ResultPath = "$.validateContentOutput",
                    RetryOnServiceExceptions = true,
                    Payload = TaskInput.FromJsonPathAt("$"),
                    PayloadResponseOnly = null,
                    InvocationType = LambdaInvocationType.REQUEST_RESPONSE,
                    TaskTimeout = Timeout.Duration(Duration.Seconds(60)),
                    StateName = "ValidateContent"
                });
        }

        /// <summary>
        /// Creates image processing task
        /// </summary>
        /// <param name="imageProcessingFunction">Image processing function</param>
        /// <returns><see cref="LambdaInvoke"/></returns>
        private LambdaInvoke CreateImageProcessingTask(Function imageProcessingFunction)
        {
            return new LambdaInvoke(
                this,
                "ImageProcessingTask",
                new LambdaInvokeProps
                {
                    LambdaFunction = imageProcessingFunction,
                    ResultPath = "$.imageProcessingOutput",
                    RetryOnServiceExceptions = true,
                    Payload = TaskInput.FromObject(
                        new Dictionary<string, object>
                        {
                            { "id", JsonPath.StringAt("$.Id") },
                            { "title", JsonPath.StringAt("$.Title") },
                            { "content", JsonPath.StringAt("$.Content") },
                            { "authorName", JsonPath.StringAt("$.AuthorName") },
                            { "createdAt", JsonPath.StringAt("$.CreatedAt") }
                        }),
                    PayloadResponseOnly = null,
                    InvocationType = LambdaInvocationType.REQUEST_RESPONSE,
                    TaskTimeout = Timeout.Duration(Duration.Seconds(90)),
                    StateName = "ProcessImages"
                });
        }

        /// <summary>
        /// Creates handle invalid content task
        /// </summary>
        /// <returns><see cref="Pass"/></returns>
        private Pass CreateHandleInvalidContentTask()
        {
            // Define a task for handling invalid content
            var handleInvalidContentTask = new Pass(
                this, 
                "HandleInvalidContent", 
                new PassProps
                {
                    Parameters = new Dictionary<string, object>
                    {
                        { "status", "INVALID_CONTENT" },
                        { "message", "Content validation failed" },
                        { "errors.$", "$.validateContentOutput.Payload.Errors" }
                    },
                    ResultPath = "$.invalidContentHandling",
                    StateName = "HandleInvalidContent"
                });

            return handleInvalidContentTask;
        }

        /// <summary>
        /// Creates publishing task
        /// </summary>
        /// <param name="publishingFunction">Publishing function</param>
        /// <returns><see cref="LambdaInvoke"/></returns>
        private LambdaInvoke CreatePublishingTask(Function publishingFunction)
        {
            return new LambdaInvoke(
                this,
                "PublishingTask",
                new LambdaInvokeProps
                {
                    LambdaFunction = publishingFunction,
                    ResultPath = "$.publishingOutput",
                    RetryOnServiceExceptions = true,
                    Payload = TaskInput.FromObject(
                        new Dictionary<string, object>
                        {
                            { 
                                "BlogPost",  
                                new Dictionary<string, object>{                            
                                    { "id", JsonPath.StringAt("$.Id") },
                                    { "title", JsonPath.StringAt("$.Title") },
                                    { "content", JsonPath.StringAt("$.Content") },
                                    { "authorName", JsonPath.StringAt("$.AuthorName") },
                                    { "createdAt", JsonPath.StringAt("$.CreatedAt") }
                                }
                            },
                            { "ValidationResult", JsonPath.StringAt("$.validateContentOutput.Payload") },
                            { "ImageProcessingResult", JsonPath.StringAt("$.imageProcessingOutput.Payload") }
                        }),
                    PayloadResponseOnly = null,
                    InvocationType = LambdaInvocationType.REQUEST_RESPONSE,
                    TaskTimeout = Timeout.Duration(Duration.Seconds(60)),
                    StateName = "PublishContent"
                });
        }

        /// <summary>
        /// Creates fallback task
        /// </summary>
        /// <returns><see cref="Pass"/></returns>
        private Pass CreateFallbackTask()
        {
            return new Pass(
                this,
                "FallbackTask",
                new PassProps
                {
                    Parameters = new Dictionary<string, object>
                    {
                        { "error", "Processing failed, manual review required" },
                        { "timestamp.$", "$$.State.EnteredTime" }
                    },
                    ResultPath = "$.fallbackOutput",
                    Comment = "Fallback state for handling errors",
                    StateName = "FallbackErrorHandler"
                });
        }

        /// <summary>
        /// Create a fail task to handle invalid content
        /// </summary>
        /// <returns><see cref="Fail"/></returns>
        private Fail CreateInvalidContentFailTask()
        {
            return new Fail(
                this,
                "InvalidContentFailTask",
                new FailProps
                {
                    Comment = "Fail state for invalid content",
                    ErrorPath = "$.validateContentOutput.Payload.Errors[0]"
                }
            );
        }

        private Fail CreateFallbackFailTask()
        {
            return new Fail(
                this,
                "ErrorFailTask",
                new FailProps
                {
                    Comment = "Fail state for errors",
                    ErrorPath = "$.error.Error"
                }
            );            
        }

        /// <summary>
        /// Creates Lambda function for Content Creation
        /// </summary>
        /// <returns><see cref="Function"/></returns>
        private Function CreateContentCreationLambdaFunction()
        { 
            // Create Lambda function
            var contentCreationLambda = new Function(
                this, 
                "ContentCreationLambdaFunction", 
                new FunctionProps
                {
                    FunctionName = $"content-creation-{_randomString}",
                    Runtime = Runtime.DOTNET_8,
                    MemorySize = 512,
                    Timeout = Duration.Seconds(30),
                    Architecture = RuntimeInformation.ProcessArchitecture == System.Runtime.InteropServices.Architecture.X64
                        ? Amazon.CDK.AWS.Lambda.Architecture.X86_64
                        : Amazon.CDK.AWS.Lambda.Architecture.ARM_64,
                    Description = "Function to create content",
                    Handler = "ContentCreationFunction",
                    Code = Code.FromAsset(
                        "src/LambdaFunctions/ContentCreationFunction",
                        new Amazon.CDK.AWS.S3.Assets.AssetOptions
                        {
                            Bundling = GetBuildingOptions()
                        })
                });

            return contentCreationLambda;
        }

        /// <summary>
        /// Creates Lambda function for Content Validation
        /// </summary>
        /// <returns><see cref="Function"/></returns>
        private Function CreateContentValidationLambdaFunction()
        { 
            // Create Lambda function
            var contentValidationLambda = new Function(
                this, 
                "ContentValidationLambdaFunction", 
                new FunctionProps
                {
                    FunctionName = $"content-validation-{_randomString}",
                    Runtime = Runtime.DOTNET_8,
                    MemorySize = 512,
                    Timeout = Duration.Seconds(30),
                    Architecture = RuntimeInformation.ProcessArchitecture == System.Runtime.InteropServices.Architecture.X64
                        ? Amazon.CDK.AWS.Lambda.Architecture.X86_64
                        : Amazon.CDK.AWS.Lambda.Architecture.ARM_64,
                    Description = "Function to validate content",
                    Handler = "ContentValidationFunction",
                    Code = Code.FromAsset(
                        "src/LambdaFunctions/ContentValidationFunction",
                        new Amazon.CDK.AWS.S3.Assets.AssetOptions
                        {
                            Bundling = GetBuildingOptions()
                        })
                });

            return contentValidationLambda;
        }

        /// <summary>
        /// Creates Lambda function for Image Processing
        /// </summary>
        /// <returns><see cref="Function"/></returns>
        private Function CreateImageProcessingLambdaFunction()
        { 
            // Create Lambda function
            var imageProcessingLambda = new Function(
                this, 
                "ImageProcessingLambdaFunction", 
                new FunctionProps
                {
                    FunctionName = $"image-processing-{_randomString}",
                    Runtime = Runtime.DOTNET_8,
                    MemorySize = 512,
                    Timeout = Duration.Seconds(30),
                    Architecture = RuntimeInformation.ProcessArchitecture == System.Runtime.InteropServices.Architecture.X64
                        ? Amazon.CDK.AWS.Lambda.Architecture.X86_64
                        : Amazon.CDK.AWS.Lambda.Architecture.ARM_64,
                    Description = "Function to process images",
                    Handler = "ImageProcessingFunction",
                    Code = Code.FromAsset(
                        "src/LambdaFunctions/ImageProcessingFunction",
                        new Amazon.CDK.AWS.S3.Assets.AssetOptions
                        {
                            Bundling = GetBuildingOptions()
                        })
                });

            return imageProcessingLambda;
        }

        /// <summary>
        /// Creates Lambda function for publishing
        /// </summary>
        /// <returns><see cref="Function"/></returns>
        private Function CreatePublishingLambdaFunction()
        { 
            // Create Lambda function
            var publishingLambda = new Function(
                this, 
                "PublishingLambdaFunction", 
                new FunctionProps
                {
                    FunctionName = $"publishing-{_randomString}",
                    Runtime = Runtime.DOTNET_8,
                    MemorySize = 512,
                    Timeout = Duration.Seconds(30),
                    Architecture = RuntimeInformation.ProcessArchitecture == System.Runtime.InteropServices.Architecture.X64
                        ? Amazon.CDK.AWS.Lambda.Architecture.X86_64
                        : Amazon.CDK.AWS.Lambda.Architecture.ARM_64,
                    Description = "Function to publish",
                    Handler = "PublishingFunction",
                    Code = Code.FromAsset(
                        "src/LambdaFunctions/PublishingFunction",
                        new Amazon.CDK.AWS.S3.Assets.AssetOptions
                        {
                            Bundling = GetBuildingOptions()
                        })
                });

            return publishingLambda;
        }

        /// <summary>
        /// Gets the bundling options for Lambda functions
        /// </summary>
        /// <returns><see cref="BundlingOptions"/></returns>
        internal static BundlingOptions GetBuildingOptions()
        {
            // Build options for Lambda functions
            return new BundlingOptions()
            {
                Image = Runtime.DOTNET_8.BundlingImage,
                User = "root",
                OutputType = BundlingOutput.ARCHIVED,
                Command = [
                    "/bin/sh",
                    "-c",
                    "dotnet tool install -g Amazon.Lambda.Tools && " +
                    "dotnet build && " +
                    "dotnet lambda package " +
                    "--function-architecture " + (RuntimeInformation.ProcessArchitecture == System.Runtime.InteropServices.Architecture.X64 ? "x86_64" : "arm64") + " " +
                    "--output-package /asset-output/function.zip"
                ],
            };
        }        

        /// <summary>
        /// Generates a random string from the stack id
        /// </summary>
        /// <returns></returns>
        private static string GenerateRandomStringFromStackId(string stackId)
        {
            return Fn.Select(4, Fn.Split("-", Fn.Select(2, Fn.Split("/", stackId))));
        }    
    }
}
