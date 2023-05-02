#!/usr/bin/env node

/*
Date : 17-Mar-2023
Author - Gourang Harhare
Role - Sr. Solutions Architect @AWS India
Description: This stack will deploy readymade architecture to receive cloudwatch and custom logs from different accounts and push to splunk cloud or splunk enterprise platform.

*/



import { Duration, Stack, StackProps, CfnParameter, App } from 'aws-cdk-lib';
//import { KinesisDataStreamLogProcessorStack } from '../lib/kinesis-data-stream-log-processor-stack';
import { Function, Runtime, AssetCode, Architecture, StartingPosition } from 'aws-cdk-lib/aws-lambda';
import { KinesisEventSource } from 'aws-cdk-lib/aws-lambda-event-sources';
import * as logDestination from 'aws-cdk-lib/aws-logs-destinations';
import * as kds from 'aws-cdk-lib/aws-kinesis';
import * as iam from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';
import { StreamMode } from 'aws-cdk-lib/aws-kinesis';
import { Effect } from 'aws-cdk-lib/aws-iam';

export class KinesisDataStreamLogProcessorStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);


    const current_account = process.env.CDK_DEFAULT_ACCOUNT;
    const current_region = process.env.CDK_DEFAULT_REGION;

    //Creates new lambda execution role to assume by log processor function
    const lambda_role = new iam.Role(this, "Role", { assumedBy: new iam.ServicePrincipal("lambda.amazonaws.com"), description: "A role for lambda function to assume" });

    //Creates new Kinesis data stream(KDS) with stream mode as on-demand and 2 days of retention period
    const datastream = new kds.Stream(this, "my-first-stream", { streamMode: StreamMode.ON_DEMAND, streamName: 'clw-log-processor-stream', retentionPeriod: Duration.hours(48) });

    //this will grant read-write access on KDS to lambda function. this will be useful for setting KDS as trigger for the lambda function
    datastream.grantReadWrite(lambda_role);

    //create IAM principal record to be added to Log destination role to allow service
    const iam_principal = new iam.ServicePrincipal("logs.amazonaws.com");

    //create inline policy statement to allow any source arn in current account to be able to push logs to log destination
    const policyWithConditions = new iam.PolicyStatement({
      actions: ['sts:AssumeRole'],
      effect: Effect.ALLOW,
      resources: ['*'],
      conditions: {
        'StringLike': {
          'aws:SourceArn': [
            "arn:aws:logs:" + current_region?.toString() + ":" + current_account?.toString() + ":*"
          ]
        }
      }
    });

    //finally create role to be associated with log destination (manual step)
    const log_dest_role = new iam.Role(this, "logDestinationRole", { roleName: "LogDestinationRole", assumedBy: iam_principal });

    //add created inline policy to above created iam role
    log_dest_role.addToPrincipalPolicy(policyWithConditions);


    // additional policy statement for allowing log destination to put records in stream
    const policyWithConditions2 = new iam.PolicyStatement({
      actions: ['kinesis:PutRecord', 'kinesis:PutRecords'],
      effect: Effect.ALLOW,
      resources: [datastream.streamArn]
    });
    // associate policy statement with role created in above steps
    log_dest_role.addToPolicy(policyWithConditions2);


    //create log destination (this doesn't work through CDK and in readme manual step is given)
    const logDest = new logDestination.KinesisDestination(datastream, { role: log_dest_role });

 
    //create event source object to associate KDS as trigger for lambda function in next steps
    const evtSrc = new KinesisEventSource(datastream, { retryAttempts: 3, startingPosition: StartingPosition.LATEST });

    // creates fnLogProcessor function which received log events which is then process and send it to splunk cloud
    const fnLogProcessor = new Function(this, "LogProcessorFunction", {
      functionName: "fnLogProcessor",
      handler: "index.handler",
      runtime: Runtime.NODEJS_14_X,
      code: new AssetCode(`./src`),
      memorySize: 512,
      timeout: Duration.seconds(300),
      environment: {
        BUCKET: "",//s3Bucket.bucketName, 
        SPLUNK_HEC_URL: "", //var_splunk_hec_url.valueAsString,
        SPLUNK_HEC_TOKEN: "" //var_splunk_hec_token.valueAsString
      },
      role: lambda_role,
      architecture: Architecture.X86_64
    });

    //associates event source with lambda function
    fnLogProcessor.addEventSource(evtSrc);









  }
}

//initialize cdk app which will in turn deploy cfn template and above stack.
const app = new App();
new KinesisDataStreamLogProcessorStack(app, 'KinesisDataStreamLogProcessorStack');
