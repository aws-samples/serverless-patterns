#!/bin/bash
set -eo pipefail
rm -rf dependencies/python
cd src
pip install --target ../dependencies/python -r ../requirements.txt
wget -O ../dependencies/python/global-bundle.pem https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem 
