using System.Collections.Generic;
using Amazon.CDK;
using Amazon.CDK.AWS.APIGateway;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.S3;
using Amazon.CDK.AWS.S3.Deployment;
using Constructs;

namespace Cdk
{
    public class CdkStack : Stack
    {
        internal CdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // Sample Json file content
            var sampleJson = new Dictionary<string, object> {
                { "key1", "value1" },
                { "key2", "value2" }
            };

            // File Names for reuse
            var stringFile = "string-file.txt";
            var jsonFile = "json-file.json";

             // S3 Bucket - for the files
            var fileshareBucket = new Bucket(this, "filebucketshare", new BucketProps
            {
                Versioned = true
            });

            // S3 Bucket Deployment for the sample files for read
            new BucketDeployment(this, "DeployFiles", new BucketDeploymentProps()
            {
                Sources = new[] {
                    Source.Data(stringFile, "This sample Text!!!"),
                    Source.JsonData(jsonFile, sampleJson )
                    },
                DestinationBucket = fileshareBucket
            });


            // Docker file with multi-stage build
            DockerImageCode dockerImageCode = DockerImageCode.FromImageAsset("../lambda/src/lambda");

            // Lambda from Image
            DockerImageFunction dockerImageFunction = new DockerImageFunction(this,
                "container-image-lambda-function",
                new DockerImageFunctionProps()
                {
                    Code = dockerImageCode,
                    Description = ".NET 6 Docker Lambda function",
                    Environment = new Dictionary<string, string>
                    {
                        { "BUCKET_NAME", fileshareBucket.BucketName},
                        {"QUERYSTRING_KEY", "key"}
                    },
                    Timeout = Duration.Minutes(1)
                });

            // Lambda Permission
            fileshareBucket.GrantReadWrite(dockerImageFunction);

            // APIGateway 
            var apiGateway = new RestApi(this, "cdkApi", new RestApiProps()
            {
                RestApiName = "CdkApi",
                Description = "Lambda Backed API - Get SignedUrl"
            });

            // APIGateway - Root Method
            apiGateway.Root.AddMethod(
                "GET",
                new LambdaIntegration(dockerImageFunction, new LambdaIntegrationOptions
                {
                    Proxy = true
                })
            );

            // CDK - Output
            new CfnOutput(this, "TextFile-Test-URL", new CfnOutputProps
            {
                Value = apiGateway.Url + "?key=" + stringFile
            });

            new CfnOutput(this, "JsonFile-Test-URL", new CfnOutputProps
            {
                Value = apiGateway.Url + "?key=" + jsonFile
            });
        }
    }
}
