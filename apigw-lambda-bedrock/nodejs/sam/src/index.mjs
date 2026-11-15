// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
//  SPDX-License-Identifier: MIT-0
import { BedrockRuntimeClient, InvokeModelCommand } from "@aws-sdk/client-bedrock-runtime";

export const handler = async (event) => {
  const client = new BedrockRuntimeClient();
  //console.log(event)
  let prompt=JSON.parse(event.body).prompt
  //console.log(prompt)
  //const prompt = 'Write a text to be posted on my social media channels about how Amazon Bedrock works';
  const body = {
    anthropic_version: "bedrock-2023-05-31",
    messages: [
      {
        role: "user",
        content: [
          {
            "type": "text",
            "text": prompt
          }
        ],
      },
    ],
    max_tokens: 200
  };
  const input = {
    body: JSON.stringify(body),
    contentType: "application/json",
    accept: "application/json",
    modelId: "global.anthropic.claude-sonnet-4-5-20250929-v1:0",
  };
  const command = new InvokeModelCommand(input);
  const res = await client.send(command);
  //console.log(res)
  let stringifiedResponse = Buffer.from(res.body).toString();
  //console.log(JSON.stringify(stringifiedResponse));
  const response = {
    statusCode: 200,
    body: stringifiedResponse,
  };
  return response;
};
