exports.handler = async (event) => {
  event.Records.forEach((record) => {
    console.log(`Event Name: ${JSON.stringify(record.eventName)}`);
    // #TODO: Show record information
    // console.log(`MSK Request: ${JSON.stringify(record.s3)}`);
    
  });
};