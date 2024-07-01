# syntax=docker/dockerfile:1.4
ARG PHP_VERSION=8.3

FROM php:${PHP_VERSION}-alpine AS base-env

WORKDIR /tmp
RUN apk add --no-cache \
    libstdc++ nodejs npm \
    #  awscli \
    && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm awscliv2.zip \
    # composer \
    && wget https://getcomposer.org/installer \
    && php ./installer && rm installer \
    && mv composer.phar /usr/local/bin/composer

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm ci

COPY ./run-docker.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/run-docker.sh

CMD ["/usr/local/bin/run-docker.sh"]
