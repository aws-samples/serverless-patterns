FROM node:12-alpine
RUN mkdir -p /usr/src/serviceB
WORKDIR /usr/src/serviceB
COPY . .
RUN npm install
EXPOSE 3001
CMD [ "node", "index.js" ]
