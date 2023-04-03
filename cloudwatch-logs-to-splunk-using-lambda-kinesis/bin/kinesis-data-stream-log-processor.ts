#!/usr/bin/env node
import { Duration, Stack, StackProps, CfnParameter, App } from 'aws-cdk-lib';
//import { KinesisDataStreamLogProcessorStack } from '../lib/kinesis-data-stream-log-processor-stack';
import { Function, Runtime, AssetCode, Architecture,  StartingPosition } from 'aws-cdk-lib/aws-lambda';
import {KinesisEventSource} from 'aws-cdk-lib/aws-lambda-event-sources';
import * as logDestination from 'aws-cdk-lib/aws-logs-destinations';
import * as kds from 'aws-cdk-lib/aws-kinesis';
import * as s3 from 'aws-cdk-lib/aws-s3';
import * as iam from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';
import { StreamMode } from 'aws-cdk-lib/aws-kinesis';
import { Effect } from 'aws-cdk-lib/aws-iam';

export class KinesisDataStreamLogProcessorStack extends Stack {
    constructor(scope: Construct, id: string, props?: StackProps) {
      super(scope, id, props);
  
  
      const current_account = process.env.CDK_DEFAULT_ACCOUNT;
      const current_region = process.env.CDK_DEFAULT_REGION;
  
/*       const var_splunk_hec_url = new CfnParameter(this, "SPLUNK_HEC_URL", {  type: "String", description: "Please provide URL of splunk host or splunk cloud endpoint"});
  
        const var_splunk_hec_token = new CfnParameter(this, "SPLUNK_HEC_TOKEN", {
          type: "String",
          description: "Please provide HEC token provided by Splunk for HTTP event collector"}); */
  
      //const s3Bucket = new s3.Bucket(this, "backupBucket",{bucketName:"clw-log-backup" });
  
      const lambda_role = new iam.Role(this, "Role",{assumedBy:new iam.ServicePrincipal("lambda.amazonaws.com"), description: "A role for lambda function to assume" });
  
      const datastream = new kds.Stream(this, "my-first-stream",{streamMode: StreamMode.ON_DEMAND, streamName: 'clw-log-processor-stream', retentionPeriod:Duration.hours(48)});
  
      datastream.grantReadWrite(lambda_role);
  
      //s3Bucket.grantReadWrite(lambda_role);
     // s3Bucket.grantPut(lambda_role);

      const iam_principal = new iam.ServicePrincipal("logs.amazonaws.com");

      const policyWithConditions = new iam.PolicyStatement({
        actions:['sts:AssumeRole'],
        effect: Effect.ALLOW,
        resources: ['*'],
        conditions: {
            'StringLike': {
                'aws:SourceArn': [
                    "arn:aws:logs:"+ current_region?.toString() +":"+ current_account?.toString() + ":*"
                    ]
                }
            }
        });

        const log_dest_role = new iam.Role(this, "logDestinationRole",{roleName:"LogDestinationRole",assumedBy: iam_principal });

        log_dest_role.addToPrincipalPolicy(policyWithConditions);



        const policyWithConditions2 = new iam.PolicyStatement({
            actions:['kinesis:PutRecord','kinesis:PutRecords'],
            effect: Effect.ALLOW,
            resources: [datastream.streamArn]
            });
  
         log_dest_role.addToPolicy(policyWithConditions2);

      
  
      const logDest = new logDestination.KinesisDestination(datastream,{role: log_dest_role});

      console.log (logDest);
  
      const evtSrc = new KinesisEventSource(datastream,{retryAttempts:3, startingPosition: StartingPosition.LATEST});
  
  
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
  
      fnLogProcessor.addEventSource(evtSrc);
  
  
  
  
      
      
  
  
  
    }
  }

  const app = new App();
  new KinesisDataStreamLogProcessorStack(app, 'KinesisDataStreamLogProcessorStack');
  