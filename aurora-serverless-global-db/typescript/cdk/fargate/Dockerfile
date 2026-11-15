FROM --platform=linux/amd64 node:22-alpine AS build
WORKDIR /usr
COPY package.json ./
COPY src ./src
RUN npm install --omit=dev
COPY . .
EXPOSE 80
CMD ["node","src/index.js"]
