# Network-ALB.tf

#################################################################
# Network - AWS Application Load Balancer
#################################################################
# Creating the internal AWS Application Load Balancer on private subnets 
resource "aws_alb" "MyApp-ALB" {
    name            = "MyApp-ALB"
    internal        = true
    subnets         = [aws_subnet.MySubnet-privateA.id, aws_subnet.MySubnet-privateB.id]
    security_groups = [aws_security_group.MyApp-ALB_SG.id]
}

# Defining ALB target group with health check of 5 seconds timeout
resource "aws_alb_target_group" "MyApp-ALB_TG" {
    name            = "MyApp-ALB-TG"
    port            = 80
    protocol        = "HTTP"
    vpc_id          = aws_vpc.MyVPC-VPC.id
    target_type     = "ip"

    health_check {
        healthy_threshold   = "3"
        interval            = "30"
        protocol            = "HTTP"
        matcher             = "200"
        timeout             = "5"
        path                = "/"
        unhealthy_threshold = "2"
    }
}

# Setting up internal ALB security group allowing only traffic from 80 TCP port
resource "aws_security_group" "MyApp-ALB_SG" {
    name            = "MyApp-ALB-SG"
    vpc_id          = aws_vpc.MyVPC-VPC.id

    ingress {
        protocol    = "tcp"
        from_port   = 80
        to_port     = 80
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        protocol    = "-1"
        from_port   = 0
        to_port     = 0
        cidr_blocks = ["0.0.0.0/0"]
    }
}

# Redirecting all traffic from the ALB to the ECS Cluster target group
resource "aws_alb_listener" "MyApp-ALB_Listener" {
  load_balancer_arn = aws_alb.MyApp-ALB.id
  port              = 80
  protocol          = "HTTP"

  default_action {
    target_group_arn = aws_alb_target_group.MyApp-ALB_TG.id
    type             = "forward"
  }
}
