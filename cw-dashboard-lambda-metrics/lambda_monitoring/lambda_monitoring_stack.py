from aws_cdk import (
    CfnOutput,
    Stack,
    Duration,
    aws_cloudwatch,
    aws_iam,
    aws_lambda,
    aws_lambda_python_alpha,
    aws_apigateway
)
from constructs import Construct

class LambdaMonitoringStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        managed_policy_insights = aws_iam.ManagedPolicy.from_aws_managed_policy_name(
            'CloudWatchLambdaInsightsExecutionRolePolicy')
        
        managed_policy_basic_exec = aws_iam.ManagedPolicy.from_aws_managed_policy_name(
            'service-role/AWSLambdaBasicExecutionRole')
        
        lambda_role = aws_iam.Role(self,
                               id='cdk-lambda-role',
                               assumed_by=aws_iam.ServicePrincipal(
                                   'lambda.amazonaws.com'),
                               managed_policies=[managed_policy_insights, managed_policy_basic_exec])
        
        lambdaLayer_insights = aws_lambda.LayerVersion.from_layer_version_arn(
                                    self, 
                                    "Cw-inisghts-layer",
                                    layer_version_arn="arn:aws:lambda:us-east-1:580247275435:layer:LambdaInsightsExtension:21"
                                )
    
        
        lambda_handler = aws_lambda_python_alpha.PythonFunction(
                            self, 
                            "MyFunction",
                            entry="./src_lambda/",  # required
                            runtime=aws_lambda.Runtime.PYTHON_3_9,  # required
                            index="handler.py",  # optional, defaults to 'index.py'
                            handler="lambda_handler",
                            role=lambda_role,
                            layers=[lambdaLayer_insights]
                        )
        
        CfnOutput(
            self, 
            "LAMBDA FUNCTION NAME", 
            value=lambda_handler.function_name
        )
        
        title_widget = aws_cloudwatch.TextWidget(
                            markdown="# Dashboard: {}".format(lambda_handler.function_name),
                            height=1,
                            width=24
                        )

        innvocation_widget_1 = aws_cloudwatch.GraphWidget(
                                    title="Invocations",
                                    left=[lambda_handler.metric_invocations()],
                                    width=24
                                )
        
        dimensions_function_name = {
            "function_name": lambda_handler.function_name
        }

        memory_metric = aws_cloudwatch.Metric(
                            metric_name="memory_utilization", 
                            namespace="LambdaInsights", 
                            statistic="avg",
                            dimensions_map=dimensions_function_name, 
                            period=Duration.seconds(10)
                        )

        innvocation_widget_2 = aws_cloudwatch.GraphWidget(
                                    title="Memory Utilization - From LambdaInsights",
                                    left=[memory_metric],
                                    width=24
                                )

        dimensions_service = {
            "service": "CWMApp-Lambda"
        }

        Response_200 = aws_cloudwatch.Metric(
                                    metric_name="Response_200", 
                                    namespace="CWMApp", 
                                    statistic="sum",
                                    dimensions_map=dimensions_service,
                                    period=Duration.seconds(10)
                                )
        
        Response_500 = aws_cloudwatch.Metric(
                                    metric_name="Response_500", 
                                    namespace="CWMApp", 
                                    statistic="sum",
                                    dimensions_map=dimensions_service,
                                    period=Duration.seconds(10)
                                )
        
        innvocation_widget_3 = aws_cloudwatch.GraphWidget(
                                    title="Count - From Custom Metrics",
                                    left=[Response_200, Response_500],
                                    width=24
                                )
        
        dashboard = aws_cloudwatch.Dashboard(
            self, "MyFirstDashboard",
            dashboard_name="LambdaCDKDashboard",
            )
        
        dashboard.add_widgets(
                title_widget, 
                innvocation_widget_1, 
                innvocation_widget_2, 
                innvocation_widget_3
            )


