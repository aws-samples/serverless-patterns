/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

// Lambda Destination OnSuccess Lambda Function

exports.handler = async (event) => {
  // do some further processing on event
  console.log('Further processing for successful function invocation ')
  console.log(JSON.stringify(event, null, 2))
  
}