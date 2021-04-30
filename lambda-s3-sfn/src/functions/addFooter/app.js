'use strict'

const AWS = require('aws-sdk')
const s3 = new AWS.S3();

exports.handler = async (event) => {
  
  const { Bucket, Key } = event
  
  const params = { Bucket, Key };
  const response = await s3.getObject(params).promise();
  
  console.log(response)  
  const processedPayload = JSON.parse(response.Body.toString('utf-8'))
  
  console.log("processedPayload", processedPayload) 
  const processedPayloadWithFooter = `${processedPayload} ***** Processed by lambda-s3-sfn serverless Pattern - https://serverlessland.com/patterns  *****`
  console.log("processedPayloadWithFooter", processedPayloadWithFooter) 

  return processedPayloadWithFooter
}