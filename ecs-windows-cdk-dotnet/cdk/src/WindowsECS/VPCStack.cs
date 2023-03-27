using Amazon.CDK;
using Amazon.CDK.AWS.EC2;
using Constructs;

namespace WindowsECS
{
    public class VPCStack : Stack
    {
        public static Vpc vpc;

        internal VPCStack(Construct scope, string id, IStackProps props = null) : base(scope, id, props)
        {
            // The code that defines your stack goes here
            // Create new VPC
            vpc = CreateVPC();
        }

        private Vpc CreateVPC()
        {
            // It will automatically divide the provided VPC CIDR range, and create public and private subnets per Availability Zone. Network routing for the public subnets will be configured to allow outbound access directly via an Internet Gateway. Network routing for the private subnets will be configured to allow outbound access via a set of resilient NAT Gateways (one per AZ).
            return new Vpc(this, "DemoVpc", new VpcProps
            {
                MaxAzs = 2
            });
        }
    }
}