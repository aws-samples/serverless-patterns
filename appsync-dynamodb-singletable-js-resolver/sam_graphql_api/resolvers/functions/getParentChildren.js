import { util } from '@aws-appsync/utils';

export function request(ctx) {
  const { PK, SK } = ctx.args;
  return dynamoDBQueryRequest({ parentPK: PK, parentSK: SK });
}

export function response(ctx) {
  ctx.stash.children = ctx.result?.items;
  return ctx.result?.items;
}

function dynamoDBQueryRequest({ parentPK, parentSK }) {
  return {
    operation: 'Query',
    index: 'ParentGSI',
    query: {
      "expression" : "parentPK = :parentPK and parentSK = :parentSK",
      "expressionValues" : {
          ":parentPK" : util.dynamodb.toDynamoDB(parentPK),
          ":parentSK" : util.dynamodb.toDynamoDB(parentSK)
      }
    }
  };
}