/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

const { StepFunctions } = require('@aws-sdk/client-sfn');

exports.handler = async (event) => {
  try {
    // Define the Step Functions client
    const stepFunctions = new StepFunctions({});

    // Define the parameters for the redriveExecution operation
    const params = {
      stateMachineArn: event.detail.executionArn
    };

    // Start the Step Functions workflow
    const result = await stepFunctions.redriveExecution(params);

    console.log('Workflow redriven:', result.executionArn);

    return {
      statusCode: 200,
      body: JSON.stringify('Workflow started successfully'),
    };
  } catch (error) {
    console.error('Error starting workflow:', error);
    return {
      statusCode: 500,
      body: JSON.stringify('Error starting workflow'),
    };
  }
};
