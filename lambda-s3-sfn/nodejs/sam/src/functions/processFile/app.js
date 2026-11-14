'use strict'

const { S3Client, GetObjectCommand, PutObjectCommand } = require('@aws-sdk/client-s3')
const s3 = new S3Client();

exports.handler = async (event) => {
  
  const { Bucket, Key } = event
  
  const params = { Bucket, Key };
  const response = await s3.send(new GetObjectCommand(params));
  
  console.log("response", response);
    
  const payload = JSON.parse(await response.Body.transformToString('utf-8')).payload
  // Can substitute a more complex processing step here 
  console.log("payload", payload);
  const processedPayload = payload.toLocaleUpperCase()
  
  
  const processedPayloadKey = `${Key.replace("initialPayload", "processedPayload")}`
  const uploadParams = { 
    Bucket: Bucket,
    Key: processedPayloadKey,
    Body: JSON.stringify(processedPayload),
  };    
    
  await s3.send(new PutObjectCommand(uploadParams))
  console.log("\rSaved processedPayload to ", `s3://${Bucket}/${processedPayloadKey}`);  

  return { Bucket: Bucket, Key: processedPayloadKey }
}
