using Amazon.CDK;

namespace WindowsECS
{
    internal sealed class Program
    {
        public static void Main(string[] args)
        {
            var app = new App();

            var vpcStack = new VPCStack(app, "VPCStack", new StackProps());
            var securityGroupStack = new SecurityGroupStack(app, "SecurityGroupStack", new StackProps());
            var albStack = new ALBStack(app, "ALBStack", new StackProps());
            var windowsECSClusterStack = new WindowsECSClusterStack(app, "WindowsECSClusterStack", new StackProps());

            securityGroupStack.Node.AddDependency(vpcStack);
            albStack.Node.AddDependency(vpcStack, securityGroupStack);
            windowsECSClusterStack.Node.AddDependency(vpcStack, securityGroupStack, albStack);

            app.Synth();
        }
    }
}