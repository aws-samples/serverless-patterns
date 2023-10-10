using Amazon.CDK;
using Amazon.CDK.AWS.SNS;
using Amazon.CDK.AWS.DynamoDB;
using System;
using System.Collections.Generic;
using System.Text;

namespace Datapipeline
{
    internal class CrossStackProp : StackProps
    {
        public Topic CrossStackTopic { get; set; }
        public Table CrossStackTable { get; set; }
    }

}
