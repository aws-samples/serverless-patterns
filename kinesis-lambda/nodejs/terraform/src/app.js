//Sample lambda code

exports.handler = async (event) => {
    console.log('Received Kinesis records:', JSON.stringify(event, null, 2));
    // Process each Kinesis record
    event.Records.forEach((record) => {
      const payload = Buffer.from(record.kinesis.data, 'base64').toString('utf-8');
      console.log('Record payload:', payload);
      // Add your processing logic here
    });
    return {
      statusCode: 200,
      body: 'Processed Kinesis records successfully',
    };
  };