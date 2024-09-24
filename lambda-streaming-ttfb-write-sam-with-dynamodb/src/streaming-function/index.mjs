import { DynamoDBClient, ScanCommand } from "@aws-sdk/client-dynamodb";
import { unmarshall } from "@aws-sdk/util-dynamodb";
const dynamodb = new DynamoDBClient();
const tableName = process.env.DDB_TABLE_NAME;

export const handler = awslambda.streamifyResponse(
  async (event, responseStream, context) => {
    const httpResponseMetadata = {
      statusCode: 200,
      headers: {
        "Content-Type": "text/html",
      },
    };

    responseStream = awslambda.HttpResponseStream.from(
      responseStream,
      httpResponseMetadata
    );

    let counter = 0;
    await scanDynamoDBTable();

    async function scanDynamoDBTable(startKey = null) {
      // Scan table with the required parameters
      const scan = new ScanCommand({
        TableName: tableName,
        ExclusiveStartKey: startKey,
        Limit: 200,
      });

      const data = await dynamodb.send(scan);

      // Convert the items from DDB JSON to regular JSON
      data.Items = data.Items.map((item) => {
        return unmarshall(item);
      });

      // Send the scan result to the stream
      responseStream.write(data.Items);

      counter += 1;

      // If there are more items to scan, recursively call the scanDynamoDBTable function with the last evaluated key
      if (data.LastEvaluatedKey && counter < 10) {
        return scanDynamoDBTable(data.LastEvaluatedKey);
      }

      // End stream
      responseStream.end();
    }
  }
);
