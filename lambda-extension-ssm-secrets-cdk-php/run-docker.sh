#!/bin/sh
#set -x

cd /app

npm ci

cd /app/php
composer install --no-scripts

php -a
