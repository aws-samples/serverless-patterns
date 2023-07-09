"use strict";
import { CognitoJwtVerifier } from "aws-jwt-verify";
import { SSMClient, GetParameterCommand } from "@aws-sdk/client-ssm";

const ssm = new SSMClient({ region: "us-east-1" });
let verifier = "";

async function init() {
  const userPoolId = await getParameter("cognitoAuthUserPoolId");
  const appClientId = await getParameter("cognitoAuthAppClientId");
  verifier = CognitoJwtVerifier.create({
    userPoolId: userPoolId,
    tokenUse: "access",
    clientId: appClientId,
  });
}

const createVerifier = init();

async function getParameter(name) {
  const input = {
    Name: name,
  };
  const command = new GetParameterCommand(input);
  const response = await ssm.send(command);

  return response.Parameter.Value;
}

exports.handler = async (event, context, callback) => {
  await createVerifier;
  const request = event.Records[0].cf.request;
  console.log(request);
  const authHeader = request.headers["authorization"][0].value;

  try {
    const payload = await verifier.verify(authHeader);
    console.log("Token is valid. Payload:", payload);

    callback(null, request);
  } catch (err) {
    console.log("Token not valid!", err);

    callback(null, {
      status: "403",
      body: "Unauthorized",
    });
  }
};
