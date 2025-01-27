        import { DynamoDBClient, PutItemCommand } from "@aws-sdk/client-dynamodb";
        const client = new DynamoDBClient({ region: process.env.AWS_REGION });
        export const handler = async (event) => {
          const connectionId = event.requestContext.connectionId;
          console.log("connection ID:", connectionId ); // Print the connection ID
            const putParams = {
              "Item": {
                "connectionId": {
                  "S": connectionId
                },
              },
              "TableName": process.env.TABLE_NAME
            };
          try {
            const command = new PutItemCommand(putParams);
            const response = await client.send(command);
            console.log("put command:", response); // Print the response
            } catch (err) {
              return { statusCode: 500, body: "Failed to connect: " + JSON.stringify(err) };
            }
            return { statusCode: 200, body: "Connected." };
        };