using Amazon.CDK;
using System;
using System.Collections.Generic;
using System.Linq;

namespace Datapipeline
{
    sealed class Program
    {
        public static void Main(string[] args)
        {
            var app = new App();
            var datapipelineStack = new DatapipelineStack(app, "DatapipelineStack");
            var enrichDatapipelineStack = new EnrichDatapipelineStack(app, "EnrichDatapipelineStack", new CrossStackProp
            {
                CrossStackTopic = datapipelineStack.CrossStackTopic,
                CrossStackTable = datapipelineStack.CrossStackTable
            });

            app.Synth();
        }
    }
}
