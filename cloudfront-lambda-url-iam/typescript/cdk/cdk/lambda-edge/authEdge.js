const axios = require('axios');
const { SignatureV4 } = require('@smithy/signature-v4');
const { HttpRequest } = require('@smithy/protocol-http');
const { Sha256 } = require('@aws-crypto/sha256-js');

const {
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_SESSION_TOKEN,
} = process.env;

const sigv4 = new SignatureV4({
    service: 'lambda',
    region: 'eu-central-1', // Modify to fit your own region
    credentials: {
        accessKeyId: AWS_ACCESS_KEY_ID,
        secretAccessKey: AWS_SECRET_ACCESS_KEY,
        sessionToken: AWS_SESSION_TOKEN,
    },
    sha256: Sha256,
});

module.exports.handler = async (event) => {
    const cfRequest = event.Records[0].cf.request;

    const apiUrl = new URL(`https://${cfRequest.origin.custom.domainName}${cfRequest.uri}`);

    const request = new HttpRequest({
        method: cfRequest.method,
        hostname: apiUrl.hostname,
        path: apiUrl.pathname + (cfRequest.querystring ? `?${cfRequest.querystring}` : ''),
        protocol: apiUrl.protocol,
        headers: {
            host: apiUrl.hostname,
        },
    });

    try {
        return await signAndForwardRequest(request, apiUrl);
    } catch (error) {
        console.error('An error occurred', error);
        return {
            status: '500',
            statusDescription: 'Internal Server Error',
            body: 'Internal Server Error',
        };
    }
};

async function signAndForwardRequest(request, apiUrl) {
    const signed = await sigv4.sign(request);
    const result = await axios({
        method: signed.method,
        url: apiUrl.href,
        headers: signed.headers,
        timeout: 5000,
    });

    return {
        status: '200',
        statusDescription: 'OK',
        body: JSON.stringify(result.data),
    };
}

