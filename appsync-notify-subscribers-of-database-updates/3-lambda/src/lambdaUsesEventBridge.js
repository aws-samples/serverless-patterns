"use strict";
const AWS = require("aws-sdk");

const eventbridge = new AWS.EventBridge();

exports.handler = async (event) => {
    try {
        console.log("event -", event);
        const params = {
            Entries: [{
                Detail: JSON.stringify({
                    "order-id": "123",
                    "previous-status": "SHIPPED",
                    "status": "DELIVERED"
                }), // Detail has to be a string
                DetailType: "Order Status Update",
                Source: "orders.system",
                EventBusName: process.env.EVENT_BUS_ARN
            }]
        };
        console.log("push data to EventBridge ", params);
        const response = await eventbridge.putEvents(params).promise();
        console.log("response ", response);

    } catch (error) {
        console.log("error ->", error);
    }
};
