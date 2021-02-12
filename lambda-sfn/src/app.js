/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

// dependencies
const AWS = require('aws-sdk');
const moment = require('moment');

exports.handler =  async (event) => {
    const sfnArn = process.env.StateMachineArn
    const rightNow = moment().format('YYYYMMDD-hhmmss');
    const params = {
        stateMachineArn: sfnArn,
        input: JSON.stringify(event),
        name: `ArchiveAt${rightNow}`
    };

    const stepfunctions = new AWS.StepFunctions();
    let res
    try {
     res = await  stepfunctions.startExecution(params).promise()
    }catch(err){
    console.error(err)
    }

    return {
    "Started": res
    };

}
