const express = require("express");
const app = express();
const port = 80;

var AWS = require('aws-sdk');
const Pool = require('pg').Pool

var client = new AWS.SecretsManager({
  region: process.env.REGION
});

var pool;

client.getSecretValue({ SecretId: 'aurora-serverless-global-db-secret' }, function (err, data) {
  if (err) {
    console.log(err, err.stack);
  }
  else {
    secretParams = JSON.parse(data.SecretString);
    pool = new Pool({
      user: secretParams.username,
      host: process.env.DB_HOST,
      database: 'sample',
      password: secretParams.password,
      port: process.env.DB_PORT
    });
  }
});

app.use(express.urlencoded({ extended: false }));
app.use(express.json());

const errorHandler = (error, request, response) => {
  console.log(`error ${error.message}`)
  const status = error.status || 400
  response.status(status).send(`error : ${error.message}`)
}

app.get('/', (req, res) => {
  res.status(200).send('Hello from Fargate Test App :-)');
});


app.get('/init', (req, res) => {
  pool.query('CREATE TABLE IF NOT EXISTS tasks ( ID SERIAL PRIMARY KEY,name VARCHAR(30), status VARCHAR(30))', (error, results) => {
    if (error) {
      return errorHandler(error, req, res)
    }
    res.status(200).json('Task table created..')
  })

});

app.get('/tasks', (req, res) => {
  pool.query('SELECT * FROM tasks ORDER BY id ASC', (error, results) => {
    if (error) {
      return errorHandler(error, req, res)
    }
    res.status(200).json(results.rows)
  })
});

app.get('/tasks/:id', (req, res) => {
  const id = parseInt(req.params.id)
  pool.query('SELECT * FROM tasks WHERE id = $1', [id], (error, results) => {
    if (error) {
      return errorHandler(error, req, res)
    }
    res.status(200).json(results.rows)
  })
});

app.post('/tasks', (req, res) => {
  const { name, status } = req.body
  pool.query('INSERT INTO tasks (name, status) VALUES ($1, $2) RETURNING id', [name, status], (error, results) => {
    if (error) {
      return errorHandler(error, req, res)
    }
    console.log(results)
    res.status(201).send(`Task added with ID: ${results.rows[0].id}`)
  })

});

app.put('/tasks/:id', (req, res) => {
  const id = parseInt(req.params.id)
  const { name, status } = req.body
  pool.query('UPDATE tasks SET name = $1, status = $2 WHERE id = $3', [name, status, id], (error, results) => {
    if (error) {
      return errorHandler(error, req, res)
    }
    res.status(200).send(`Task modified with ID: ${id}`)
  }
  )

});

app.delete('/tasks/:id', (req, res) => {
  const id = parseInt(req.params.id)
  pool.query('DELETE FROM tasks WHERE id = $1', [id], (error, results) => {
    if (error) {
      return errorHandler(error, req, res)
    }
    res.status(200).send(`Task deleted with ID: ${id}`)
  })
});

app.use(errorHandler)

app.listen(port, () => {
  console.log(`server started at http://localhost:${port}`);
});