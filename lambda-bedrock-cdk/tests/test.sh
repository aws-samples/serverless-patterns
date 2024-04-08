#!/bin/bash
#Get aguments
while getopts ":f:m:e:" opt; do
  case $opt in
    f) fn="$OPTARG"
    ;;
    m) model="$OPTARG"
    ;;
    e) event="$OPTARG"
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
    exit 1
    ;;
  esac

  case $OPTARG in
    -*) echo "Option $opt needs a valid argument"
    exit 1
    ;;
  esac
done


#Provide function name after CDK deployment:
echo "Deleting previous test result..."
rm $model-response$event.json
echo "Executing $fn with event $event"
aws lambda invoke --function-name $fn --cli-binary-format raw-in-base64-out --payload file://events/$model/event$event.json --output json $model-response$event.json &