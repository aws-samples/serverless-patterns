exports.handler = async (event = {}) => {
    return {
      statusCode: 200,
      body: JSON.stringify('Hello from Lambda!'),
      headers: {
          'Content-Type': 'application/json'
      }
    };
  };