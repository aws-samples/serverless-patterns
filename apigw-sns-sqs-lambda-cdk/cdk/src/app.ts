/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
  *  SPDX-License-Identifier: MIT-0
 */

'use strict'

import { Handler } from "aws-lambda";

export const handler: Handler = async (event) => {
    console.log(event);
};