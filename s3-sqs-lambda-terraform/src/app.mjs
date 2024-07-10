console.log('Loading function');

export const handler = async (event, context) => {
    //console.log('Received event:', JSON.stringify(event, null, 2));
    console.log('value1 =', event.key1);
    return event.key1;  // Echo back the first key value
    // throw new Error('Something went wrong');
};
