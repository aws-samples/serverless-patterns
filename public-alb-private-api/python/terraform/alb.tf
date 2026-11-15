#Create ALB
resource "aws_lb" "public_alb" {
  name               = "public-alb-test"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.allow_https.id]
  subnets            = [aws_subnet.public_subnet.id,aws_subnet.public_subnet2.id]
}

#Create target group
resource "aws_lb_target_group" "test" {
  name     = "tf-example-lb-tg"
  port     = 443
  protocol = "HTTPS"
  target_type = "ip"
  vpc_id   = aws_vpc.vpc.id
  
  health_check {
    matcher     = "200,403"
    port        = 443    
  }
}

#Add target to target group
resource "aws_lb_target_group_attachment" "nic01" {
  target_group_arn = aws_lb_target_group.test.arn
  target_id        = data.aws_network_interface.nic1.private_ip
  port             = 443
}

#Create listener
resource "aws_lb_listener" "front_end" {
  load_balancer_arn = aws_lb.public_alb.arn
  port              = "443"
  protocol          = "HTTPS"
  ssl_policy        = "ELBSecurityPolicy-2016-08"
  certificate_arn   = aws_acm_certificate.cert.arn

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.test.arn
  }
}

output "final_url" {
    value = "https://${var.custom_domain_name_prefix}.${var.domain_name}/${aws_api_gateway_stage.dev.stage_name} -H 'Host:${aws_api_gateway_rest_api.private_api.id}.execute-api.${var.region}.amazonaws.com'"
}