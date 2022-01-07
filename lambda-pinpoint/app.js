/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

("use strict");

const { SendMessagesCommand } = require("@aws-sdk/client-pinpoint");
const { PinpointClient } = require("@aws-sdk/client-pinpoint");
const REGION = "us-east-1";
//Set the MediaConvert Service Object
const pinClient = new PinpointClient({region: REGION});

const originationNumber = process.env.ORIGINATION_NUMBER;
const projectId = process.env.PINPOINT_PROJECT_ID;
const destinationNumber = process.env.DESTINATION_NUMBER;

// The content of the SMS message.
const message =
  "This message was sent through Amazon Pinpoint " +
  "using the AWS SDK for JavaScript in Node.js. Reply STOP to " +
  "opt out.";
var messageType = "TRANSACTIONAL";

// Specify the parameters to pass to the API.
var params = {
  ApplicationId: projectId,
  MessageRequest: {
    Addresses: {
      [destinationNumber]: {
        ChannelType: "SMS",
      },
    },
    MessageConfiguration: {
      SMSMessage: {
        Body: message,
        MessageType: messageType,
        OriginationNumber: originationNumber,
      },
    },
  },
};

// The Lambda handler
exports.handler = async (event) => {
  try {
    const data = await pinClient.send(new SendMessagesCommand(params));
    console.log(
      "Message sent! " +
        data["MessageResponse"]["Result"][destinationNumber]["StatusMessage"]
    );
  } catch (err) {
    console.log(err);
  }
}