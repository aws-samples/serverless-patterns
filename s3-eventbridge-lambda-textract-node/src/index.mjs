import { S3Client, PutObjectCommand } from "@aws-sdk/client-s3";
import { TextractClient, DetectDocumentTextCommand } from "@aws-sdk/client-textract";

const s3Client = new S3Client();
const textractClient = new TextractClient();

export const handler = async (event, context) => {
    // Extract bucket and key from the EventBridge event
    console.log(event)
    event.Records[0].s3.bucket.name;
    
    const bucket = event.Records[0].s3.bucket.name;
    const key = event.Records[0].s3.object.key;
    console.log(bucket);
    console.log(key);
    try {
        // Call Textract to detect document text
        const detectParams = {
            Document: {
                S3Object: {
                    Bucket: bucket,
                    Name: key
                }
            }
        };
        const detectCommand = new DetectDocumentTextCommand(detectParams);
        const response = await textractClient.send(detectCommand);
        console.log(response);
        // Prepare the output key
        let outputKey = `textract-output-${key}`;
        outputKey = outputKey.substring(0, outputKey.lastIndexOf('.')) + '.json';
        console.log(outputKey);
        
        // Write the Textract output to the output bucket
        const putParams = {
            Bucket: process.env.OUTPUT_BUCKET,
            Key: outputKey,
            Body: JSON.stringify(response)
        };
        const putCommand = new PutObjectCommand(putParams);
        await s3Client.send(putCommand);
        
        return {
            statusCode: 200,
            body: JSON.stringify('Document processed successfully')
        };
    } catch (error) {
        console.error('Error:', error);
        return {
            statusCode: 500,
            body: JSON.stringify('Error processing document')
        };
    }
};
