# TypeScript Express server without Docker

Run the following to start the server on port 80:

```bash
npm install
npm run start
```

# TypeScript Express server with Docker

Run the following to start the server on port 80:

```bash
docker build . -t ts-express
docker run -p 80:80 --name ts-app ts-express
```