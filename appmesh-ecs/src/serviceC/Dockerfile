FROM node:12-alpine
RUN mkdir -p /usr/src/serviceC
WORKDIR /usr/src/serviceC
COPY . .
RUN npm install
EXPOSE 3001
CMD [ "node", "index.js" ]
