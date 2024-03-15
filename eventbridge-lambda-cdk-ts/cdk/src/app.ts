export async function main( event: any ) {
    console.log('Event: ', event);

    return {
      statusCode: 200,
      body: 'Hello World!',
    };
  }