/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */
'use strict'
const AWS = require('aws-sdk')
AWS.config.region = process.env.AWS_REGION 
const sns = new AWS.SNS({apiVersion: '2012-11-05'})

// The Lambda handler
exports.handler = async (event) => {

  console.log("request:", JSON.stringify(event, undefined, 2));
  if (event.MetricType == 'Temperature' || event.MetricType == 'Humidity') {
    // Params object for SNS
    const params = {
      MessageAttributes: {
        'MetricType': {
          DataType: 'String',
          StringValue: event.MetricType
        }
      },
      Message: event.MetricType + " = " + event.MetricValue + " at " + event.Location,
      Subject: 'Event notification - ' +  event.MetricType,
      TopicArn: process.env.SNStopic
    }
    
    // Send to SNS
    const result = await sns.publish(params).promise()
    console.log(result)
  }

}