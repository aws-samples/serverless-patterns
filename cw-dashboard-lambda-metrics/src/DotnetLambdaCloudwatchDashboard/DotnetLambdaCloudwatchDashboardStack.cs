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
            var assetImageCodeProps = new AssetImageCodeProps
            {
                BuildArgs = new Dictionary<string, string> {
                //ARM - https://lambda-insights-extension-arm64.s3-ap-northeast-1.amazonaws.com/amazon_linux/lambda-insights-extension-arm64.rpm 
                { "URL", "https://lambda-insights-extension.s3-ap-northeast-1.amazonaws.com/amazon_linux/" },
                {"INSIGHTSEXTENSION","lambda-insights-extension.rpm"}
                }
            };
            // The code that defines your stack goes here
            DockerImageCode dockerImageCode = DockerImageCode.FromImageAsset("src/lambda/proxy-lambda", assetImageCodeProps);

            // Lambda from Image
            DockerImageFunction dockerImageFunction = new DockerImageFunction(this,
                "container-image-lambda-function",
                new DockerImageFunctionProps()
                {
                    Code = dockerImageCode,
                    Description = ".NET 6 Docker Lambda function",
                    Timeout = Duration.Minutes(1)
                });

            var dashboard = new Dashboard(this, "DotnetCDKDashboard");

            List<Metric> invocations_metrics = new List<Metric>();
            invocations_metrics.Add(dockerImageFunction.MetricInvocations(new MetricOptions() { Period = Duration.Seconds(10) }));

            var functionNameDimension = new Dictionary<string, string>();
            functionNameDimension.Add("function_name", dockerImageFunction.FunctionName);

            List<Metric> insightsMetrics = new List<Metric>();

            insightsMetrics.Add(new Metric(new MetricProps()
            {
                MetricName = "cpu_total_time",
                Namespace = "LambdaInsights",
                Statistic = "avg",
                DimensionsMap = functionNameDimension,
                Period = Duration.Seconds(10)
            }));



            List<Metric> insightsMetrics2 = new List<Metric>();

            insightsMetrics2.Add(new Metric(new MetricProps()
            {
                MetricName = "memory_utilization",
                Namespace = "LambdaInsights",
                Statistic = "avg",
                DimensionsMap = functionNameDimension,
                Period = Duration.Seconds(10)
            }));

            List<Metric> customMetrics = new List<Metric>();

            var serviceDimension = new Dictionary<string, string>();
            serviceDimension.Add("Service", "ProxyCall");

            customMetrics.Add(new Metric(new MetricProps()
            {
                MetricName = "Proxy-Request",
                Namespace = "MyDotNetApp",
                Statistic = "sum",
                DimensionsMap = serviceDimension,
                Period = Duration.Seconds(10)
            }));

            customMetrics.Add(new Metric(new MetricProps()
            {
                MetricName = "Proxy-Successful",
                Namespace = "MyDotNetApp",
                Statistic = "sum",
                DimensionsMap = serviceDimension,
                Period = Duration.Seconds(10)
            }));

            var graphwidget1 = new GraphWidget(new GraphWidgetProps
            {
                Title = "Custom - Number of Requests & Success",
                Left = customMetrics.ToArray(),
                Width = 6,
                View = GraphWidgetView.PIE,
            });


            var graphwidget2 = new GraphWidget(new GraphWidgetProps
            {
                Title = "Insights - Average Memory Utilization",
                Left = insightsMetrics2.ToArray(),
                Width = 6
            });

            dashboard.AddWidgets(new TextWidget(new TextWidgetProps
            {
                Markdown = "# Key Performance Indicators",
                Width = 24,
                Height = 1
            }));

            dashboard.AddWidgets(graphwidget1, graphwidget2);

            dashboard.AddWidgets(new GraphWidget(new GraphWidgetProps
            {
                Title = "Invocations",
                Left = invocations_metrics.ToArray(),
                Width = 24
            }));

            dashboard.AddWidgets(new GraphWidget(new GraphWidgetProps
            {
                Title = "Insights - Average CPU Total Time",
                Left = insightsMetrics.ToArray(),
                Width = 24
            }));
        }
    }
}
