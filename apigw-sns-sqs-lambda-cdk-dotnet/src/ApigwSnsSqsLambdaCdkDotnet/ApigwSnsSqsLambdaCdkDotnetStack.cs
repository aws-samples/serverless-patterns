using Amazon.CDK;
using Amazon.CDK.AWS.SNS;
using Amazon.CDK.AWS.SNS.Subscriptions;
using Amazon.CDK.AWS.SQS;
using Amazon.CDK.AWS.APIGateway;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.Lambda.EventSources;
using Amazon.CDK.AWS.IAM;
using Constructs;
using System.Collections.Generic;
using AssetOptions = Amazon.CDK.AWS.S3.Assets.AssetOptions;


namespace ApigwSnsSqsLambdaCdkDotnet
{
    public class ApigwSnsSqsLambdaCdkDotnetStack : Stack
    {
        internal ApigwSnsSqsLambdaCdkDotnetStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {

            var topicCarPriceChange = new Topic(this, "CarPriceChange");

            var queueCarChangeQueueNonPremium = new Queue(this, "CarChangeQueueNonPremium", new QueueProps
            {
                VisibilityTimeout = Duration.Seconds(300)
            });


            topicCarPriceChange.AddSubscription(new SqsSubscription(queueCarChangeQueueNonPremium));

            var lambdaCarChangeQueueNonPremium = new Function(this, "nonPremiumWorkerHandler", new FunctionProps
            {
                Runtime = Runtime.DOTNET_6,
                Handler = "ApiEventHandler::ApiEventHandler.Function::SQSHandler",
                Code = Code.FromAsset("./src/lambdaHandler/ApiEventHandler/src/ApiEventHandler/bin/Debug/net6.0"),

            });

            lambdaCarChangeQueueNonPremium.AddEventSource(new SqsEventSource(queueCarChangeQueueNonPremium));


            var queueCarChangeQueuPremium = new Queue(this, "CarChangeQueuePremium", new QueueProps
            {
                VisibilityTimeout = Duration.Seconds(300)
            });


            topicCarPriceChange.AddSubscription(new SqsSubscription(queueCarChangeQueuPremium));

            var buildOption = new BundlingOptions()
            {
                Image = Runtime.DOTNET_6.BundlingImage,
                User = "root",
                OutputType = BundlingOutput.ARCHIVED,
                Command = new string[]{
                    "/bin/sh",
                    "-c",
                    " dotnet tool install -g Amazon.Lambda.Tools"+
                    " && dotnet build"+
                    " && dotnet lambda package --output-package /asset-output/function.zip"
                }
            };

            var lambdaCarChangeQueuePremium = new Function(this, "premiumWorkerHandler", new FunctionProps
            {
                Runtime = Runtime.DOTNET_6,
                Handler = "Lambdas::Lambdas.Function::SQSHandler",
                Code = Code.FromAsset("./src/lambdaHandler/ApiEventHandler/src/ApiEventHandler", new AssetOptions
                {
                    Bundling = buildOption

                })

            });

            lambdaCarChangeQueuePremium.AddEventSource(new SqsEventSource(queueCarChangeQueuPremium));


            var gateWayExecutionRole = new Role(this, "GatewayExecutionRole", new RoleProps
            {
                AssumedBy = new ServicePrincipal("apigateway.amazonaws.com"),
                InlinePolicies = new Dictionary<string, PolicyDocument>
                  {
                    {
                        "PublishMessagePolicy", new PolicyDocument(new PolicyDocumentProps
                        {
                            Statements = new[] {
                            new PolicyStatement(new PolicyStatementProps
                            {
                                Actions = new []{"sns:Publish"},
                                Resources = new []{topicCarPriceChange.TopicArn}

                            })
                        }

                        })
                    }
                  }
            }
            );
            //Api Gateway 

            var awsIntegration = new AwsIntegration(new AwsIntegrationProps
            {
                Service = "sns",
                IntegrationHttpMethod = "POST",
                Path = "/",
                Options = new IntegrationOptions
                {
                    CredentialsRole = gateWayExecutionRole,
                    PassthroughBehavior = PassthroughBehavior.NEVER,
                    RequestParameters = new Dictionary<string, string>{
                        {"integration.request.header.Content-Type","'application/x-www-form-urlencoded'"}
                    },
                    RequestTemplates = new Dictionary<string, string>{
                        {"application/json","Action=Publish&TopicArn=$util.urlEncode('"+topicCarPriceChange.TopicArn+"')&Message=$util.urlEncode($input.body)"}
                    },
                    IntegrationResponses = new[]{
                        new IntegrationResponse {
                            StatusCode = "200",
                            ResponseTemplates = new Dictionary<string,string>{
                                {"application/json", @"{""status"": ""message added to topic""}"
                                }
                            }
                        }  ,
                        new IntegrationResponse {
                            StatusCode = "400",
                            SelectionPattern = "^\\[Error\\].*",
                            ResponseTemplates = new Dictionary<string,string>{
                                {"application/json","{\"state\":\"error\",\"message\":\"$util.escapeJavaScript($input.path('$.errorMessage'))\"}"
                                }
                            }

                        }
                     }

                },

            });

            var apiGateWay = new RestApi(this, "CarPriceChangeApi");
            apiGateWay.Root.AddMethod("POST", awsIntegration, new MethodOptions
            {
                MethodResponses = new[] { new MethodResponse{
                    StatusCode="200"
                },
                new MethodResponse{
                    StatusCode="400"
                }
                }

            });

        }
    }
}
