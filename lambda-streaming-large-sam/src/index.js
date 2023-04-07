const util = require('util');
const stream = require('stream');
const { Readable } = stream;
const pipeline = util.promisify(stream.pipeline);

const AWS = require('aws-sdk');
AWS.config.update({ region: process.env.AWS_REGION });
const s3 = new AWS.S3();

exports.handler = awslambda.streamifyResponse(async (event, responseStream, context) => {
    const params = {
        Bucket: "da-public-assets",
        Key: "serverlessland/pdf/SVS401-ri22.pdf"
    };
    console.log ("Streaming PDF file using S3 createReadStream");
    const requestStream = s3.getObject(params).createReadStream();
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