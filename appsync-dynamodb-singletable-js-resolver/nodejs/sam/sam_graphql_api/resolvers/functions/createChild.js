import { util } from '@aws-appsync/utils';

export function request(ctx) {
  const { PK, SK, ...values } = ctx.arguments;
  return dynamodbPutRequest({ key: { PK, SK }, values: { ...values, type: "Child" } });
}

export function response(ctx) {
  return ctx.result;
}

function dynamodbPutRequest({ key, values }) {
  return {
    operation: 'PutItem',
    key: util.dynamodb.toMapValues(key),
    attributeValues: util.dynamodb.toMapValues(values)
  };
}