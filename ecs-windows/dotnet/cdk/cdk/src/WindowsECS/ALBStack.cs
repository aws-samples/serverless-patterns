using Amazon.CDK;
using Amazon.CDK.AWS.EC2;
using Amazon.CDK.AWS.ElasticLoadBalancingV2;
using Constructs;
using System.Collections.Generic;
using HealthCheck = Amazon.CDK.AWS.ElasticLoadBalancingV2.HealthCheck;

namespace WindowsECS
{
    public class ALBStack : Stack
    {
        public static List<ApplicationTargetGroup> applicationWindowsTargetGroupsList = new();
        public static List<string> applicationWindowsTargetGroupsArnList = new();
        private Vpc vpc = VPCStack.vpc;
        private SecurityGroup alb_sg = SecurityGroupStack.alb_sg;

        internal ALBStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // The code that defines your stack goes here
            // Create Windows Target Groups
            string[] windowsTargetGroups = new string[] { "blue", "green" };

            CreateTargetGroups(vpc, windowsTargetGroups, applicationWindowsTargetGroupsList, applicationWindowsTargetGroupsArnList);

            // Create Application Load Balancer
            _ = CreateApplicationLoadBalancer(vpc, alb_sg, applicationWindowsTargetGroupsArnList);
        }

        private ApplicationLoadBalancer CreateApplicationLoadBalancer(Vpc vpc, SecurityGroup alb_sg, List<string> applicationWindowsTargetGroupsArnList)
        {
            var alb = new ApplicationLoadBalancer(this, "ApplicationLoadBalancerWindows", new ApplicationLoadBalancerProps
            {
                Vpc = vpc,
                SecurityGroup = alb_sg,
                VpcSubnets = new SubnetSelection
                {
                    SubnetType = SubnetType.PUBLIC
                },
                InternetFacing = true
            });

            Amazon.CDK.Tags.Of(alb).Add("Name", "app-load-balancer-Windows");
            _ = alb.AddListener("ApplicationListenerWindows", new BaseApplicationListenerProps
            {
                Port = 80,
                DefaultAction = new ListenerAction(
                      new CfnListener.ActionProperty
                      {
                          Type = "forward",
                          TargetGroupArn = applicationWindowsTargetGroupsArnList[0]
                      })
            });

            _= new CfnOutput(this, "ApplicationLoadBalancerOutput", new CfnOutputProps
            {
                Value = alb.LoadBalancerDnsName,
                Description = "The DNS name for the load balancer"
            });

            return alb;
        }

        private void CreateTargetGroups(Vpc vpc, string[] windowsTargetGroups, List<ApplicationTargetGroup> applicationWindowsTargetGroupsList, List<string> applicationWindowsTargetGroupsArnList)
        {
            foreach (string windowsTargetGroup in windowsTargetGroups)
            {
                var applicationWindowsTargetGroup = new ApplicationTargetGroup(this, "ApplicationWindowsTargetGroup" + windowsTargetGroup, new ApplicationTargetGroupProps
                {
                    Port = 80,
                    Protocol = ApplicationProtocol.HTTP,
                    TargetType = TargetType.INSTANCE,
                    Vpc = vpc,
                    HealthCheck = new HealthCheck { Path = "/" }
                });

                applicationWindowsTargetGroupsList.Add(applicationWindowsTargetGroup);
                applicationWindowsTargetGroupsArnList.Add(applicationWindowsTargetGroup.TargetGroupArn);
            }
        }
    }
}