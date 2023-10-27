import { Handler } from 'aws-lambda';

export const handler: Handler = async (event, context) => {

    const method = event.requestContext.http.method;

    const returnBody = {"type":"g","score":0,"_id":"links","coo":[],"data":{}};

    return {
      statusCode: 200,
      body: JSON.stringify(returnBody),
    };

    if (method === 'GET') {
        return await getHello(event)
     } else if (method === 'POST') {
        return await save(event);
     } else {
         return {
             statusCode: 400, 
             body: 'Not a valid operation'
         };
     }  
};

async function save(event : any) {
    const name = event.queryStringParameters.name;
  
    const item = {
      name: name,
      date: Date.now(),
    };
  
    console.log(item);
    const savedItem = await saveItem(item);
  
    return {
      statusCode: 200,
      body: JSON.stringify(savedItem),
    };
  }
  
async function getHello(event : any ) {

}
  
async function getItem(name : string ) {

}
  
async function saveItem(item : any) {

}