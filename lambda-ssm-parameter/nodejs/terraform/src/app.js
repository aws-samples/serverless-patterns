/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

// 1. Receive event with method and body.
// 2. GET or PUT an SSM Parameter Store parameter.
// 3. Return a response with parameter result.

const { SSMClient, GetParameterCommand, PutParameterCommand } = require('@aws-sdk/client-ssm')

const ssmClient = new SSMClient({
  region: process.env.AWS_REGION
})

exports.handler = async (event, context) => {
  try {
    // Log event and context object to CloudWatch Logs
    console.log("Event:\n", JSON.stringify(event, null, 2))
    console.log("Context:\n", JSON.stringify(context, null, 2))

    // Log parameter name from environment variables
    const parameterName = process.env.SSMParameterName;
    console.log("SSMParameterName: ", parameterName);

    // Get method and body from event
    const method = event.method
    const body = event.body
    console.log("Method: ", method)
    console.log("Body: ", body)

    // Modify or Get parameter
    let result = ""
    if (method == "PUT") {
      const ssmPutParams = {
        Name: parameterName,
        Value: body,
        Overwrite: true,
        Type: "String",
      };
      result = await ssmClient.send(new PutParameterCommand(ssmPutParams))
    } else if (method == "GET") {
      const ssmGetParams = {
        Name: parameterName,
      };
      result = await ssmClient.send(new GetParameterCommand(ssmGetParams))
    } else {
      result = "Method not supported"
    }

    console.log("Result:\n", JSON.stringify(result));

    const response = {
      statusCode: 200,
      body: JSON.stringify(result)
    }

    return response

  } catch (error) {
    console.error(error);
    throw new Error(error);
  }
}
