import { DynamoDBClient, ScanCommand, DeleteItemCommand } from "@aws-sdk/client-dynamodb";
import { ApiGatewayManagementApiClient, PostToConnectionCommand } from "@aws-sdk/client-apigatewaymanagementapi";
const ddbClient = new DynamoDBClient({ region: process.env.AWS_REGION });

export const handler = async (event) => {
  let connectionData;

  //scanning DB table to get the Connection ID
  const scanParams = {
    TableName: process.env.TABLE_NAME,
    ProjectionExpression: "connectionId",
  };
  
  const scanCommand = new ScanCommand(scanParams);
  const responseDynamo = await ddbClient.send(scanCommand);
  connectionData = responseDynamo.Items;
  const connectionId = connectionData[0].connectionId.S;
  console.log("connectionData:", connectionData); // print info about the DB connection
  
  //building endpoint from env variables, can also be buit from request parameters 
  const endpoint = "https://" + process.env.API_ID + ".execute-api." + process.env.AWS_REGION + ".amazonaws.com/" + process.env.STAGE + "/";
  
  const apigwManagementApi = new ApiGatewayManagementApiClient({ apiVersion: "2018-11-29",
    endpoint: endpoint,
  });

  //parameters to post response to the connectionId
  const postParams = {
    ConnectionId: connectionId,
    Data: "good job on deploying this template, keep slaying!!",
  };

  try{
    const postCommand = new PostToConnectionCommand(postParams);
    const responseApi = await apigwManagementApi.send(postCommand);
    console.log("response:", responseApi); //print the response
  } catch (err) {
    return { statusCode: 500, body: "Failed to connect: " + JSON.stringify(err) };
  }
  
  return { statusCode: 200, body: "Data sent" };
};