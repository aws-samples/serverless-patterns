const AWS = require('aws-sdk');
const stepfunctions = new AWS.StepFunctions();
const apig = new AWS.ApiGatewayManagementApi({
    endpoint: process.env.APIG_ENDPOINT,
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
  let response = await stepfunctions.startSyncExecution(params).promise();
  await apig
    .postToConnection({
        ConnectionId: connectionId,
        Data: response?JSON.stringify( {"url" : JSON.parse(response.output).url} ):"No data"
    }).promise();
  if ( response && response.output)
    response = {"url" : JSON.parse(response.output).url}
  return {
    statusCode: 200
  }
}
