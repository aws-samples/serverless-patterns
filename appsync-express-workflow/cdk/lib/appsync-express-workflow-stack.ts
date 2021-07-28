import * as cdk from '@aws-cdk/core';
import {Pass, StateMachine, StateMachineType} from '@aws-cdk/aws-stepfunctions';
import { GraphqlApi, Schema, FieldLogLevel, AuthorizationType, MappingTemplate } from '@aws-cdk/aws-appsync';
import { Role, ServicePrincipal, PolicyStatement } from "@aws-cdk/aws-iam";
import { join } from 'path';

const START_EXECUTION_REQUEST_TEMPLATE = (stateMachineArn: String) => {
  return `
  {
    "version": "2018-05-29",
    "method": "POST",
    "resourcePath": "/",
    "params": {
      "headers": {
        "content-type": "application/x-amz-json-1.0",
        "x-amz-target":"AWSStepFunctions.StartSyncExecution"
      },
      "body": {
        "stateMachineArn": "${stateMachineArn}",
        "name" : "$context.args.execution.name",
        "input": "{ \\\"input\\\": \\\"$context.args.execution.input\\\"}"
      }
    }
  }
`
}


const RESPONSE_TEMPLATE = `
## Raise a GraphQL field error in case of a datasource invocation error
#if($ctx.error)
  $util.error($ctx.error.message, $ctx.error.type)
#end
## if the response status code is not 200, then return an error. Else return the body **
#if($ctx.result.statusCode == 200)
    ## If response is 200, return the body.
  $ctx.result.body
#else
    ## If response is not 200, append the response to error block.
    $utils.appendError($ctx.result.body, $ctx.result.statusCode)
#end
`

export class AppsyncExpressWorkflowStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here
    const stateMachineDefinition = new Pass(this, "passState", {
      result: { value: "Hello from StepFunctions!" }
    });

    const stateMachine = new StateMachine(this, 'SyncStateMachine', {
      definition: stateMachineDefinition,
      stateMachineType: StateMachineType.EXPRESS
    });

    const api = new GraphqlApi(this, 'Api', {
      name: 'SyncStateMachineAPI',
      schema: Schema.fromAsset(join(__dirname, 'schema.graphql')),
      xrayEnabled: true,
      logConfig: {
        excludeVerboseContent: false,
        fieldLogLevel: FieldLogLevel.ALL,
      },
    });

    const appsyncStepFunctionsRole = new Role(this, "SyncStateMachineRole", {
      assumedBy: new ServicePrincipal("appsync.amazonaws.com")
    });
    appsyncStepFunctionsRole.addToPolicy(
      new PolicyStatement({
        resources: ["*"],
        actions: ["states:StartSyncExecution"]
      })
    );

    const endpoint = "https://sync-states." + this.region + ".amazonaws.com/";
    const httpdatasource = api.addHttpDataSource('StepFunctionsStateMachine', endpoint, {
      authorizationConfig: { signingRegion: this.region, signingServiceName: 'states' },
    });

    stateMachine.grant(httpdatasource.grantPrincipal, "states:StartSyncExecution");

    httpdatasource.createResolver({
      typeName: 'Mutation',
      fieldName: 'startExecution',
      requestMappingTemplate: MappingTemplate.fromString(START_EXECUTION_REQUEST_TEMPLATE(stateMachine.stateMachineArn)),
      responseMappingTemplate: MappingTemplate.fromString(RESPONSE_TEMPLATE)
    })


    new cdk.CfnOutput(this, 'graphqlUrl', { value: api.graphqlUrl })
    new cdk.CfnOutput(this, 'apiKey', { value: api.apiKey! })
    new cdk.CfnOutput(this, 'apiId', { value: api.apiId })
    new cdk.CfnOutput(this, 'stateMachine', {value: stateMachine.stateMachineArn})
  }
}
