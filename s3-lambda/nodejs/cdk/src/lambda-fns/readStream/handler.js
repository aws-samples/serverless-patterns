exports.handler = async (event) => {
  event.Records.forEach((record) => {
    console.log(`Event Name: ${JSON.stringify(record.eventName)}`);
    console.log(`S3 Request: ${JSON.stringify(record.s3)}`);
  });
};