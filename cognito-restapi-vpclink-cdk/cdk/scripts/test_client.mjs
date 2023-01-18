#!/usr/bin/env node

/**
 * Installation
 * 
 * curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.2/install.sh | bash
 * nvm install 16.19.0
 * nvm use 16.19.0
 * nvm alias default 16.19.0
 */

import https from 'node:https';
import querystring from 'node:querystring';

const TOKEN_HOSTNAME = `XXXXX.auth.us-east-1.amazoncognito.com`;
const CLIENT_ID = 'XXXXXX';
const CLIENT_SECRET = 'XXXXXX';
const CLIENT_SCOPE = 'finsys/*'; // or finsys/*

const APIGW_HOSTNAME = 'APIGWID-vpce-VPCEID.execute-api.us-east-1.amazonaws.com';

function getToken() {
    const data = querystring.stringify({
        grant_type: 'client_credentials',
        scope: CLIENT_SCOPE
    });
    
    const options = {
        hostname: TOKEN_HOSTNAME,
        path: '/oauth2/token',
        port: 443,
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Content-Length': data.length,
            'Authorization': 'Basic ' + Buffer.from(`${CLIENT_ID}:${CLIENT_SECRET}`).toString('base64')
        }
    }
    console.debug(options);

    return new Promise((resolve, reject) => {
        const req = https.request(options, (res) => {
            console.log('######## TOKEN RESPONSE ###########');
            console.debug('statusCode:', res.statusCode);
            console.debug('headers:', res.headers);
        
            const buffers = [];
        
            res.on('data', (chunk) => buffers.push(chunk));
            res.once('end', () => resolve(Buffer.concat(buffers).toString()));
            res.once('error', reject);
        });
        
        req.once('timeout', () => {
            req.destroy();
        });
        
        req.once('error', reject);
        
        req.write(data);
        req.end();
    });
}

console.log('######## TOKEN REQUEST ###########');

const data = await getToken();
const { access_token: accessToken } = JSON.parse(data);

console.log('######## API REQUEST ###########');

// https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-api-test-invoke-url.html#apigateway-private-api-route53-alias
const options = {
    hostname: APIGW_HOSTNAME,
    path: '/prod',
    port: 443,
    headers: {
        'Authorization': accessToken
    }
}

console.debug(options);

const req = https.get(options, (res) => {
    console.log('######## API RESPONSE ###########');
    console.debug('statusCode:', res.statusCode);
    console.debug('headers:', res.headers);

    const buffers = [];

    res.on('data', (chunk) => buffers.push(chunk));
    res.once('end', () => {
        console.log(Buffer.concat(buffers).toString());
    });
    res.once('error', (err) => {
        console.error(err);
    });
});
    
req.once('timeout', () => {
    req.destroy();
});

req.once('error', (err) => {
    console.error(err);
});
req.end();

