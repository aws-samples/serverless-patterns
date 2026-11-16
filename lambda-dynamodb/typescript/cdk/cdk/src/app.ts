/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
*/

import { DynamoDBClient } from '@aws-sdk/client-dynamodb';
import { DynamoDBDocumentClient, PutCommand } from '@aws-sdk/lib-dynamodb';
const moment = require('moment');

const documentClient = DynamoDBDocumentClient.from(new DynamoDBClient({}));

export async function main( event: any ) {
  let params = {
    TableName : process.env.DatabaseTable,
    Item: {
      ID: Math.floor(Math.random() * Math.floor(10000000)).toString(),
      created: moment().format('YYYYMMDD-hhmmss'),
      metadata:JSON.stringify(event),
    }
  }
  try {
    let data = await documentClient.send(new PutCommand(params));
  }
  catch (err) {
    console.log(err);
    return err;
  }
  return {
    statusCode: 200,
    body: 'OK!',
  };
}