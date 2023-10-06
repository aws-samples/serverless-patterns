FROM --platform=linux/amd64 node:16-alpine
WORKDIR /usr
COPY package.json ./
COPY src ./src
RUN npm install
RUN npm install pg
COPY . .
EXPOSE 80
CMD ["npm","start"]