#!/bin/bash

JOB_STATUS=$(aws glue get-job-runs --job-name ${1} --query 'JobRuns[0].JobRunState' --output text)

if [[ ${JOB_STATUS} != "RUNNING" && ${JOB_STATUS} != "STARTING" ]]; then
  echo "Running the Glue Job..."
  aws glue start-job-run --job-name ${1} \
  --arguments='--enable-metrics=true,--enable-job-insights=true,--enable-continuous-cloudwatch-log=true,--enable-auto-scaling=true'
else
  echo "The Glue job is either running or starting."
fi