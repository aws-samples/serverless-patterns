/*! Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *  SPDX-License-Identifier: MIT-0
 */

import { SecretsManagerClient, GetSecretValueCommand } from "@aws-sdk/client-secrets-manager"; // ES Modules import
const client = new SecretsManagerClient();
const input = { "SecretId": process.env.SECRET_NAME }
const command = new GetSecretValueCommand(input);
console.log('Retrieving secret during top-level await')
const secret = await client.send(command);

export async function handler() {
    console.log('Using secret in handler')
    return secret.SecretString;    
};