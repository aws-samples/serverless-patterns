const { S3Client, PutObjectTaggingCommand } = require('@aws-sdk/client-s3')
const s3 = new S3Client({ region: process.env.AWS_REGION })

exports.handler = async (event) => {
    console.log(JSON.stringify(event, null, 2));

    const params = {
        Bucket: event.detail.bucket.name,
        Key: decodeURIComponent(event.detail.object.key.replace(/\+/g, " ")),
        Tagging: {
            TagSet: [
                {
                    Key: "TagAddedBy",
                    Value: "S3EventProcessor"
                }
            ]
        }
    };

    // Tag the S3 object using putObjectTagging
    const response = await s3.send(new PutObjectTaggingCommand(params));

    // Logs the response
    console.log(`Response from putObjectTagging SDK call ${JSON.stringify(response)}`);
}