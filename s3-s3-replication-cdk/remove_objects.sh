#!/bin/sh

buckets="my-source-bucket my-destination-bucket-1 my-destination-bucket-2"

for bucket_name in $buckets
do
    echo ${bucket_name}
    aws s3api delete-objects --bucket ${bucket_name} --delete "$(aws s3api list-object-versions --bucket ${bucket_name} --output=json --query='{Objects: Versions[].{Key:Key,VersionId:VersionId}}')" > output.log
    aws s3api delete-objects --bucket ${bucket_name} --delete "$(aws s3api list-object-versions --bucket ${bucket_name} --output=json --query='{Objects: DeleteMarkers[].{Key:Key,VersionId:VersionId}}')" > output.log
done
