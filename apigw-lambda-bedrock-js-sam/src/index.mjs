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
        'prompt': "\n\nHuman:" + prompt + "\n\nAssistant:",
        "temperature": 0.5,
        "top_p": 1,
        "top_k": 250,
        "max_tokens_to_sample": 200,
        "stop_sequences": ["\n\nHuman:"]
    }
  const input = {
    body: JSON.stringify(body),
    contentType: "application/json",
    accept: "application/json",
    modelId: "anthropic.claude-v2",
  };
  const command = new InvokeModelCommand(input);
  const res = await client.send(command);
  //console.log(res)
  let stringifiedResponse = Buffer.from(res.body).toString();
  //console.log(JSON.stringify(stringifiedResponse));
  const response = {
    statusCode: 200,
    body: JSON.stringify(stringifiedResponse),
  };
  return response;
};