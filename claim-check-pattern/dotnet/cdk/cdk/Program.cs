using Amazon.CDK;

namespace Cdk
{
    public sealed class Program
    {
        public static void Main(string[] args)
        {
            var app = new App();
            _ = new CdkStack(app, "ClaimCheckPatternDotnet", new StackProps
            {
                Description = "Serverless .NET implementation of the Claim Check Pattern"
            });
            app.Synth();
        }
    }
}
