import { RekognitionClient, IndexFacesCommand } from "@aws-sdk/client-rekognition";
import * as path from 'path';

const rekognition = new RekognitionClient();

export const handler = async (event: any = {}): Promise<any> => {
    const facesCollectionId = process.env.FACES_COLLECTION_ID || '';

    for (const image of event['Records']) {
        let imageData = image['s3'];
        let fileData = path.parse(imageData['object']['key']);

        try {
            await rekognition.send(new IndexFacesCommand({
                CollectionId: facesCollectionId,
                Image: {
                    S3Object: {
                        Bucket: imageData['bucket']['name'],
                        Name: imageData['object']['key'],
                    }
                },
                ExternalImageId: fileData['name'],
            }));
        } catch (error) {
            console.log(error);
        }
    }
}
