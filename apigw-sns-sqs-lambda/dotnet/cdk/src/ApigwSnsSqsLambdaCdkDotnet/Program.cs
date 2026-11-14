using Amazon.CDK;

namespace ApigwSnsSqsLambdaCdkDotnet
{
    sealed class Program
    {
        public static void Main(string[] args)
        {
            var app = new App();
            new ApigwSnsSqsLambdaCdkDotnetStack(app, "ApigwSnsSqsLambdaCdkDotnetStack",
            new StackProps
            {
                Env = new Amazon.CDK.Environment
                {
                    Account = System.Environment.GetEnvironmentVariable("CDK_AWS_ACCOUNT"),
                    Region = System.Environment.GetEnvironmentVariable("CDK_AWS_REGION")
                }
            });

            app.Synth();
        }
    }
}
