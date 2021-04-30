'use strict'

const AWS = require('aws-sdk')
const s3 = new AWS.S3();

exports.handler = async(event) => {
    const key = getKey()
    
    const uploadParams = {
        Bucket: process.env["UPLOADS_BUCKET"],
        Key: key,
        Body: JSON.stringify(event) 
    };    
    
    //Store payload in S3
    const stored = await s3.upload(uploadParams).promise()
    console.log("\rUploaded payload to ", stored.Location);
    
    console.log("\rStarting step functions", process.env["PROCESS_FILE_STATE_MACHINE_ARN"]);
    
    //startsync execution here and return the result
    const stepfunctions = new AWS.StepFunctions();
    const params = {
      stateMachineArn: process.env["PROCESS_FILE_STATE_MACHINE_ARN"],
      input: JSON.stringify({ Bucket: uploadParams.Bucket, Key: uploadParams.Key }),
    };
    const result = await stepfunctions.startSyncExecution(params).promise()

    return result
};

const getKey = () => {
    const d = new Date()
    const ticks = `${d.getFullYear()}-${d.getMonth()+1}-${d.getDate()}-${d.getHours()}-${d.getSeconds()}-${d.getMilliseconds()}`
    const randomID = parseInt(Math.random() * 10000000, 10)
    const key = `${randomID}`    
    
    return `${ticks}/initialPayload/${key}`
    
}