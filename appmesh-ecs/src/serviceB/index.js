const express = require('express');
const app = express();
const xray = require('aws-xray-sdk');
const axios = require('axios');
const serviceC = 'http://servicec.services.local:3001';
const util = require('util');
const http = require('http');

xray.captureHTTPsGlobal(require('http'));
xray.capturePromise();

app.use(xray.express.openSegment('serviceB'));

app.get('/', async (req, res) => {
    const barr = ['Hi', 'Hello', 'Konnichiwa', 'Ohaiyo'];
    const bres = barr[Math.floor(Math.random() * barr.length)];
    try {
        const serviceCRes = await axios.get(serviceC);
        if (typeof serviceCRes === 'object') {
            console.log(`serviceC (obj): ${util.inspect(serviceCRes)}`);
        } else {
            console.log(`serviceC (str): ${serviceCRes}`);
        }
        res.send(`${bres} ${serviceCRes.data}`);
    } catch (e) {
        console.log(`Error getting serviceC: ${e}`);
        res.send(e);
    }
});

app.get('/health', async(req, res) => {
    res.sendStatus(200);
});

app.use(xray.express.closeSegment());

app.listen(3001, () => {
    console.log(`ServiceB started`);
})