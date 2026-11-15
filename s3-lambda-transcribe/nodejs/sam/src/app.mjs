import { S3Client, GetObjectCommand } from '@aws-sdk/client-s3';
import { TranscribeClient, StartTranscriptionJobCommand } from '@aws-sdk/client-transcribe';

const s3Client = new S3Client({ region: process.env.REGION });
const transcribeClient = new TranscribeClient({ region: process.env.REGION });

export const handler = async (event) => {
  try {
    // Get the S3 bucket and key from the event
    const bucket = event.Records[0].s3.bucket.name;
    const key = decodeURIComponent(event.Records[0].s3.object.key.replace(/\+/g, ' '));
    
    console.log(`Processing file: s3://${bucket}/${key}`);

    // Extract file name and extension for the transcription job
    const fileName = key.split('/').pop();
    const fileNameWithoutExt = fileName.substring(0, fileName.lastIndexOf('.')) || fileName;
    const fileExt = fileName.substring(fileName.lastIndexOf('.') + 1).toLowerCase();
    
    // Determine media format based on file extension
    let mediaFormat;
    switch (fileExt) {
      case 'mp3':
        mediaFormat = 'mp3';
        break;
      case 'wav':
        mediaFormat = 'wav';
        break;
      case 'flac':
        mediaFormat = 'flac';
        break;
      default:
        throw new Error(`Unsupported file format: ${fileExt}`);
    }
    
    const transcriptionJobName = `${fileNameWithoutExt}-${Date.now()}`;
    
    const mediaFileUri = `s3://${bucket}/${key}`;

    const startTranscriptionParams = {
      TranscriptionJobName: transcriptionJobName,
      LanguageCode: 'en-US', 
      MediaFormat: mediaFormat,
      Media: {
        MediaFileUri: mediaFileUri
      },
      OutputBucketName: bucket,
      OutputKey: `transcriptions/${fileNameWithoutExt}.json`
    };

    const transcriptionCommand = new StartTranscriptionJobCommand(startTranscriptionParams);
    const transcriptionResponse = await transcribeClient.send(transcriptionCommand);
    
    console.log(`Started transcription job: ${transcriptionJobName}`);
    console.log(`Transcription job response: ${JSON.stringify(transcriptionResponse)}`);
    
    return {
      statusCode: 200,
      body: JSON.stringify({
        message: 'Transcription job started successfully',
        jobName: transcriptionJobName,
        jobStatus: transcriptionResponse.TranscriptionJob.TranscriptionJobStatus
      })
    };
  } catch (error) {
    console.error('Error processing the file:', error);
    
    return {
      statusCode: 500,
      body: JSON.stringify({
        message: 'Error starting transcription job',
        error: error.message
      })
    };
  }
};
