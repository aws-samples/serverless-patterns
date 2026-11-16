const express = require('express')
const app = express()
const port = process.env['PORT'] || 8080


app.get('/', (req, res) => {
    console.log('path root')
    res.send('Hi there!')
})

app.get('/hello', (req, res) => {
    console.log('path hello')

    res.send('Hello endpoint')
})

app.get('/test', (req, res) => {
    console.log('path test')

    const name = req.query.name;

    res.send('Hello '+ name)
})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})