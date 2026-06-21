using Amazon.CDK;

namespace Cdk;

internal sealed class Program
{
    public static void Main(string[] args)
    {
        var app = new App();
        new LambdaS3FilesStack(app, "LambdaS3FilesStack", new StackProps
        {
            // Uncomment to specialize this stack for the AWS Account and Region
            // that are implied by the current CLI configuration.
            /*
            Env = new Amazon.CDK.Environment
            {
                Account = System.Environment.GetEnvironmentVariable("CDK_DEFAULT_ACCOUNT"),
                Region = System.Environment.GetEnvironmentVariable("CDK_DEFAULT_REGION"),
            }
            */
        });
        app.Synth();
    }
}
