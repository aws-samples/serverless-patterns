import { TranscribeClient, StartTranscriptionJobCommand } from "@aws-sdk/client-transcribe";
import { randomUUID } from 'crypto';

export const lambda_handler = async (event, context) => {
    try {
        const requestBody = JSON.parse(event.body);
        const s3_url = requestBody.audio_url;
        
        const transcribe = new TranscribeClient();
        const job_name = `transcribe-${randomUUID()}`;
        
        const command = new StartTranscriptionJobCommand({
            TranscriptionJobName: job_name,
            Media: { MediaFileUri: s3_url },
            MediaFormat: 'mp3',  // Adjust based on your needs
            LanguageCode: 'en-US'  // Adjust based on your needs
        });
        
        await transcribe.send(command);
        
        return {
            statusCode: 200,
            body: JSON.stringify({
                job_name: job_name,
                status: 'IN_PROGRESS'
            })
        };
        
    } catch (e) {
        return {
            statusCode: 500,
            body: JSON.stringify({
                error: e.toString()
            })
        };
    }
};