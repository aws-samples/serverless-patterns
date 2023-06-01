const AWS = require('aws-sdk');
const transcribe = new AWS.TranscribeService();

const apig = new AWS.ApiGatewayManagementApi({
    endpoint: process.env.APIG_ENDPOINT,
});

module.exports.handler = async (event, context) => {
    console.log(event)
    const jobName = event.jobName,
        outputBucket = event.outputBucket,
        connectionId = event.connectionId,
        inputLanguageCode = event.inputLanguageCode,
        outputLanguageCode = event.outputLanguageCode;

    const params = {
        TranscriptionJobName: jobName
    };

    let jobData = await transcribe.getTranscriptionJob(params).promise();
    let jobStatus = jobData.TranscriptionJob.TranscriptionJobStatus;

    await apig.postToConnection({
        ConnectionId: connectionId,
        Data: "Transcribed Job Running"
    }).promise();

    if ( jobStatus == 'COMPLETED' || jobStatus == 'FAILED') {
        let s3Loc = jobData.TranscriptionJob.Transcript.TranscriptFileUri;
        console.log(s3Loc)
        return { 
            continue: false,
            s3Loc, jobName, outputBucket, connectionId, inputLanguageCode, outputLanguageCode
        }
    }
    else {
        return { continue: true, jobName, outputBucket, connectionId, inputLanguageCode, outputLanguageCode }
    }
}