const { SFNClient, StartSyncExecutionCommand } = require('@aws-sdk/client-sfn');
const { ApiGatewayManagementApiClient, PostToConnectionCommand } = require('@aws-sdk/client-apigatewaymanagementapi');
const stepfunctions = new SFNClient({});
const apig = new ApiGatewayManagementApiClient({
    endpoint: `https://${process.env.APIG_ENDPOINT}`,
  });

module.exports.handler = async (event, context) => {
  const { body, requestContext: { connectionId, routeKey }} = event;

  if (routeKey === "$connect") {
    // handle new connection
    
    return {
      statusCode: 200
    }
  }
  if (routeKey === "$disconnect") {
    // handle disconnection
    return {
      statusCode: 200
    }
  }

  let params = {
      stateMachineArn: process.env.statemachine_arn,
      input: body
  }
  let response = await stepfunctions.send(new StartSyncExecutionCommand(params));
  await apig.send(new PostToConnectionCommand({
        ConnectionId: connectionId,
        Data: response?JSON.stringify( {"url" : JSON.parse(response.output).url} ):"No data"
    }));
  if ( response && response.output)
    response = {"url" : JSON.parse(response.output).url}
  return {
    statusCode: 200
  }
}
