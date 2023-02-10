using Amazon.CDK;

namespace DynamoPipeSqs;

sealed class Program
{
    public static void Main(string[] args)
    {
        var app = new App();
        new DynamoPipeSqsStack(app, "DynamoPipeSqsStack");

        app.Synth();
    }
}
