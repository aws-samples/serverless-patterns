const AWS = require('aws-sdk');
const S3 = new AWS.S3();
var sns = new AWS.SNS();
const sharp = require('sharp');

let NotificationSNSTopic = process.env.NotificationSNSTopic

exports.handler = async (event) => {

    console.log("Event = ", event);
    console.log("NotificationSNSTopic = ", NotificationSNSTopic);
    // Collect the object key from the S3 event record
    const { key } = event.Records[0].s3.object;

    console.log({ triggerObject: key });

    // Collect the full resolution image from s3 using the object key
    const uncompressedImage = await S3.getObject({
        Bucket: process.env.UNCOMPRESSED_BUCKET,
        Key: key,
    }).promise();

    console.log("uncompressedImage = ", uncompressedImage)

    // Compress the image to a 200x200 avatar square as a buffer, without stretching
    const compressedImageBuffer = await sharp(uncompressedImage.Body)
    .resize({ 
        width: 200, 
        height: 200, 
        fit: 'cover'
    })
    .toBuffer();

    console.log("compressedImageBuffer = ", compressedImageBuffer);

    // Upload the compressed image buffer to the Compressed Images bucket
    await S3.putObject({
        Bucket: process.env.COMPRESSED_BUCKET,
        Key: key,
        Body: compressedImageBuffer,
        ContentType: "image"
    }).promise();

    console.log("Object uploaded to destination bucket");

    var presignedGETURL = S3.getSignedUrl('getObject', {
        Bucket: process.env.COMPRESSED_BUCKET,
        Key: key, //filename
        Expires: 300 //time to expire in seconds
    });  
    
    console.log("presignedGETURL = ", presignedGETURL)

    var params = {
        Message: 'Access the compressed image using the link :-' + presignedGETURL, /* required */
        Subject: 'Compressed image',
        TopicArn: NotificationSNSTopic
    };

    let output = await sns.publish(params).promise();

    console.log("Output = ", output);

    console.log(`Compressing ${key} complete!`)

}