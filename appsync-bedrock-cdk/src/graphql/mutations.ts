/* tslint:disable */
/* eslint-disable */
// this is an auto generated file. This will be overwritten

import * as APITypes from "../API";
type GeneratedMutation<InputType, OutputType> = string & {
  __generatedMutationInput: InputType;
  __generatedMutationOutput: OutputType;
};

export const invoke = /* GraphQL */ `mutation Invoke($prompt: String!) {
  invoke(prompt: $prompt)
}
` as GeneratedMutation<
  APITypes.InvokeMutationVariables,
  APITypes.InvokeMutation
>;
