// /* eslint-disable */

export const listObjects = /* GraphQL */ `
  query ListObjects($limit: Int, $nextToken: String) {
    listObjects(limit: $limit, nextToken: $nextToken) {
      items {
        ObjectId
        Version
        DetailType
        Source
        FileName
        FilePath
        AccountId
        CreatedAt
        Region
        CurrentBucket
        OriginalBucket
        ObjectSize
        SourceIPAddress
        LifecycleConfig
      }
      nextToken
    }
  }
`;

export const getObject = /* GraphQL */ `
  query GetObject($ObjectId: String!) {
    getObject(ObjectId: $ObjectId) {
      ObjectId
      Version
      DetailType
      Source
      FileName
      FilePath
      AccountId
      CreatedAt
      Region
      CurrentBucket
      OriginalBucket
      ObjectSize
      SourceIPAddress
      LifecycleConfig
    }
  }
`;
