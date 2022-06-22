// Declare constants reqiured for the signature process
const crypto = require('crypto');
const qs = require('querystring');
const emptyHash = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855';
// CloudFront includes the x-amz-cf-id header in the signature for custom origins
const signedHeadersCustomOrigin = 'host;x-amz-cf-id;x-amz-content-sha256;x-amz-date;x-amz-security-token';
// Retrieve the temporary IAM credentials of the function that were granted by
// the Lambda@Edge service based on the function permissions. In this solution, the function
// is given permissions to read from S3 and decrypt using the KMS key.
const { AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN } = process.env;

// Since the function is configured to be executed on origin request events, the handler
// is executed every time CloudFront needs to go back to the origin, which is S3 here.
exports.handler = async event => {
    console.log("xx event=" + JSON.stringify(event))
    // Retrieve the original request that CloudFront was going to send to S3
    const request = event.Records[0].cf.request;

    // The request object has different properties depending on the type of
    // origin that is being used. Account for that here.
    let originType = '';
    if (request.origin.hasOwnProperty('custom'))
        originType = 'custom';
    else
        throw("Unexpected origin type. Expected 'custom'. Got: " + JSON.stringify(request.origin));

    // Create a JSON object with the fields that should be included in the Sigv4 request,
    // including the X-Amz-Cf-Id header that CloudFront adds to every request forwarded
    // upstream. This header is exposed to Lambda@Edge in the event object
    const sigv4Options = {
        method: request.method,
        path: request.origin[originType].path + request.uri,
        query: request.querystring,
        credentials: {
            accessKeyId: AWS_ACCESS_KEY_ID,
            secretAccessKey: AWS_SECRET_ACCESS_KEY,
            sessionToken: AWS_SESSION_TOKEN
        },
        host: request.headers['host'][0].value,
        xAmzCfId: event.Records[0].cf.config.requestId,
        originType: originType
    };

    console.log(sigv4Options)

    // Compute the signature object that includes the following headers: X-Amz-Security-Token, Authorization,
    // X-Amz-Date, X-Amz-Content-Sha256, and X-Amz-Security-Token
    const signature = signV4(sigv4Options);

    // Finally, add the signature headers to the request before it is sent to S3
    for(var header in signature){
        request.headers[header.toLowerCase()] = [{
            key: header,
            value: signature[header].toString()
        }];
    }
    console.log("request=" + JSON.stringify(request))
    return request;
};


// Helper functions to sign the request using AWS Signature Version 4
function signV4(options) {
    // Infer the region from the host header
    // Create the canonical request
    const region = options.host.split('.')[2];
    const date = (new Date()).toISOString().replace(/[:-]|\.\d{3}/g, '');
    let canonicalHeaders = '';
    let signedHeaders = '';
    canonicalHeaders = ['host:'+options.host, 'x-amz-cf-id:'+options.xAmzCfId, 'x-amz-content-sha256:'+emptyHash, 'x-amz-date:'+date, 'x-amz-security-token:'+options.credentials.sessionToken].join('\n');
    signedHeaders = signedHeadersCustomOrigin;
    const requestParameters = createCanonicalQS(options.query);

    const canonicalURI = encodeRfc3986(encodeURIComponent(decodeURIComponent(options.path).replace(/\+/g, ' ')).replace(/%2F/g, '/'));
    const canonicalRequest = [options.method, canonicalURI, requestParameters, canonicalHeaders + '\n', signedHeaders,emptyHash].join('\n');
    console.log("canonicalRequest="+canonicalRequest);
    // Create string to sign
    const credentialScope = [date.slice(0, 8), region, 'execute-api/aws4_request'].join('/');
    const stringToSign = ['AWS4-HMAC-SHA256', date, credentialScope, hash(canonicalRequest, 'hex')].join('\n');
    // Calculate the signature
    const signature = hmac(hmac(hmac(hmac(hmac('AWS4' + options.credentials.secretAccessKey, date.slice(0, 8)), region), "execute-api"), 'aws4_request'), stringToSign, 'hex');
    // Form the authorization header
    const authorizationHeader = ['AWS4-HMAC-SHA256 Credential=' + options.credentials.accessKeyId + '/' + credentialScope,'SignedHeaders=' + signedHeaders,'Signature=' + signature].join(', ');

    // return required headers for Sigv4 to be added to the request
    return {
        'Authorization': authorizationHeader,
        'X-Amz-Content-Sha256' : emptyHash,
        'X-Amz-Date': date,
        'X-Amz-Security-Token': options.credentials.sessionToken
    };
}

function createCanonicalQS(input_qs){
	let canonicalQS='';
	let qsparsed = qs.parse(input_qs);
	Object.keys(qsparsed).sort().forEach((param)=>{
		canonicalQS += encodeQS(param)+'='+encodeQS(qsparsed[param])+'&'
	});
	canonicalQS = canonicalQS.slice(0, -1);

	return canonicalQS;
}

function encodeQS(input_str){
	return input_str.replace(/[!'()*=]/g, c => '%' + c.charCodeAt(0).toString(16).toUpperCase())
}

function encodeRfc3986(urlEncodedStr) {
  return urlEncodedStr.replace(/[!'()*]/g, c => '%25' + c.charCodeAt(0).toString(16).toUpperCase())
}

function hash(string, encoding) {
  return crypto.createHash('sha256').update(string, 'utf8').digest(encoding)
}

function hmac(key, string, encoding) {
  return crypto.createHmac('sha256', key).update(string, 'utf8').digest(encoding)
}