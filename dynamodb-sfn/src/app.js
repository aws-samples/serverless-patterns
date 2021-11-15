const AWS = require('aws-sdk');

exports.handler =  async (event) => {
    const 
    const stepFunctionARN = process.env.StateMachineArn
    const params = {
        stateMachineArn: sfnArn,
        input: JSON.stringify(event),
    };

    const stepfunctions = new AWS.StepFunctions();
    let res
    try {
     res = await stepfunctions.startExecution(params).promise()
    }catch(err){
    console.error(err)
    }

    return {
    "Started": res
    };

}
