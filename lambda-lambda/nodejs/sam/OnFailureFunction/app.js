/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

// Lambda Destination OnFailure Lambda Function

exports.handler = async (event) => {
  // do some further processing on event
  console.log('Further Processing for failed function invocation')
  console.log(JSON.stringify(event, null, 2))
  
}