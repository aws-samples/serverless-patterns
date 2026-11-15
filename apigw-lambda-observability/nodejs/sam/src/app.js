/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

const { metricScope } = require("aws-embedded-metrics");

exports.handler = metricScope(metrics => async (event, context) => {
  let body = event;
  let statusCode = 200;
  const headers = {
    "Content-Type": "application/json"
  };

  // Initialize putting common business metrics using EMF
  var metricPayload = {}
  metrics.putDimensions({ Service: "Sample Service" });
  metrics.putMetric("ProcessedRequests", 1, "Count");
  metrics.setProperty("requestId", event.requestContext.requestId);
  metrics.setProperty("routeKey", event.routeKey);

  // Your business logics goes here

  // Define your custom metrics payload - record ID in the database, operation performed, etc.
  // In this example we will use HTTP method 
  metricPayload.operation = event.requestContext.http.method;

  metrics.setProperty("Payload", metricPayload);

  return body;
});

