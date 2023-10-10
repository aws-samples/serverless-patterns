using Amazon.CDK;
using System;
using System.Collections.Generic;
using System.Linq;

namespace Mdsite
{
    sealed class Program
    {
        public static void Main(string[] args)
        {
            var app = new App();
            new MdsiteStack(app, "markdown-site-cdkstack");
            app.Synth();
        }
    }
}
