/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

// 1. Receive event from API Gateway REST API.
// 2. Log event to CloudWatch Logs.
// 3. Return a response with basic event information to the caller.

exports.handler = async (event) => {
  try {
    // Log event object to CloudWatch Logs
    console.log("Event: ", JSON.stringify(event, null, 2));

    // Parse event body
    var jbody = JSON.parse(event.body);

    // Create event object to return to caller
    const respObj = {
      queryString: event.queryStringParameters.myQueryString,
      header: event.headers.myheader,
      message: 'Hello '+jbody.firstName+' '+jbody.lastName+', from AWS Lambda!'
    };

    //Send response to caller
    const response = {
      statusCode: 200,
      body: JSON.stringify(respObj, null, 2),
    };
    return response;
  } catch (error) {
    console.error(error);
    throw new Error(error);
  }
};
