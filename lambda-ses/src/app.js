// Load the AWS SDK for Node.js
const AWS = require('aws-sdk')
// Set the region 
AWS.config.region = process.env.AWS_REGION 
const ses = new AWS.SES({apiVersion: '2010-12-01'})
//Get Email Addresses
const senderEmailAddress = process.env.SES_SENDER_IDENTITY;

//Refernce: https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/ses-examples-sending-email.html

exports.handler = async function (event) {

var params = {
  Destination: { 
    ToAddresses: [
        event.ReceiverAddress /* RECEIVER email address */
    ]
  },
  Message: { 
    Body: { 
      Html: {
       Charset: "UTF-8",
       Data: event.HTMLBody /* customize html version of email body */
      },
      Text: {
       Charset: "UTF-8",
       Data: event.TXTBody /* customize text version of email body */
      }
     },
     Subject: {
      Charset: 'UTF-8',
      Data: event.Subject /* customize subject text */
     }
    },
  Source: senderEmailAddress, /* required: verified Amazon SES identity FROM email address */
  ReplyToAddresses: [
    senderEmailAddress /* verified Amazon SES identity FROM email address */
  ]
}
    // Send to SES
    const result = await ses.sendEmail(params).promise();
    console.log(result)
}