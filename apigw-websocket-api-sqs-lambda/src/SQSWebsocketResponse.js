// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

const AWS = require("aws-sdk");
const apig = new AWS.ApiGatewayManagementApi({ endpoint: process.env.ApiGatewayEndpoint });

exports.handler = async (event, context) => {
    //console.log("Event: ", JSON.stringify(event, null, 2));
    if (event.Records) {
        for (let r = 0; r < event.Records.length; r++) {
            try {
                let response = {
                    connectionId: event.Records[r].messageAttributes.connectionId.stringValue,
                    requestId: event.Records[r].messageAttributes.requestId.stringValue,
                    message: event.Records[r].body
                };
                await apig.postToConnection({ ConnectionId: event.Records[r].messageAttributes.connectionId.stringValue, Data: JSON.stringify(response) }).promise();
            }
            catch (err) {
                console.error(err);
            }
        }
    }
    return {
        statusCode: 200
    };
};