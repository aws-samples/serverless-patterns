#!/bin/bash

function usage {
    echo "usage: build.sh [-i image_name] [-a account] [-r region]"
    echo "Required:"
    echo "  -i        Used to specify the build container image."
    echo "  -a        Used to specify the account"
    echo "  -r        Used to specify the region"
    exit 1
}

image_flag=false
account_flag=false
region_flag=false

while getopts ":i:a:r:" opt; do
    case "$opt" in
        i) image_flag=true; imagename=$OPTARG;;
        a) account_flag=true; accountid=$OPTARG;;
        r) region_flag=true; regionname=$OPTARG;;
        h) usage; exit;;
        \?) echo "Unknown option: -$OPTARG" >&2; usage;exit 1;;
        :) echo "Missing option argument for -$OPTARG" >&2; usage;exit 1;;
        *) echo "Invalid option: -$OPTARG" >&2; usage; exit 1;;
    esac
done

if  ! $image_flag
then
    echo "The image name (-i) must be included for a build to run" >&2
fi

if  ! $account_flag
then
    echo "The account id (-a) must be included for a build to run" >&2
fi

if  ! $region_flag
then
    echo "The region (-r) must be included for a build to run" >&2
fi

if  ! $image_flag ||  ! $account_flag || ! $region_flag
then
    exit 1
fi

# Login to ECR
echo ECR Login
aws ecr get-login-password --region $regionname | docker login --username AWS --password-stdin $accountid.dkr.ecr.$regionname.amazonaws.com
docker build -t $imagename --network=host .
docker tag $imagename:latest $accountid.dkr.ecr.$regionname.amazonaws.com/$imagename:latest

repositories=`aws ecr describe-repositories --region $regionname`
REPO_LIST=$(aws ecr describe-repositories --query "repositories[].repositoryName" --output text --region $regionname)
for repo in $REPO_LIST; do
  if [ "$repo" == "$imagename" ] ; then
      echo "Found existing repo for $imagename. Pushing image to this repo"
      docker push $accountid.dkr.ecr.$regionname.amazonaws.com/$imagename:latest
      echo build completed on `date`
      exit 0
  fi
done
echo "No existing repo $imagename found. Creating one and pushing image to this repo"
aws ecr create-repository --repository-name $imagename --region $regionname
docker push $accountid.dkr.ecr.$regionname.amazonaws.com/$imagename:latest
echo build completed on `date`

