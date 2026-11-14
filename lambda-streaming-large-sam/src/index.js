const util = require('util');
const stream = require('stream');
const { Readable } = stream;
const pipeline = util.promisify(stream.pipeline);

const { S3Client, GetObjectCommand } = require('@aws-sdk/client-s3');
const s3 = new S3Client({ region: process.env.AWS_REGION });

exports.handler = awslambda.streamifyResponse(async (event, responseStream, context) => {
    const params = {
        Bucket: "da-public-assets",
        Key: "serverlessland/pdf/SVS401-ri22.pdf"
    };
    console.log ("Streaming PDF file from S3 GetObject");
    const requestStream = (await s3.send(new GetObjectCommand(params))).Body;
    const metadata = {
        statusCode: 200,
        headers: {
            "Content-Type": "application/pdf",
            "X-Custom-Header": "Example-Custom-Header"
        }
    };
    console.log ("Streaming PDF file to client via function URL");
    responseStream = awslambda.HttpResponseStream.from(responseStream, metadata);
  
    await pipeline(requestStream, responseStream);
  });