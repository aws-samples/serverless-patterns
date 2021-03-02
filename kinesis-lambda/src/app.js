/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

'use strict'

exports.handler = async (event) => {
  event.Records.forEach(item => {
        let payload = new Buffer(item.kinesis.data, 'base64').toString("ascii")
        console.log(payload)
    })
}