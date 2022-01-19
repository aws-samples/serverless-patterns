import * as AWSXRay from 'aws-xray-sdk';
import * as AWSSDK from 'aws-sdk';
import { APIGatewayProxyEvent } from "aws-lambda";


const AWS = AWSXRay.captureAWS(AWSSDK);
const docClient = new AWS.DynamoDB.DocumentClient();

const table = process.env.DYNAMODB || "undefined"

const params = {
  TableName : table
}

async function scanItems(){
  try {
    const data = await docClient.scan(params).promise()
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