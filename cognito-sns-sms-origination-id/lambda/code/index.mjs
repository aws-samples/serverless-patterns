// ES Modules import
import { SNSClient, PublishCommand } from "@aws-sdk/client-sns";
import b64 from 'base64-js';
import libphonenumber from 'google-libphonenumber';
import encryptionSdk from '@aws-crypto/client-node';
//Configure orignation number or sender id as per destination country iso code
import { createRequire } from "module";
const require = createRequire(import.meta.url);
const orignationIdConfig = require("./orignationIdConfig.json");
//Set up an encryption client with an explicit commitment policy: REQUIRE_ENCRYPT_ALLOW_DECRYPT 
const { encrypt, decrypt } = encryptionSdk.buildClient(encryptionSdk.CommitmentPolicy.REQUIRE_ENCRYPT_ALLOW_DECRYPT);
const generatorKeyId = process.env.KEY_ALIAS;
const keyIds = [process.env.KEY_ARN];
const keyring = new encryptionSdk.KmsKeyringNode({ generatorKeyId, keyIds })
// SNS Client
const client = new SNSClient();
async function snsPublish(message, phoneNumber) {
    //SNS SMS Parameters
    const [messageAttributes] =
        await Promise.all([
            getSMSMessageAttributes(phoneNumber)
        ]);
    const input = { // PublishInput
        Message: message,
        PhoneNumber: phoneNumber.toString(),
        MessageAttributes: messageAttributes
    };
    const command = new PublishCommand(input);
    const response = await client.send(command);
    return response
}
// Function to get ISO Country Code from Phone Number
// Phone Number should be E.164 format
function getISOCode(phoneNumber) {
    // Get an instance of `PhoneNumberUtil`.
    const phoneUtil = libphonenumber.PhoneNumberUtil.getInstance();
    // Parse number with country code and keep raw input.
    const number = phoneUtil.parseAndKeepRawInput(phoneNumber);
    //Get ISO Code from getRegionCodeForNumber 
    const countryCode = phoneUtil.getRegionCodeForNumber(number);
    console.log("SMS Message Sent to Country Code:" + countryCode);
    return countryCode;
}
// Function to set SNS SMS Message Attributes as per origination configuration and destination country code
function getSMSMessageAttributes(phoneNumber) {
    //SNS SMS MessageAttributes
    let senderId;
    let originationNumber;
    //Default SMS Message Attributes if no orgination Id configured
    let smsMessageAttributes = {
        'AWS.SNS.SMS.SMSType': {
            DataType: 'String', /* required */
            StringValue: 'Transactional'
        }
    };
    // Get ISO country code of the phoneNumber
    let isoCountryCode = getISOCode(phoneNumber);
    // Check if origination configuration has orgination identites configured for destination  country code
    if (isoCountryCode in orignationIdConfig) {
        let originationId  = Object.keys(orignationIdConfig[isoCountryCode]);
        let originationType = originationId[0];
        // Check if ISO country code has orignation number or sender id
        switch (originationType) {
            case "SenderID":
                // Set Sender Id
                senderId = orignationIdConfig[isoCountryCode]['SenderID'];
                console.log("Sender Id used:" + senderId);
                // Create publish parameters with Sender Id 
                smsMessageAttributes = {
                    'AWS.SNS.SMS.SMSType': {
                        DataType: 'String', /* required */
                        StringValue: 'Transactional'
                    },
                    'AWS.SNS.SMS.SenderID': {
                        DataType: 'String', /* required */
                        StringValue: senderId
                    }
                };
                return smsMessageAttributes;
            case "OriginationNumber":
                //Set originationNumber
                originationNumber = orignationIdConfig[isoCountryCode]['OriginationNumber'];
                console.log("Origination number used:" + originationNumber);
                // Create publish parameters with Sender Id 
                smsMessageAttributes = {
                    'AWS.SNS.SMS.SMSType': {
                        DataType: 'String', /* required */
                        StringValue: 'Transactional'
                    },
                    'AWS.MM.SMS.OriginationNumber': {
                        DataType: 'String', /* required */
                        StringValue: originationNumber
                    }
                };
                return smsMessageAttributes;
            default:
                //Default SMS message attributes if no orgination Id configured
                console.log("No Origination number used:" + originationNumber);
                return smsMessageAttributes;
        }
    }else {
        //Default SMS message attributes if no orgination Id configured
        console.log("No origination identity configured for country code:"+ isoCountryCode);
        return smsMessageAttributes;
    }
}
//main lambda handler
export const handler = async (event) => {
    // Log triggerSource
    console.log("TriggerSource:" + event.triggerSource)
    //SMS Attributes
    let plainTextCode;
    let smsMessage;
    let destinationPhoneNumber;
    //Decrypt the secret code using encryption SDK.
    if (event.request.code) {
        const { plaintext, messageHeader } = await decrypt(keyring, b64.toByteArray(event.request.code));
        //PlainTextCode now contains the decrypted secret.
        plainTextCode = plaintext;
        //Get destination phonenumber 
        destinationPhoneNumber = event.request.userAttributes.phone_number;
    }
    //Include the temporary MFA code in the sms message.
    smsMessage = "Your OTP Code from Custom SMS Sender: " + plainTextCode;
    //Send SMS Messaging 
    const [result] =
        await Promise.all([
            snsPublish(smsMessage, destinationPhoneNumber)
        ]);
    // Print SNS SMS Message Id
    console.log("SNS Publish MessageId:"+result.MessageId);
    return result;
};
