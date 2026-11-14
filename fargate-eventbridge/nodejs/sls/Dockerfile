FROM amd64/node:18.17-alpine

COPY . .

RUN yarn install

CMD [ "handlers/handler.js" ]

ENTRYPOINT [ "node" ]
