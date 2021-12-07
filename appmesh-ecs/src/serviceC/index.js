const express = require('express');
const app = express();
const axios = require('axios');
const xray = require('aws-xray-sdk');

app.use(xray.express.openSegment('serviceC'));

app.get('/', async(req, res) => {
    const carr = ['there', 'world', 'friend'];
    const cres = carr[Math.floor(Math.random() * carr.length)];
    res.send(cres);
});

app.get('/health', async(req, res) => {
    res.sendStatus(200);
});

app.use(xray.express.closeSegment());

app.listen(3001, () => {
    console.log(`ServiceC started`);
})