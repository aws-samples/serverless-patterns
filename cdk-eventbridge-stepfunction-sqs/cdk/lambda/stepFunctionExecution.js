exports.handler = async function(event) {
  const eventInput = typeof event == 'object' ? event : JSON.parse(event);
  console.log(eventInput);
  if (eventInput.detail.failure) {
    throw new Error('Failure Exception');
  } else {
    console.log("request:", JSON.stringify(event, undefined, 2));
    return {
      statusCode: 200,
      processedInput: {
        transactionStatus: 'completed',
      },
      sourceEvent: eventInput,
    };
  }
};