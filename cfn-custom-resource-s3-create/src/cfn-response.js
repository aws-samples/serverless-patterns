/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

// More information on cfn-response: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-lambda-function-code-cfnresponsemodule.html

exports.SUCCESS = "SUCCESS";
exports.FAILED = "FAILED";

exports.send = function (event, context, responseStatus, responseData, physicalResourceId, noEcho) {
  try {
    const https = require("https");
    const { URL } = require("url");

    const responseBody = {
      Status: responseStatus,
      Reason: "See the details in CloudWatch Log Stream: " + context.logStreamName,
      PhysicalResourceId: context.logStreamName,
      StackId: event.StackId,
      RequestId: event.RequestId,
      LogicalResourceId: event.LogicalResourceId,
      NoEcho: false,
      Data: responseData,
    };
    console.log("Response body:\n", JSON.stringify(responseBody));

    const parsedUrl = new URL(event.ResponseURL);
    const requestOptions = {
      hostname: parsedUrl.hostname,
      port: 443,
      path: parsedUrl.pathname + parsedUrl.search,
      method: "PUT",
      headers: {
        "content-type": "",
        "content-length": JSON.stringify(responseBody).length,
      },
    };
    console.log("Request options:\n", JSON.stringify(requestOptions));

    // Send response back to CloudFormation
    return new Promise((resolve, reject) => {
      const request = https.request(requestOptions, function (response) {
        response.on("data", () => {});
        response.on("end", () => {
          console.log("Status code: ", response.statusCode);
          console.log("Status message: ", response.statusMessage);
          resolve("Success");
        });
      });
      request.on("error", (e) => {
        console.error(e);
        reject("Error");
      });
      request.write(JSON.stringify(responseBody));
      request.end();
    });
  } catch (error) {
    console.error("Error in cfn_response:\n", error);
    return;
  }
};
