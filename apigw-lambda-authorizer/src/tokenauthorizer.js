/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

// A simple token-based authorizer example to demonstrate how to use an authorization token to allow or deny a request. 

'use strict';
const { promisify } = require('util')
const sleep = promisify(setTimeout)
const milliseconds = 1

exports.handler = function(event, context, callback) {
    
    console.log('Received event:', JSON.stringify(event, null, 2));

    sleep(milliseconds).then(() => {
        console.log('Slept for ' + milliseconds + ' milliseconds');
        
        var user = 'user'
        var token_name = 'authorizationToken'
        var token = event[token_name];
        
        console.log('Token: ' + token);
        
        switch (token) {
            case 'Bearer allow':
                console.log('Returning Allow');
                callback(null, generatePolicy(user, 'Allow', event.methodArn));
                break;
            case 'Bearer deny':
                console.log('Returning Deny');
                callback(null, generatePolicy(user, 'Deny', event.methodArn));
                break;
            case 'unauthorized':
                console.log('Returning Unauthorized');
                callback("Unauthorized");   // Return a 401 Unauthorized response
                break;
            default:
                console.log('Returning Error');
                callback("Error: Invalid token"); // Return a 500 Invalid token response
        }
    })
};

// Help function to generate an IAM policy
var generatePolicy = function(principalId, effect, resource) {
    
    // Required output:
    var authResponse = {};
    authResponse.principalId = principalId;
    if (effect && resource) {
        var policyDocument = {};
        policyDocument.Version = '2012-10-17'; // default version
        policyDocument.Statement = [];
        var statementOne = {};
        statementOne.Action = 'execute-api:Invoke'; // default action
        statementOne.Effect = effect;
        statementOne.Resource = resource;
        policyDocument.Statement[0] = statementOne;
        authResponse.policyDocument = policyDocument;
    }
    
    // Optional output with custom properties of the String, Number or Boolean type.
    authResponse.context = {
        "stringKey": "stringval",
        "numberKey": 123,
        "booleanKey": true,
        "authorizerTimestamp": +new Date
    };
    
    console.log("Sent policy: " + authResponse.policyDocument);
    return authResponse;
}