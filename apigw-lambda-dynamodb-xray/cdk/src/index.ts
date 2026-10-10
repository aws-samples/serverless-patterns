import * as AWSXRay from 'aws-xray-sdk-core';
import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, ScanCommand } from '@aws-sdk/lib-dynamodb';
import { APIGatewayProxyEvent } from "aws-lambda";

const client = AWSXRay.captureAWSv3Client(new DynamoDBClient({}));
const docClient = DynamoDBDocumentClient.from(client);

const table = process.env.DYNAMODB || "undefined"

const params = {
  TableName : table
}

async function scanItems(){
  try {
    const data = await docClient.send(new ScanCommand(params))
    return data
  } catch (err) {
    return err
  }
}

exports.handler = async (event:APIGatewayProxyEvent) => {
  try {
    console.log(event)
    const data = await scanItems()
    return { body: JSON.stringify(data) }
  } catch (err) {
    return { error: err }
  }
}