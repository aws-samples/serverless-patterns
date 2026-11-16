# Usage

## Build the python task to read files from a S3 bucket when triggered by EventBridge

* Build the Docker image first in local
    
    docker build -t `<image name>`:latest .

* Publish the image to ECR and provide the image name, AWS region and AWS Account Number
    
    ./build.sh -i `<image name>` -r `<region>` -a `<account>`


