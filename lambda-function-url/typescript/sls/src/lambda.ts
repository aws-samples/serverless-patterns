import { APIGatewayProxyEventV2WithRequestContext } from "aws-lambda"

export const handler = async (event: APIGatewayProxyEventV2WithRequestContext<any>) => {
    
  console.info('event received:', event);
  
  const method = event.requestContext.http.method;
  
  let responseCode = 200
  let responseMsg = ""

  if (method === 'GET') {
    responseMsg = "hello from a lambda function url"
  } else if (method === 'POST') {
    responseMsg = JSON.stringify({ "output":"added", ...JSON.parse(event.body)})
  } else {
    responseCode = 400
    responseMsg = `Invalid HTTP method: ${method}`
  }  
  
  const response = {
    statusCode: responseCode,
    body: responseMsg
  };
 
  console.info(`response from: ${event.requestContext.domainName} statusCode: ${response.statusCode} body: ${response.body}`);
  return response;
}
