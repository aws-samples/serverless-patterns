using Amazon.CDK;
using System;
using System.Collections.Generic;
using System.Linq;

namespace StaticSite
{
    sealed class Program
    {
        public static void Main(string[] args)
        {
            var app = new App();
            new StaticSiteStack(app, "StaticSiteStack");
            app.Synth();
        }
    }
}
