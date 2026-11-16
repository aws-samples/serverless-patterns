FROM --platform=linux/amd64 node:24-alpine

COPY . .

RUN yarn install

CMD [ "handlers/handler.js" ]

ENTRYPOINT [ "node" ]
