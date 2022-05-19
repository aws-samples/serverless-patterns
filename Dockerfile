# Docker file used for custom GitHub Action to run cfn-nag
FROM beevelop/nodejs-python-ruby:latest

RUN gem install cfn-nag -v 0.8.9

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . ./

RUN ["chmod", "+x", "/usr/src/app/cfn-nag-action/entrypoint.sh"]

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/usr/src/app/cfn-nag-action/entrypoint.sh"]