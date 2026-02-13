const { TranscribeClient, GetTranscriptionJobCommand } = require('@aws-sdk/client-transcribe');
const transcribe = new TranscribeClient({});

module.exports.handler = async (event, context) => {
    console.log(event)
    const jobName = event.jobName,
        outputBucket = event.outputBucket,
        inputLanguageCode = event.inputLanguageCode,
        outputLanguageCode = event.outputLanguageCode;

    const params = {
        TranscriptionJobName: jobName
    };

    let jobData = await transcribe.send(new GetTranscriptionJobCommand(params));
    let jobStatus = jobData.TranscriptionJob.TranscriptionJobStatus;
    if ( jobStatus == 'COMPLETED' || jobStatus == 'FAILED') {
        let s3Loc = jobData.TranscriptionJob.Transcript.TranscriptFileUri;
        console.log(s3Loc)
        return { 
            continue: false,
            s3Loc, jobName, outputBucket, inputLanguageCode, outputLanguageCode
        }
    }
    else {
        return { continue: true, jobName, outputBucket, inputLanguageCode, outputLanguageCode }
    }
}
