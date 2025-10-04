const path = require('path');
const { TranscribeClient, StartTranscriptionJobCommand } = require('@aws-sdk/client-transcribe');
const transcribe = new TranscribeClient({});

module.exports.handler = async (event, context) => {
  console.log(event)
  const inputBucket = event.bucketName,
    key = event.objectKey,
    id = context.awsRequestId,
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
  await transcribe.send(new StartTranscriptionJobCommand(params));
  return { jobName, outputBucket:OUTPUT_BUCKET, inputLanguageCode, outputLanguageCode };
};
