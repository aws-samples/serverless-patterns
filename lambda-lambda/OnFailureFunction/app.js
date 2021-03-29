/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

// Lambda Destination handler function

exports.handler = async (event) => {
  // do some further processing on event
  console.log('Further Processing for failed function')
  console.log(JSON.stringify(event, null, 2))
  
}