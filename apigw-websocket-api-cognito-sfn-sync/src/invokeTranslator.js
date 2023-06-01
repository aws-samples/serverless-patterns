const AWS = require('aws-sdk');
const apig = new AWS.ApiGatewayManagementApi({
    endpoint: process.env.APIG_ENDPOINT,
  });

module.exports.handler = async (event, context) => {
  const { requestContext: { connectionId, routeKey }} = event;

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

  if (routeKey === "getConnectionId") {
    await apig
    .postToConnection({
        ConnectionId: connectionId,
        Data: JSON.stringify( {"connectionId" : connectionId} )
    }).promise();
    
    return {
      statusCode: 200
    }
  }

  return {
    statusCode: 200
  }
}
