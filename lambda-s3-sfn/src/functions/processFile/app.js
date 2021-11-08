'use strict'

const AWS = require('aws-sdk')
const s3 = new AWS.S3();

exports.handler = async (event) => {
  
  const { Bucket, Key } = event
  
  const params = { Bucket, Key };
  const response = await s3.getObject(params).promise();
  
  console.log("response", response);
    
  const payload = JSON.parse(response.Body.toString('utf-8')).payload
  // Can substitute a more complex processing step here 
  console.log("payload", payload);
  const processedPayload = payload.toLocaleUpperCase()
  
  
  const processedPayloadKey = `${Key.replace("initialPayload", "processedPayload")}`
  const uploadParams = { 
    Bucket: Bucket,
    Key: processedPayloadKey,
    Body: JSON.stringify(processedPayload),
  };    
    
  const stored = await s3.upload(uploadParams).promise()
  console.log("\rSaved processedPayload to ", stored.Location);  

  return { Bucket: Bucket, Key: processedPayloadKey }
}
