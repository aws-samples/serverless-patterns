/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

// 1. Receive event from API Gateway HTTP API.
// 2. Log event and context object, and example environment variables to CloudWatch Logs.
// 3. Return a response with basic event information to the caller.

exports.handler = async (event, context) => {
  try {
    // Log event and context object to CloudWatch Logs
    console.log("Event: ", JSON.stringify(event, null, 2));
    console.log("Context: ", JSON.stringify(context, null, 2));

    // Create event object to return to caller
    const eventObj = {
      functionName: context.functionName,
      xForwardedFor: event.headers["x-forwarded-for"],
      contentType: event.headers["content-type"],
      method: event.requestContext.http.method,
      rawPath: event.rawPath,
      queryString: event.queryStringParameters,
      body: event.body,
    };

    const response = {
      statusCode: 200,
      body: JSON.stringify(eventObj, null, 2),
    };
    return response;
  } catch (error) {
    console.error(error);
    throw new Error(error);
  }
};
