import * as cognito from "@aws-sdk/client-cognito-identity-provider";

import Chance from "chance";
import { REGION, USER_POOL_ID, CLIENT_USER_POOL_ID } from "../constants";
const cognitoClient = new cognito.CognitoIdentityProviderClient({
  region: REGION,
});

const chance = new Chance();

const userpool = USER_POOL_ID;
const userpoolClient = CLIENT_USER_POOL_ID;

export const a_random_user = () => {
  const given_name = chance.first({ nationality: "en" });
  const family_name = chance.first({ nationality: "en" });
  const password = ensurePasswordPolicy(
    chance.string({
      length: 12,
      pool: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+",
    })
  );
  console.log("password: ", password);
  const email = `${given_name}-${family_name}@dev.com`;
  return { given_name, family_name, password, email };
};

function ensurePasswordPolicy(password: string): string {
  let newPassword = password;
  if (!/[a-z]/.test(newPassword))
    newPassword += chance.letter({ casing: "lower" });
  if (!/[A-Z]/.test(newPassword))
    newPassword += chance.letter({ casing: "upper" });
  if (!/[0-9]/.test(newPassword))
    newPassword += chance.integer({ min: 0, max: 9 }).toString();
  if (!/[!@#$%^&*()_+]/.test(newPassword))
    newPassword += chance.pickone([
      "!",
      "@",
      "#",
      "$",
      "%",
      "^",
      "&",
      "*",
      "(",
      ")",
      "_",
      "+",
    ]);
  return newPassword; // Ensure the password is still 12 characters long
}

export const an_authenticated_user = async (): Promise<any> => {
  const { given_name, family_name, email, password } = a_random_user();

  const userPoolId = userpool;
  const clientId = userpoolClient;
  console.log("userPoolId", userPoolId);
  console.log("clientId", clientId);

  console.log(`[${email}] - signing up...`);

  const command = new cognito.SignUpCommand({
    ClientId: clientId,
    Username: email,
    Password: password,
    UserAttributes: [
      { Name: "firstName", Value: given_name },
      {
        Name: "lastName",
        Value: family_name,
      },
    ],
  });

  const signUpResponse = await cognitoClient.send(command);
  const userSub = signUpResponse.UserSub;

  console.log(`${userSub} - confirming sign up`);

  const adminCommand: cognito.AdminConfirmSignUpCommandInput = {
    UserPoolId: userPoolId as string,
    Username: userSub as string,
  };

  await cognitoClient.send(new cognito.AdminConfirmSignUpCommand(adminCommand));

  console.log(`[${email}] - confirmed sign up`);

  const authRequest: cognito.InitiateAuthCommandInput = {
    ClientId: process.env.CLIENT_USER_POOL_ID as string,
    AuthFlow: "USER_PASSWORD_AUTH",
    AuthParameters: {
      USERNAME: email,
      PASSWORD: password,
    },
  };

  const authResponse = await cognitoClient.send(
    new cognito.InitiateAuthCommand(authRequest)
  );

  console.log(`${email} - signed in`);

  return {
    username: userSub as string,
    name: `${given_name} ${family_name}`,
    email,
    idToken: authResponse.AuthenticationResult?.IdToken as string,
    accessToken: authResponse.AuthenticationResult?.AccessToken as string,
  };
};
