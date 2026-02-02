import { S3Client, GetObjectCommand } from "@aws-sdk/client-s3";
import {
      BedrockRuntimeClient,
      InvokeModelCommand,
} from "@aws-sdk/client-bedrock-runtime";

const awsS3Client = new S3Client();
const awsBedrockClient = new BedrockRuntimeClient();

const fetchFileFromS3 = async (bucketName, fileKey) => {
      const command = new GetObjectCommand({
            Bucket: bucketName,
            Key: fileKey,
      });
      const response = await awsS3Client.send(command);
      const fileContent = response.Body
            ? await response.Body.transformToString()
            : "";
      return fileContent;
};

export const handler = async (event) => {
      if (!event || !event.Records) {
            return {
                  statusCode: 200,
                  body: JSON.stringify({ message: "No S3 event detected" }),
            };
      }

      const eventRecord = event.Records[0];
      const bucketName = eventRecord.s3.bucket.name;
      const fileName = decodeURIComponent(eventRecord.s3.object.key);
      const fileContent = await fetchFileFromS3(bucketName, fileName);

      const bedrockModelInput = {
            modelId: "amazon.titan-embed-text-v1",
            contentType: "application/json",
            accept: "*/*",
            body: JSON.stringify({ inputText: JSON.stringify(fileContent) }),
      };
      console.log("Input provided to Bedrock", bedrockModelInput);

      const bedrockCommand = new InvokeModelCommand(bedrockModelInput);
      const bedrockResponse = await awsBedrockClient.send(bedrockCommand);

      const responseData = Buffer.from(bedrockResponse.body).toString();
      console.log("Response data: ", responseData);

      return {
            statusCode: 200,
            body: JSON.stringify(responseData),
      };
};
