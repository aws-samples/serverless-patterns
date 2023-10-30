using Amazon.CDK;
using Constructs;
using Amazon.CDK.AWS.ElasticLoadBalancingV2;
using Amazon.CDK.AWS.Lambda;
using Amazon.CDK.AWS.EC2;
using Amazon.CDK.AWS.ElasticLoadBalancingV2.Targets;
using Amazon.CDK.AWS.IAM;

namespace AlbPathBasedRouteLambdaCdk
{
    public class AlbPathBasedRouteLambdaCdkStack : Stack
    {
        internal AlbPathBasedRouteLambdaCdkStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // The code that defines your stack goes here

            // Create a new VPC with two subnets (one per Availability Zone)
            var vpc = new Vpc(this, "DemoVPC", new VpcProps
            {
                MaxAzs = 2, // Specify the desired number of Availability Zones
            });

            // Create an AWS Lambda function
            var lambdaFunction1 = new Function(this, "MyLambdaFunction1", new FunctionProps
            {
                Runtime = Runtime.NODEJS_14_X,
                Handler = "index.handler", // Update with your Lambda handler
                Code = Code.FromAsset("./src/AlbPathBasedRouteLambdaCdk/Lambda1.zip"),
                Vpc = vpc, // Attach the Lambda to the VPC
            });

            // Create an AWS Lambda function
            var lambdaFunction2 = new Function(this, "MyLambdaFunction2", new FunctionProps
            {
                Runtime = Runtime.NODEJS_14_X,
                Handler = "index.handler", // Update with your Lambda handler
                Code = Code.FromAsset("./src/AlbPathBasedRouteLambdaCdk/Lambda2.zip"),
                Vpc = vpc, // Attach the Lambda to the VPC
            });

            // Create an Application Load Balancer
            var loadBalancer = new ApplicationLoadBalancer(this, "MyLoadBalancer", new ApplicationLoadBalancerProps
            {
                Vpc = vpc,
                InternetFacing = true, // Set to false for an internal load balancer
            });

            // Create target group for Lambda
            var targetGroup1 = new ApplicationTargetGroup(this, "MyTargetGroup1", new ApplicationTargetGroupProps
            {                
                Targets = new IApplicationLoadBalancerTarget[] { new LambdaTarget(lambdaFunction1) },
                Vpc = vpc,
            });

            var targetGroup2 = new ApplicationTargetGroup(this, "MyTargetGroup2", new ApplicationTargetGroupProps
            {
                Targets = new IApplicationLoadBalancerTarget[] { new LambdaTarget(lambdaFunction2) },
                Vpc = vpc,
            });

            // Create an ALB listener
            var listener = loadBalancer.AddListener("MyListener", new ApplicationListenerProps
            {
                Port = 80, // Listener port
                DefaultAction = ListenerAction.FixedResponse(200, new FixedResponseOptions
                {
                    ContentType = "text/plain",
                    MessageBody = "Default response from ALB!!!",
                }),
            });

            var pathPatternCondition1 = ListenerCondition.PathPatterns(new[] { "/api/service1*" });
            var pathPatternCondition2 = ListenerCondition.PathPatterns(new[] { "/api/service2*" });

            //Path-based route
            var applicationListnerRule1 = new ApplicationListenerRule(this, "service-lisnerrule-1", new ApplicationListenerRuleProps
            {
                Listener = listener,
                Priority = 100,
                Conditions = new[] {pathPatternCondition1},
                Action = ListenerAction.Forward(new[] { targetGroup1 })
            });

            //Path-based route
            var applicationListnerRule2 = new ApplicationListenerRule(this, "service-lisnerrule-2", new ApplicationListenerRuleProps
            {
                Listener = listener,
                Priority = 101,
                Conditions = new[] { pathPatternCondition2 },
                Action = ListenerAction.Forward(new[] { targetGroup2 })
            });

            // Allow the Application Load Balancer to access Lambda Function
            lambdaFunction1.AddPermission("WithLbFunction1", new Permission
            {
                Action = "lambda:InvokeFunction",
                Principal = new ServicePrincipal("elasticloadbalancing.amazonaws.com"),
                SourceArn = targetGroup1.TargetGroupArn,
            });

            // Allow the Application Load Balancer to access Lambda Function
            lambdaFunction2.AddPermission("WithLbFunction2", new Permission
            {
                Action = "lambda:InvokeFunction",
                Principal = new ServicePrincipal("elasticloadbalancing.amazonaws.com"),
                SourceArn = targetGroup2.TargetGroupArn,
            });

            // Define an output for the ALB URL
            new CfnOutput(this, "AlbUrl", new CfnOutputProps
            {
                Value = $"http://{loadBalancer.LoadBalancerDnsName}",
            });
        }
    }
}
