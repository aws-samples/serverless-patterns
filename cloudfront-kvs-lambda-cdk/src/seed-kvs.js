// Utility script to seed the KeyValueStore with sample config
// Run: node src/seed-kvs.js <KVS_ARN>
const { CloudFrontKeyValueStoreClient, PutKeyCommand, DescribeKeyValueStoreCommand } = require('@aws-sdk/client-cloudfront-keyvaluestore');

async function seed() {
  const kvsArn = process.argv[2];
  if (!kvsArn) { console.error('Usage: node seed-kvs.js <KVS_ARN>'); process.exit(1); }

  const client = new CloudFrontKeyValueStoreClient();
  const { ETag } = await client.send(new DescribeKeyValueStoreCommand({ KvsARN: kvsArn }));

  const entries = [
    { Key: '/old-page', Value: '/new-page' },
    { Key: '/docs', Value: 'https://docs.example.com' },
    { Key: 'ab-test-enabled', Value: 'true' }
  ];

  let etag = ETag;
  for (const { Key, Value } of entries) {
    const result = await client.send(new PutKeyCommand({ KvsARN: kvsArn, Key, Value, IfMatch: etag }));
    etag = result.ETag;
    console.log(`Set ${Key} = ${Value}`);
  }
  console.log('KVS seeded successfully');
}
seed().catch(console.error);
