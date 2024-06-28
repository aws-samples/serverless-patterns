output "dns_record_for_application" {
  description = "DNS Address to Access the Application"
  value       = "http://${aws_alb.this_aws_alb_front_end.dns_name}:8080"
}