using Amazon.CDK;
using System;
using System.Collections.Generic;
using System.Linq;

namespace S3Lambda
{
    sealed class Program
    {
        public static void Main(string[] args)
        {
            var app = new App();
            new S3LambdaStack(app, "S3LambdaStack");
            app.Synth();
        }
    }
}
