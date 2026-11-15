export const handler = async (event) => {
    // TODO implement
    const response = 
      {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": "<h1>Hello from AWS !!! <br><br> This is CloudFront to Lambda Function URL integration with Origin Access Control (OAC)</h1>"
    };
    return response;
  };
  