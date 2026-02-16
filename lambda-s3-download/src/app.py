import requests
import boto3
import json
import os
from pathlib import Path


def lambda_handler(event, context):

    target_bucket = event.get("target_bucket", os.environ["TARGET_BUCKET"])
    target_bucket_region = event.get("target_bucket_region", os.environ.get("AWS_REGION"))
    
    download_url = event["download_url"]
    download_filename = event["download_filename"]

    # Cap chunk size under 5 GB to be inside S3 max part size and not exhaust max Lambda memory
    # Floor chunk size at 5 MB to fit the S3 minimum part size
    chunk_size_mb = min(max(int(event.get("chunk_size_mb", 128)), 5), 5120)

    # open a multipart s3 upload request.
    s3 = boto3.client("s3", region_name = target_bucket_region)
    upload_request = s3.create_multipart_upload(Bucket=target_bucket, Key=download_filename, ChecksumAlgorithm="SHA256")
    upload_id = upload_request["UploadId"]
    part_number = 0
    parts = []
    
    try:
        with requests.get(download_url, stream=True) as download_request:

            for chunk in download_request.iter_content(chunk_size=chunk_size_mb*1024*1024):
                part_number = part_number + 1
                download_target = Path("/tmp", download_filename + "_" + str(part_number))
                
                with download_target.open('wb') as download_file:
                    download_file.write(chunk)
                    download_file.close()

                with download_target.open('rb') as download_file:
                    part_upload = s3.upload_part(Body=download_file, Bucket=target_bucket, Key=download_filename, PartNumber=part_number, UploadId=upload_id, ChecksumAlgorithm="SHA256")
                    parts.append({'ETag': part_upload['ETag'], 'ChecksumSHA256': part_upload['ChecksumSHA256'], 'PartNumber': part_number})
                    download_file.close()

                download_target.unlink()

        s3.complete_multipart_upload(Bucket=target_bucket, Key=download_filename, MultipartUpload={'Parts': parts}, UploadId=upload_id)
        objectSummary = s3.get_object_attributes(Bucket=target_bucket,Key=download_filename, ObjectAttributes=['Checksum'])

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"{download_filename} uploaded successfully",
                "bucket": target_bucket,
                "key": download_filename,
                "checksum_sha256": objectSummary["Checksum"]["ChecksumSHA256"],
                "parts": len(parts)
            })
        }

    except Exception as e:
        s3.abort_multipart_upload(Bucket=target_bucket, Key=download_filename, UploadId=upload_id)
        return {
            "statusCode": 500,
            "body": json.dumps({"message": f"Download/Upload failed: {str(e)}"})
        }


