/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

// dependencies
const { SFNClient, StartExecutionCommand } = require('@aws-sdk/client-sfn');
const moment = require('moment');

exports.handler =  async (event) => {
    const sfnArn = process.env.StateMachineArn
    const rightNow = moment().format('YYYYMMDD-hhmmss');
    const params = {
        stateMachineArn: sfnArn,
        input: JSON.stringify(event),
        name: `ArchiveAt${rightNow}`
    };

    const stepfunctions = new SFNClient();
    let res
    try {
     res = await  stepfunctions.send(new StartExecutionCommand(params))
    }catch(err){
    console.error(err)
    }

    return {
    "Started": res
    };

}
