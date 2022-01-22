# TypeScript Express server without docker

Run the following to start the server on port 80:

```bash
npm install
npm run start
```

# TypeScript Express server with docker

```bash
docker build . -t tsexpress
docker run -d -p 80:80 --env region=<AWS_REGION> --name ts-app tsexpress
```