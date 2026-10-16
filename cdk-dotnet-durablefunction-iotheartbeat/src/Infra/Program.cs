using Amazon.CDK;

namespace Infra;

sealed class Program
{
    public static void Main()
    {
        var app = new App();
        new InfraStack(app, "CdkDotnetDurablefunctionIotheartbeatStack", new StackProps
        {
            Env = new Amazon.CDK.Environment
            {
                Account = System.Environment.GetEnvironmentVariable("CDK_DEFAULT_ACCOUNT"),
                Region = System.Environment.GetEnvironmentVariable("CDK_DEFAULT_REGION"),
            }
        });
        app.Synth();
    }
}
