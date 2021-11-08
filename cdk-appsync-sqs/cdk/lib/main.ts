import * as sqs from '@aws-cdk/aws-sqs'
import * as cdk from '@aws-cdk/core'
import * as appsync from '@aws-cdk/aws-appsync'
import { join } from 'path'

const REQUEST_TEMPLATE = (accountId: String, queue: sqs.Queue) => {
  return `
#set ($body = "Action=SendMessage&Version=2012-11-05")
#set ($messageBody = $util.urlEncode($util.toJson($ctx.args)))
#set ($queueUrl = $util.urlEncode("${queue.queueUrl}"))
#set ($body = "$body&MessageBody=$messageBody&QueueUrl=$queueUrl")

{
  "version": "2018-05-29",
  "method": "POST",
  "resourcePath": "/${accountId}/${queue.queueName}",
  "params": {
    "body": "$body",
    "headers": {
      "content-type": "application/x-www-form-urlencoded"
    }
  }
}
`
}

const RESPONSE_TEMPLATE = `
#if($ctx.result.statusCode == 200)
    ##if response is 200
    ## Because the response is of type XML, we are going to convert
    ## the result body as a map and only get the User object.
    $utils.toJson($utils.xml.toMap($ctx.result.body).SendMessageResponse.SendMessageResult)
#else
    ##if response is not 200, append the response to error block.
    $utils.appendError($ctx.result.body, "$ctx.result.statusCode")
    null
#end
`

export class CdkAppSyncSqSStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props)

    const region = cdk.Stack.of(this).region
    const account = cdk.Stack.of(this).account

    const api = new appsync.GraphqlApi(this, 'Api', {
      name: 'ToSqSApi',
      schema: appsync.Schema.fromAsset(join(__dirname, 'schema.graphql')),
    })

    const queue = new sqs.Queue(this, 'queue')
    const datasource = api.addHttpDataSource('sqs', `https://sqs.${region}.amazonaws.com`, {
      authorizationConfig: { signingRegion: region, signingServiceName: 'sqs' },
    })
    datasource.node.addDependency(queue)
    queue.grantSendMessages(datasource.grantPrincipal)

    datasource.createResolver({
      typeName: 'Query',
      fieldName: 'sendMessage',
      requestMappingTemplate: appsync.MappingTemplate.fromString(REQUEST_TEMPLATE(account, queue)),
      responseMappingTemplate: appsync.MappingTemplate.fromString(RESPONSE_TEMPLATE),
    })

    new cdk.CfnOutput(this, 'graphqlUrl', { value: api.graphqlUrl })
    new cdk.CfnOutput(this, 'apiKey', { value: api.apiKey! })
    new cdk.CfnOutput(this, 'apiId', { value: api.apiId })
    new cdk.CfnOutput(this, 'queueUrl', { value: queue.queueUrl })
  }
}
