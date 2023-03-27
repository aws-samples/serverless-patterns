using Amazon.CDK;
using Amazon.CDK.AWS.EC2;
using Constructs;

namespace WindowsECS
{
    public class SecurityGroupStack : Stack
    {
        public static SecurityGroup alb_sg;
        private Vpc vpc = VPCStack.vpc;

        internal SecurityGroupStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // The code that defines your stack goes here
            //Create Security Group which will be attached to the ALB
            alb_sg = CreateSecurityGroup(vpc);
        }

        private SecurityGroup CreateSecurityGroup(Vpc vpc)
        {
            var alb_sg = new SecurityGroup(this, "AlbSecurityGroup", new SecurityGroupProps
            {
                Vpc = vpc,
                SecurityGroupName = "Windows-alb-security-group",
                AllowAllOutbound = true
            });

            // Adding Inbound rule for ALB
            alb_sg.AddIngressRule(Peer.AnyIpv4(), Port.Tcp(80), "Allows HTTPS access from Internet to ALB");
            Amazon.CDK.Tags.Of(alb_sg).Add("Name", "Windows-alb-security-group");
            return alb_sg;
        }
    }
}