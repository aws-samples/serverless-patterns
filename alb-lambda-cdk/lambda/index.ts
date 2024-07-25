export const handler = async (event: any = {}): Promise<any> => {
  return {
    statusCode: 200,
    body: JSON.stringify('Hello from Updtaed Lambda!'),
    headers: {
        'Content-Type': 'application/json'
    }
  };
};
