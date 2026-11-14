import * as cognito from "@aws-sdk/client-cognito-identity-provider";
import { REGION, USER_POOL_ID, CLIENT_USER_POOL_ID } from "../constants";

const cognitoClient = new cognito.CognitoIdentityProviderClient({
  region: REGION,
});

const userpool = USER_POOL_ID;
const userpoolClient = CLIENT_USER_POOL_ID;

export const a_user_signs_up = async (
  password: string,
  email: string,
  given_name: string,
  family_name: string
): Promise<string> => {
  const userPoolId = userpool;
  const clientId = userpoolClient;
  const username = email;

  console.log(`[${email}] - signing up...`);

  const command = new cognito.SignUpCommand({
    ClientId: clientId,
    Username: username,
    Password: password,
    UserAttributes: [
      { Name: "email", Value: email },
      { Name: "custom:firstName", Value: given_name },
      { Name: "custom:lastName", Value: family_name },
    ],
  });

  const signUpResponse = await cognitoClient.send(command);
  const userSub = signUpResponse.UserSub;

  const adminCommand: cognito.AdminConfirmSignUpCommandInput = {
    UserPoolId: userPoolId as string,
    Username: userSub as string,
  };

  const result = await cognitoClient.send(
    new cognito.AdminConfirmSignUpCommand(adminCommand)
  );

  console.log("CONFIRM SIGNUP RESPONSE", result);

  console.log(`[${email}] - confirmed sign up`);

  return userSub as string;
};
