const redis = require('ioredis');

const client = new redis({
  port: process.env.REDIS_PORT,
  host: process.env.REDIS_HOST,
  maxRetriesPerRequest: 20,
});

client.on('connect', function () {
  console.log('connected');
});

exports.handler = async function (event) {
  await client.set('foo', 'bar');
  let result = await client.get('foo');
  return {
    statusCode: 200,
    headers: { 'Content-Type': 'text/plain' },
    body: result,
  };
};
