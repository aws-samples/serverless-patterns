// https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-ssm/classes/getparametersbypathcommand.html
// Input: https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-ssm/interfaces/getparametersbypathcommandinput.html
// Output: https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-ssm/interfaces/getparametersbypathcommandoutput.html
// Parameters will be cached until the execution environment is terminated.
import { SSMClient, GetParametersByPathCommand } from "@aws-sdk/client-ssm";
const ssmClient = new SSMClient();
const input = {
  Path: process.env.ParameterPath,
  Recursive: true,
  WithDecryption: true,
};
const command = new GetParametersByPathCommand(input);
export const config = await ssmClient.send(command);