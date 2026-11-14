/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

'use strict'

// The Lambda handler
exports.handler = async (event) => {
  console.log(JSON.stringify(event, 2, null))
}