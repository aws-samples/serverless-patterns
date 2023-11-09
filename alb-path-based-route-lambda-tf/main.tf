
# Create AWS VPC 
resource "aws_vpc" "vpc" {
  cidr_block = var.vpc_cidr

}

# Create public subnet 1
resource "aws_subnet" "public_subnet1" {
  cidr_block = "10.0.1.0/24"
  vpc_id = aws_vpc.vpc.id
  availability_zone = "${var.region}a"
  tags = {
    Name = "Subnet for ${var.region}a"
  }
}

# Create public subnet 2
resource "aws_subnet" "public_subnet2" {
  cidr_block = "10.0.2.0/24"
  vpc_id = aws_vpc.vpc.id
  availability_zone = "${var.region}b"
  tags = {
    Name = "Subnet for ${var.region}b"
  }
}

# Create a route table 
resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }

  tags = {
    Name = "public_rt"
  }
}

# Associate the route table with public subnet 1
resource "aws_route_table_association" "public_rt_table_a" {
  subnet_id      = aws_subnet.public_subnet1.id
  route_table_id = aws_route_table.public_rt.id
}

# Associate the route table with public subnet 2
resource "aws_route_table_association" "public_rt_table_b" {
  subnet_id      = aws_subnet.public_subnet2.id
  route_table_id = aws_route_table.public_rt.id
}

# Create an Internet Gateway
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.vpc.id
  tags = {
    "Name" = "example-igw"
  }
}

# Create IAM Role for Lambda Function
resource "aws_iam_role" "lambda_role" {
name   = "Lambda_Function_Role"
assume_role_policy = <<EOF
{
 "Version": "2012-10-17",
 "Statement": [
   {
     "Action": "sts:AssumeRole",
     "Principal": {
       "Service": "lambda.amazonaws.com"
     },
     "Effect": "Allow",
     "Sid": ""
   }
 ]
}
EOF
}

# Create IAM policy for Lambda to write logs
resource "aws_iam_policy" "iam_policy_for_lambda" {
 
 name         = "aws_iam_policy_for_terraform_aws_lambda_role"
 path         = "/"
 description  = "AWS IAM Policy for managing aws lambda role"
 policy = <<EOF
{
 "Version": "2012-10-17",
 "Statement": [
   {
     "Action": [
       "logs:CreateLogGroup",
       "logs:CreateLogStream",
       "logs:PutLogEvents"
     ],
     "Resource": "arn:aws:logs:*:*:*",
     "Effect": "Allow"
   }
 ]
}
EOF
}
 
# Attach the IAM policy for writing logs to the Lambda Role
resource "aws_iam_role_policy_attachment" "attach_iam_policy_to_iam_role" {
 role        = aws_iam_role.lambda_role.name
 policy_arn  = aws_iam_policy.iam_policy_for_lambda.arn
}

# Create a security group for application load balancer
resource "aws_security_group" "load_balancer_sg" {
  name        = "myLoadBalancerSG"
  vpc_id      = aws_vpc.vpc.id
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "myLoadBalancerSG"
  }
}

# Create the application load balancer
resource "aws_lb" "load_balancer" {
  name               = "myLoadBalancer"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.load_balancer_sg.id]
  subnets            = [aws_subnet.public_subnet1.id,aws_subnet.public_subnet2.id]
  tags = {
    Name = "myLoadBalancer"
  }
}

# Create target groups for different services
resource "aws_lb_target_group" "service1" {
  name        = "service1-target-group"
  target_type = "lambda"
  vpc_id   = aws_vpc.vpc.id
}

resource "aws_lb_target_group" "service2" {
  name        = "service2-target-group"
  target_type = "lambda"
  vpc_id   = aws_vpc.vpc.id
}

resource "aws_alb_target_group_attachment" "service1_attachment" {
  depends_on       = [aws_lb.load_balancer]
  target_group_arn = aws_lb_target_group.service1.arn
  target_id        = aws_lambda_function.lambda_function1.arn
}

resource "aws_alb_target_group_attachment" "service2_attachment" {
  depends_on       = [aws_lb.load_balancer]
  target_group_arn = aws_lb_target_group.service2.arn
  target_id        = aws_lambda_function.lambda_function2.arn
}

# Define ALB listeners and path-based routing
resource "aws_lb_listener" "http" {
  load_balancer_arn = aws_lb.load_balancer.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type = "fixed-response"
    fixed_response {
      content_type = "text/plain"
      status_code  = "200"
      message_body = "Default Response from ALB"
    }
  }
}
# Define path-based routing rules
resource "aws_lb_listener_rule" "example_rule1" {
  listener_arn = aws_lb_listener.http.arn
  priority     = 100
  action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.service1.arn
  }
  condition {
    path_pattern {
      values = ["/api/service1*"]
    }
  }

}
resource "aws_lb_listener_rule" "example_rule2" {
  listener_arn = aws_lb_listener.http.arn
  priority     = 101
  action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.service2.arn
  }
  condition {
    path_pattern {
      values = ["/api/service2*"]
    }
  }
}

# Create the Lambda Function
resource "aws_lambda_function" "lambda_function1" {
  function_name = "lambdaFunction-service1"
  runtime       = "nodejs14.x"
  handler       = "index.handler"
  filename      = "Lambda1.zip"
  role          = aws_iam_role.lambda_role.arn
  depends_on    = [aws_iam_role_policy_attachment.attach_iam_policy_to_iam_role]
  tags = {
    Name = "lambdaFunction"
  }
}

# Create the Lambda Function
resource "aws_lambda_function" "lambda_function2" {
  function_name = "lambdaFunction-service2"
  runtime       = "nodejs14.x"
  handler       = "index.handler"
  filename      = "Lambda2.zip"
  role          = aws_iam_role.lambda_role.arn
  depends_on    = [aws_iam_role_policy_attachment.attach_iam_policy_to_iam_role]
  tags = {
    Name = "lambdaFunction"
  }
}

# Allow the application load balancer to access Lambda Function
resource "aws_lambda_permission" "with_lb_function1" {
  statement_id  = "AllowExecutionFromlb"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_function1.arn
  principal     = "elasticloadbalancing.amazonaws.com"
  source_arn    = aws_lb_target_group.service1.arn
}

# Allow the application load balancer to access Lambda Function
resource "aws_lambda_permission" "with_lb_function2" {
  statement_id  = "AllowExecutionFromlb"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda_function2.arn
  principal     = "elasticloadbalancing.amazonaws.com"
  source_arn    = aws_lb_target_group.service2.arn
}