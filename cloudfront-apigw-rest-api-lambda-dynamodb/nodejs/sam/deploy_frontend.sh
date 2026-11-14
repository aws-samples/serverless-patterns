#!/bin/bash
##
# Deploys the front-end
##

txtgrn=$(tput setaf 2) # Green
txtylw=$(tput setaf 3) # Yellow
txtblu=$(tput setaf 4) # Blue
txtpur=$(tput setaf 5) # Purple
txtcyn=$(tput setaf 6) # Cyan
txtwht=$(tput setaf 7) # White
txtrst=$(tput sgr0) # Text reset

_DEBUG="on"

function EXECUTE() {
    [ "$_DEBUG" == "on" ] && echo $@ || $@
}

function title() {
    tput rev 
    showHeader $@
    tput sgr0
}

function showHeader() {
    input=$@
    echo ${txtgrn}
    printf "%0.s-" $(seq 1 ${#input})
    printf "\n"
    echo $input
    printf "%0.s-" $(seq 1 ${#input})
    echo ${txtrst}  
}

function showSectionTitle() {
    echo 
    echo ---  ${txtblu} $@ ${txtrst}  
    echo 
}

#-------------------------------------------
# Introduction
#-------------------------------------------
title "DEPLOYING THE FRONT-END FOR THE SERVERLESS WEBFORM SAMPLE APP"
## Fixing Cognito is required only for the workshop
#showHeader Fixing Cognito
#source fixcognito.sh
#-------------------------------------------
# Retrieving parameters from CloudFormation
#-------------------------------------------
url=$(eval $(echo "aws cloudformation list-exports --query 'Exports[?contains(Name,\`WebformCloudfrontDomain\`)].Value | [0]' | xargs -I {} echo {}"))
bucket=$(eval $(echo "aws cloudformation list-exports --query 'Exports[?contains(Name,\`WebformS3Bucket\`)].Value | [0]' | xargs -I {} echo {}"))
#-------------------------------------------
# DEPLOYING THE WEBSITE ON S3
#-------------------------------------------
showHeader "DEPLOYING THE WEBSITE ON S3"
aws s3 cp frontend/index.html s3://$bucket
#-------------------------------------------
# Finalization
#-------------------------------------------
title "Serverless Webform Sample App deployed"
echo "URL: https://$url"