const { PutObjectCommand, S3Client } = require("@aws-sdk/client-s3");
const s3 = new S3Client({});

const handler = async () => {
  const timestamp = Date.now()
  const message = JSON.stringify({
    message: 'Task executed from Fargate Cluster!',
    timestamp
  })
  const putCommand = new PutObjectCommand({
    Bucket: process.env.DESTINATION_BUCKET,
    Key: timestamp + '.json',
    ContentType: 'application/json',
    Body: message,
  });
  const result = await s3.send(putCommand);
  console.log('result: ', result)
};

handler()