using Amazon.CDK;
using Amazon.CDK.AWS.SES;
using Cdklabs.CdkNag;
using Constructs;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using static System.Net.Mime.MediaTypeNames;

namespace cdk
{
    static class Program
    {
        public static void Main(string[] args)
        {
            var app = new App();
            var cdkStack = new CdkStack(app, "orderAppCdkStack", new StackProps
            {
                // If you don't specify 'env', this stack will be environment-agnostic.
                // Account/Region-dependent features and context lookups will not work,
                // but a single synthesized template can be deployed anywhere.

                // Uncomment the next block to specialize this stack for the AWS Account
                // and Region that are implied by the current CLI configuration.
                /*
                Env = new Amazon.CDK.Environment
                {
                    Account = System.Environment.GetEnvironmentVariable("CDK_DEFAULT_ACCOUNT"),
                    Region = System.Environment.GetEnvironmentVariable("CDK_DEFAULT_REGION"),
                }
                */

                // Uncomment the next block if you know exactly what Account and Region you
                // want to deploy the stack to.

                Env = new Amazon.CDK.Environment
                {
                    Account = System.Environment.GetEnvironmentVariable("CDK_DEFAULT_ACCOUNT"),
                    Region = "us-east-1",
                }
                // For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
            });
            
            Aspects.Of(app).Add(new AwsSolutionsChecks(new NagPackProps()
            {
                Verbose = true
            }));

            NagSuppressions.AddStackSuppressions(cdkStack, new[] {
                new NagPackSuppression { Id = "AwsSolutions-COG4", Reason = "No using Cognito user pool authorizer, using API key for security for this sample..." },
                new NagPackSuppression { Id = "AwsSolutions-APIG4", Reason = "Not using Authorization, using API key for security for this sample..." },
                new NagPackSuppression { Id = "AwsSolutions-APIG2", Reason = "Validating request on Lambda in this sample..." },
                new NagPackSuppression { Id = "AwsSolutions-IAM4", Reason = "AWSLambdaBasicExecutionRole created as default in this sample..." },
                new NagPackSuppression { Id = "AwsSolutions-S1", Reason = "Not enabling Access logs for S3 in this sample..." },
                new NagPackSuppression { Id = "AwsSolutions-IAM5", Reason = "When CloudWatchRole enabled for lambda rest api, role automatically configured, service-role/AmazonAPIGatewayPushToCloudWatchLogs..." },
                //new NagPackSuppression { Id = "AwsSolutions-APIG6", Reason = "Not enabling CloudWatch logs for API in this sample..." },
                //new NagPackSuppression { Id = "AwsSolutions-APIG1", Reason = "Not enabling Access logs for API in this sample..." },
                //new NagPackSuppression { Id = "AwsSolutions-SF2", Reason = "Not enabling X-Ray tracing in this sample..." },
                //new NagPackSuppression { Id = "AwsSolutions-SF1", Reason = "Not logging all the SF events in CloudWatch in this sample..." },
                           });

            app.Synth();
        }
    }
}
