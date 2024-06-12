#!/bin/sh

cd /app

npm ci

cd /app/php
composer install --no-scripts

php -a
