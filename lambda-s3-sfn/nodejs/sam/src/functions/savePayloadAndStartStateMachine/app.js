'use strict'

const { S3Client, PutObjectCommand } = require('@aws-sdk/client-s3')
const s3 = new S3Client();
const { SFNClient, StartSyncExecutionCommand } = require('@aws-sdk/client-sfn')

exports.handler = async(event) => {
    const key = getKey()
    
    const uploadParams = {
        Bucket: process.env["UPLOADS_BUCKET"],
        Key: key,
        Body: JSON.stringify(event) 
    };    
    
    //Store payload in S3
    await s3.send(new PutObjectCommand(uploadParams))
    console.log("\rUploaded payload to ", `s3://${uploadParams.Bucket}/${key}`);
    
    console.log("\rStarting step functions", process.env["PROCESS_FILE_STATE_MACHINE_ARN"]);
    
    //startsync execution here and return the result
    const stepfunctions = new SFNClient();
    const params = {
      stateMachineArn: process.env["PROCESS_FILE_STATE_MACHINE_ARN"],
      input: JSON.stringify({ Bucket: uploadParams.Bucket, Key: uploadParams.Key }),
    };
    const result = await stepfunctions.send(new StartSyncExecutionCommand(params))

    return result
};

const getKey = () => {
    const d = new Date()
    const ticks = `${d.getFullYear()}-${d.getMonth()+1}-${d.getDate()}-${d.getHours()}-${d.getSeconds()}-${d.getMilliseconds()}`
    const randomID = parseInt(Math.random() * 10000000, 10)
    const key = `${randomID}`    
    
    return `${ticks}/initialPayload/${key}`
    
}