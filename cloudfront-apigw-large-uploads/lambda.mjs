// This is a copy of the file found in lambda.zip.

// Using a small value of 300 bytes to demonstrate the behaviour of Lambda@Edge function.
// In real world applications, you would set this higher.
const MAX_FILE_SIZE = 300;

// Using a random public facing endpoint that will respond to requests.
const LARGE_UPLOAD_ORIGIN = "echo.free.beeceptor.com"; 

export const handler = async (event) => {
    const request = event.Records[0].cf.request;
    const headers = request.headers;
    const origin = event.Records[0].cf.request.origin;

    if (request.method === 'POST') {
        if (headers['content-length'] && parseInt(headers['content-length'][0].value) < MAX_FILE_SIZE ) {
            console.log(`Request size less than: ` + MAX_FILE_SIZE); 
        } else {
            console.log(`Request has no content-length or request size is greater than: ` + MAX_FILE_SIZE);
            origin.custom.domainName = LARGE_UPLOAD_ORIGIN;
            request.headers.host[0].value = LARGE_UPLOAD_ORIGIN;
            request.uri = '/';
        }
    }

    return request;
};