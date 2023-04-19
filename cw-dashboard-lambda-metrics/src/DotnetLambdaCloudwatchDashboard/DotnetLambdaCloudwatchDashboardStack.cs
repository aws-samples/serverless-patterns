using System.Collections.Generic;
using Amazon.CDK;
using Amazon.CDK.AWS.CloudWatch;
using Amazon.CDK.AWS.Lambda;
using Constructs;

namespace DotnetLambdaCloudwatchDashboard
{
    public class DotnetLambdaCloudwatchDashboardStack : Stack
    {
        internal DotnetLambdaCloudwatchDashboardStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // The code that defines your stack goes here
            DockerImageCode dockerImageCode = DockerImageCode.FromImageAsset("src/lambda/proxy-lambda");

            var layerArn = "arn:aws:lambda:us-east-1:580247275435:layer:LambdaInsightsExtension:14";

            // Lambda from Image
            DockerImageFunction dockerImageFunction = new DockerImageFunction(this,
                "container-image-lambda-function",
                new DockerImageFunctionProps()
                {
                    Code = dockerImageCode,
                    Description = ".NET 6 Docker Lambda function",
                    Timeout = Duration.Minutes(1),
                    InsightsVersion = LambdaInsightsVersion.FromInsightVersionArn(layerArn)
                });

            var dashboard = new Dashboard(this, "DotnetCDKDashboard");

            dashboard.AddWidgets(new TextWidget(new TextWidgetProps
            {
                Markdown = "# Key Performance Indicators",
                Width = 24,
                Height = 1
            }));

            List<Metric> invocations_metrics = new List<Metric>();
            invocations_metrics.Add(dockerImageFunction.MetricInvocations());

            dashboard.AddWidgets(new GraphWidget(new GraphWidgetProps
            {
                Title = "Invocations",
                Left = invocations_metrics.ToArray(),
                Width = 24
            }));

            List<Metric> insights_metrics = new List<Metric>();

            var functionNameDimension = new Dictionary<string, string>();
            functionNameDimension.Add("function_name", dockerImageFunction.FunctionName);

            insights_metrics.Add(new Metric(new MetricProps()
            {
                MetricName = "memory_utilization",
                Namespace = "LambdaInsights",
                Statistic = "avg",
                DimensionsMap = functionNameDimension,
                Period = Duration.Seconds(10)
            }));

            dashboard.AddWidgets(new GraphWidget(new GraphWidgetProps
            {
                Title = "Insights - Average Memory Utilization",
                Left = insights_metrics.ToArray(),
                Width = 24
            }));
            

            List<Metric> custom_metrics = new List<Metric>();

            var serviceDimension = new Dictionary<string, string>();
            serviceDimension.Add("Service", "ProxyCall");

            custom_metrics.Add(new Metric(new MetricProps()
            {
                MetricName = "Proxy-Request",
                Namespace = "MyDotNetApp",
                Statistic = "sum",
                DimensionsMap = serviceDimension,
                Period = Duration.Seconds(10)
            }));

            custom_metrics.Add(new Metric(new MetricProps()
            {
                MetricName = "Proxy-Successful",
                Namespace = "MyDotNetApp",
                Statistic = "sum",
                DimensionsMap = serviceDimension,
                Period = Duration.Seconds(10)
            }));

            dashboard.AddWidgets(new GraphWidget(new GraphWidgetProps
            {
                Title = "Custom - Number of Requests & Success",
                Left = custom_metrics.ToArray(),
                Width = 24
            }));

        }
    }
}
