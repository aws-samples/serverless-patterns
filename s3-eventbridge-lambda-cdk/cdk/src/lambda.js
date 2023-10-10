const AWS = require('aws-sdk')
AWS.config.update({ region: process.env.AWS_REGION })
const s3 = new AWS.S3()

exports.handler = async (event) => {
    console.log(JSON.stringify(event, null, 2));

    var params = {
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
    const response = await s3.putObjectTagging(params).promise();

    // Logs the response
    console.log(`Response from putObjectTagging SDK call ${JSON.stringify(response)}`);
}