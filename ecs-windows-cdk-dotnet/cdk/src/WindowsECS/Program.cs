using Amazon.CDK;

namespace WindowsECS
{
    internal sealed class Program
    {
        public static void Main(string[] args)
        {
            var app = new App();

            var vpcStack = new VPCStack(app, "VPCStack", new StackProps { Env = makeEnv() });
            var securityGroupStack = new SecurityGroupStack(app, "SecurityGroupStack", new StackProps { Env = makeEnv() });
            var albStack = new ALBStack(app, "ALBStack", new StackProps { Env = makeEnv() });
            var windowsECSClusterStack = new WindowsECSClusterStack(app, "WindowsECSClusterStack", new StackProps { Env = makeEnv() });

            securityGroupStack.Node.AddDependency(vpcStack);
            albStack.Node.AddDependency(vpcStack, securityGroupStack);
            windowsECSClusterStack.Node.AddDependency(vpcStack, securityGroupStack, albStack);

            app.Synth();

            Amazon.CDK.Environment makeEnv()
            {
                return new Amazon.CDK.Environment
                {
                    Account = System.Environment.GetEnvironmentVariable("CDK_DEPLOY_ACCOUNT"),
                    Region = System.Environment.GetEnvironmentVariable("CDK_DEPLOY_REGION"),
                };
            }
        }
    }
}