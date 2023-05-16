
#1. VPC with subnet

resource "aws_vpc" "main" {
  cidr_block = "11.0.0.0/16"
  tags = {
    Name = "main_vpc"
  }
}

resource "aws_subnet" "pub_subnet_1" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = cidrsubnet(aws_vpc.main.cidr_block, 4, 1)
  
  availability_zone       = "us-west-2a"
  map_public_ip_on_launch = "true"
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "demo_igw"
  }
}

resource "aws_route" "internetgatewayroute" {
  depends_on                = [aws_internet_gateway.igw]

  route_table_id            = aws_route_table.pub_route_table.id
  destination_cidr_block    = "0.0.0.0/0"
  gateway_id                = aws_internet_gateway.igw.id
}

resource "aws_route_table" "pub_route_table" {
  vpc_id = aws_vpc.main.id
}

resource "aws_route_table_association" "pubsubnetroutetableassociation1" {
  subnet_id      = aws_subnet.pub_subnet_1.id
  route_table_id = aws_route_table.pub_route_table.id
}

resource "aws_default_security_group" "default" {
  vpc_id = aws_vpc.main.id
}

resource "aws_security_group" "allow_http" {
  name        = "allow_http"
  description = "Allow http inbound traffic"
  vpc_id      = aws_vpc.main.id

  ingress {
    description      = "TLS from VPC"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = [aws_vpc.main.cidr_block]
  }

  egress {
    description      = "Outbound"
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }
}

#2. Cloud map, public

resource "aws_service_discovery_public_dns_namespace" "cloud_map_dns" {
  name        = "serverless.terraform.com"
  description = "cloud map"
  }

resource "aws_service_discovery_service" "cloud_map_service" {
  name = "cloudmapservice"

  dns_config {
    namespace_id = aws_service_discovery_public_dns_namespace.cloud_map_dns.id

    dns_records {
      ttl  = 10
      type = "A"
    }
  }
  namespace_id = aws_service_discovery_public_dns_namespace.cloud_map_dns.id
}

#3. Cluster:

resource "aws_ecs_cluster" "demo_cluster" {
  name = "demo_ecs_cluster"

  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}

#4. Capacity Provider

resource "aws_ecs_cluster_capacity_providers" "example" {
  cluster_name = aws_ecs_cluster.demo_cluster.name

  capacity_providers = ["FARGATE"]

  default_capacity_provider_strategy {
    base              = 1
    weight            = 100
    capacity_provider = "FARGATE"
  }
}

#5. Task Definition:

resource "aws_ecs_task_definition" "task_registration" {
  family                   = "task_definition_demo"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = ".5vCPU"
  memory = "1024"
  container_definitions    = jsonencode([
  {
    "name": "dotnet",
    "image": "httpd:2.4",
    "portMappings" = [
        {
          "containerPort" = 80
          "hostPort"      = 80
        }
    ],
    "essential": true,
  }
])
  runtime_platform {
    operating_system_family = "LINUX"
    cpu_architecture        = "ARM64"
  }
}

#6. ECS Service

resource "aws_ecs_service" "demo_service" {
  name               = "demo-fargate-service"
  cluster            = aws_ecs_cluster.demo_cluster.name 
  task_definition    = aws_ecs_task_definition.task_registration.arn
  desired_count   = 2
  deployment_maximum_percent          = 200
  deployment_minimum_healthy_percent  = 100
  enable_ecs_managed_tags = "true"
  launch_type = "FARGATE"
  network_configuration {
    subnets           = [aws_subnet.pub_subnet_1.id]
    security_groups   = [aws_security_group.allow_http.id]
    assign_public_ip  = "true"
  }
service_registries {
    registry_arn  = aws_service_discovery_service.cloud_map_service.arn
  }
}
