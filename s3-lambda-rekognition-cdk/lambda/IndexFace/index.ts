import { Rekognition } from "aws-sdk";
import * as path from 'path';

export const handler = async (event: any = {}): Promise<any> => {
    const facesCollectionId = process.env.FACES_COLLECTION_ID || '';
    const rekognition = new Rekognition();

    for (const image of event['Records']) {
        let imageData = image['s3'];
        let fileData = path.parse(imageData['object']['key']);
        var params = {
            CollectionId: facesCollectionId,
            Image: {
                S3Object: {
                    Bucket: imageData['bucket']['name'],
                    Name: imageData['object']['key'],
                }
            },
            ExternalImageId: fileData['name'],
        };

        try {
            await rekognition.indexFaces(params).promise();
        } catch (error) {
            console.log(error);
        }
    }
}
