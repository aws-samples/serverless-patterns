'use strict'

const { S3Client, GetObjectCommand } = require('@aws-sdk/client-s3')
const s3 = new S3Client();

exports.handler = async (event) => {
  
  const { Bucket, Key } = event
  
  const params = { Bucket, Key };
  const response = await s3.send(new GetObjectCommand(params));
  
  console.log(response)  
  const processedPayload = JSON.parse(await response.Body.transformToString('utf-8'))
  
  console.log("processedPayload", processedPayload) 
  const processedPayloadWithFooter = `${processedPayload} ***** Processed by lambda-s3-sfn serverless Pattern - https://serverlessland.com/patterns  *****`
  console.log("processedPayloadWithFooter", processedPayloadWithFooter) 

  return processedPayloadWithFooter
}