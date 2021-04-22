'use strict'

const AWS = require('aws-sdk')
const s3 = new AWS.S3();

exports.handler = async (event) => {
  
  const { Bucket, Key } = event
  
  const params = { Bucket, Key };
  const response = await s3.getObject(params).promise();
    
  const processedPayload = JSON.parse(response.Body.toString('utf-8'))  
  let processedPayloadWithFooter = `${processedPayload}\r\r ***** Brought to you by Serverless Patterns - https://serverlessland.com/patterns  *****`

  return processedPayloadWithFooter
}