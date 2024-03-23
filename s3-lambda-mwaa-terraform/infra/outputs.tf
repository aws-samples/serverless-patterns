output "input_bucket_id" {
  description = "Name of the input bucket"
  value       = module.input_bucket.s3_bucket_id
}

output "mwaa_webserver_url" {
  description = "The webserver URL of the MWAA Environment"
  value       = module.mwaa.mwaa_webserver_url
}