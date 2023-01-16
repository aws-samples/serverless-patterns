/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

'use strict'

exports.handler =  async function(event, context) {
  console.log("EVENT: \n" + JSON.stringify(event, null, 2))
  return      {
    "statusCode" : 200,
    "body": JSON.stringify(	{
      "petDetails": {
        "action": "RETRIEVE",
        "status": "available",
      },
      "category": {
        "id": 0,
        "name": "string"
      },
      "tags": [{
        "name": "doggie"
      },
        {
          "name": "photoUrls",
          "value": "string"
        },
        {
          "name": "location",
          "value": "string"
        }
      ]

    })
  };
};
