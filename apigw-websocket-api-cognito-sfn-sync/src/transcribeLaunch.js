const AWS = require('aws-sdk');
const transcribe = new AWS.TranscribeService();

const apig = new AWS.ApiGatewayManagementApi({
  endpoint: process.env.APIG_ENDPOINT,
});

module.exports.handler = async (event, context) => {
  console.log(event)
  const inputBucket = event.bucketName,
    key = event.objectKey,
    id = context.awsRequestId,
    connectionId = event.connectionId,
    inputLanguageCode = event.inputLanguageCode,
    outputLanguageCode = event.outputLanguageCode;

    const fileUri = `https://${inputBucket}.s3.amazonaws.com/${key}`,
      jobName = `s3-lambda-audio-transcribe-${id}`;
    
    let OUTPUT_BUCKET = inputBucket // Need separate destination
    let code = (inputLanguageCode == "" ? 'en-US':inputLanguageCode);
    const params = {
    LanguageCode: code,
    Media: {
      MediaFileUri: fileUri
    },
    MediaFormat: "ogg",
    TranscriptionJobName: jobName,
    OutputBucketName: OUTPUT_BUCKET
  };
  console.log(params);
  await apig
  .postToConnection({
      ConnectionId: connectionId,
      Data: "Transcribed Job Launched"
  }).promise();
  await transcribe.startTranscriptionJob(params).promise();
  return { jobName, outputBucket:OUTPUT_BUCKET, connectionId, inputLanguageCode, outputLanguageCode };
};
