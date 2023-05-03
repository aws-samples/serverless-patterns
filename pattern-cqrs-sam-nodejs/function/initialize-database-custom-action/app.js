
import { EventBridgeClient, PutEventsCommand } from "@aws-sdk/client-eventbridge";
import { request } from 'node:https';
import { parse } from 'node:url';

const ebClient = new EventBridgeClient();

export const params = {
  Entries: [
    {
      DetailType: "initializeDatabase",
      Source: "orderPipeline",
      EventBusName: process.env.EVENTBUS_NAME,
      Time: new Date(),
      Detail: "{}"
    },
  ],
};

export async function handler(event, context) {
  
  console.log("REQUEST RECEIVED:\n" + JSON.stringify(event));
  
  var responseStatus = "FAILED";
  var responseData = {};
  
  if (event.RequestType == "Delete" || event.RequestType == "Update") {
    await sendResponse(event, context, "SUCCESS");
    return;
  }
    
    
  console.log('Emitting Event to EventBridge');
  
  try {
    
    console.log("Sending event to EventBridge:", params);

    const data = await ebClient.send(new PutEventsCommand(params));
    
    console.log("Success, event sent; requestID:", data);
    
    responseData.requestID = data;
    
    responseStatus = "SUCCESS";
    await sendResponse(event, context, responseStatus, responseData);

  }  
  catch (e){
       console.log('Error Sending event to EventBridge : ' + JSON.stringify(e))
       await sendResponse(event, context, responseStatus, responseData);
  }
}

// Send response to the pre-signed S3 URL 
async function sendResponse(event, context, responseStatus, responseData) {
  
  try{
    var cfnParameters = {
        Status: responseStatus,
        Reason: "See the details in CloudWatch Log Stream: " + context.logStreamName,
        StackId: event.StackId,
        RequestId: event.RequestId,
        LogicalResourceId: event.LogicalResourceId,
        Data: responseData
    }
    
    if (event.RequestType == "Delete" || event.RequestType == "Update") {
      cfnParameters.PhysicalResourceId = event.PhysicalResourceId
    } else {
      cfnParameters.PhysicalResourceId = "DatabaseInitializationCustomResource"
    }
    
    var responseBody = JSON.stringify(cfnParameters);
    
    console.log("RESPONSE BODY:\n", responseBody);
    

    var parsedUrl = parse(event.ResponseURL);
    var options = {
        hostname: parsedUrl.hostname,
        port: 443,
        path: parsedUrl.path,
        method: "PUT",
        headers: {
            "content-type": "",
            "content-length": responseBody.length
        }
    };    
    
    console.log("SENDING RESPONSE...\n",options);
    
    return new Promise((resolve, reject) => {
      const req = request(options, (response) => {
        console.log("STATUS: " + response.statusCode);
        console.log("HEADERS: " + JSON.stringify(response.headers));
        // Tell AWS Lambda that the function execution is done  
        context.done();      
      
      
      }).on('error', (err) => reject(err));
      // write data to request body
      req.write(responseBody);
      req.end();
    });
    
  } catch (error) {
    console.log("sendResponse Error:" + error);
  }
}