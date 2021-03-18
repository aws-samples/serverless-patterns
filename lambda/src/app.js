/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

// Simple Lambda handler function

exports.handler = async (event) => {

  // do some further processing on event
  let message ="Hello "+event.name +", from Lambda"
  console.log(message)
  
  return message
}