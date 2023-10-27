# Output value definitions

output "alb_url" {
  value = "http://${aws_lb.load_balancer.dns_name}"
}

