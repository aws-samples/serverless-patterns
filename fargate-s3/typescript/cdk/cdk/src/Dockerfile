FROM --platform=linux/amd64 node:22-alpine AS build
WORKDIR /usr
COPY package.json ./
COPY tsconfig.json ./
COPY src ./src
RUN npm install
RUN npm run build

FROM --platform=linux/amd64 node:22-alpine
WORKDIR /usr
COPY package.json ./
RUN npm install --omit=dev
COPY --from=build /usr/dist .
EXPOSE 80
CMD ["node","index.js"]
