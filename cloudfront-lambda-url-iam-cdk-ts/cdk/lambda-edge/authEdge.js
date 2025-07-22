const axios = require('axios');
const { SignatureV4 } = require('@aws-sdk/signature-v4');
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
    const headers = cfRequest.headers;

    const apiUrl = new URL(`https://${cfRequest.origin.custom.domainName}${cfRequest.uri}`);

    const signV4Options = {
        method: cfRequest.method,
        hostname: apiUrl.host,
        path: apiUrl.pathname + (cfRequest.querystring ? `?${cfRequest.querystring}` : ''),
        protocol: apiUrl.protocol,
        query: cfRequest.querystring,
        headers: {
            host: apiUrl.hostname
        },
    };

    try {
        return await signAndForwardRequest(signV4Options, apiUrl);
    } catch (error) {
        console.error('An error occurred', error);
        return {
            status: '500',
            statusDescription: 'Internal Server Error',
            body: 'Internal Server Error',
        };
    }
};

async function signAndForwardRequest(signV4Options, apiUrl) {
    const signed = await sigv4.sign(signV4Options);
    const result = await axios({
        ...signed,
        url: apiUrl.href,
        timeout: 5000
    });

    return {
        status: '200',
        statusDescription: 'OK',
        body: JSON.stringify(result.data),
    };
}

