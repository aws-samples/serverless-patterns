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



            var functionNameDimension = new Dictionary<string, string>();
            functionNameDimension.Add("function_name", dockerImageFunction.FunctionName);

            List<Metric> insights_metrics = new List<Metric>();

            insights_metrics.Add(new Metric(new MetricProps()
            {
                MetricName = "cpu_total_time",
                Namespace = "LambdaInsights",
                Statistic = "avg",
                DimensionsMap = functionNameDimension,
                Period = Duration.Seconds(10)
            }));

            dashboard.AddWidgets(new GraphWidget(new GraphWidgetProps
            {
                Title = "Insights - Average CPU Total Time",
                Left = insights_metrics.ToArray(),
                Width = 24
            }));

            List<Metric> insights_metrics_2 = new List<Metric>();

            insights_metrics_2.Add(new Metric(new MetricProps()
            {
                MetricName = "memory_utilization",
                Namespace = "LambdaInsights",
                Statistic = "avg",
                DimensionsMap = functionNameDimension,
                Period = Duration.Seconds(10)
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

            var gw_1 = new GraphWidget(new GraphWidgetProps
            {
                Title = "Custom - Number of Requests & Success",
                Left = custom_metrics.ToArray(),
                Width = 6,
                View = GraphWidgetView.PIE,
            });

            var gw_2 = new GraphWidget(new GraphWidgetProps
            {
                Title = "Insights - Average Memory Utilization",
                Left = insights_metrics_2.ToArray(),
                Width = 6
            });
            dashboard.AddWidgets(gw_1,gw_2);

        }
    }
}
