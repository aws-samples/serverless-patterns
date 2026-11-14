import fs from "fs";
import zlib from "zlib";
import process from "process";
import { pipeline } from "stream";
import { promisify } from "util";
import { DynamoDBClient, PutItemCommand } from "@aws-sdk/client-dynamodb";
import { marshall } from "@aws-sdk/util-dynamodb";
const dynamodb = new DynamoDBClient();
const tableName = process.env.DDB_TABLE_NAME;

const pipelineAsync = promisify(pipeline);

// Function to read and unzip the .gz file directly
const readAndUnzipJson = async (gzFilePath) => {
  const gunzip = zlib.createGunzip();
  const input = fs.createReadStream(gzFilePath);
  let data = "";
  await pipelineAsync(input, gunzip, async (source) => {
    for await (const chunk of source) {
      data += chunk;
    }
  });
  return JSON.parse(data);
};

// Function to dump JSON data to DynamoDB
const dumpToDynamoDB = async (jsonData) => {
  const promises = jsonData.map(async (item) => {
    console.log(`Dumping item ${JSON.stringify(item)}`);
    const command = new PutItemCommand({
      TableName: tableName,
      Item: marshall(item),
    });
    return dynamodb.send(command);
  });
  await Promise.all(promises);
};

export const handler = async (event) => {
  try {
    const gzFilePath = "data.json.gz";
    const jsonData = await readAndUnzipJson(gzFilePath);
    await dumpToDynamoDB(jsonData);

    return {
      statusCode: 200,
      body: "Data dump successful",
    };
  } catch (error) {
    console.error("Error:", error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: "Failed to process the data" }),
    };
  }
};
