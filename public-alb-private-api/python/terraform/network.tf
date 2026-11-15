# Creates VPCs
resource "aws_vpc" "vpc" {
  cidr_block = "20.0.0.0/16"
  enable_dns_hostnames = "true" 
}

#Creates subnets
resource "aws_subnet" "private_subnet" {
  vpc_id = aws_vpc.vpc.id
  cidr_block = "20.0.0.0/24"
  availability_zone = "${var.region}a"
  tags = {
    Name = "Subnet for ${var.region}a"
  }
}

resource "aws_subnet" "public_subnet" {
  cidr_block = "20.0.1.0/24"
  vpc_id = aws_vpc.vpc.id
  availability_zone = "${var.region}a"
  tags = {
    Name = "Subnet for ${var.region}a"
  }
}

resource "aws_subnet" "public_subnet2" {
  cidr_block = "20.0.2.0/24"
  vpc_id = aws_vpc.vpc.id
  availability_zone = "${var.region}c"
  tags = {
    Name = "Subnet for ${var.region}c"
  }
}

#Creates IGW 
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.vpc.id

  tags = {
    Name = "igw"
  }
}

#Creates RouteTables
resource "aws_route_table" "private_rt" {
  vpc_id = aws_vpc.vpc.id

  tags = {
    Name = "private_rt"
  }
}

resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "public_rt"
  }
}

resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.private_subnet.id
  route_table_id = aws_route_table.private_rt.id
}

resource "aws_route_table_association" "b" {
  subnet_id      = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_route_table_association" "c" {
  subnet_id      = aws_subnet.public_subnet2.id
  route_table_id = aws_route_table.public_rt.id
}


#Creates SecurityGroup
resource "aws_security_group" "allow_https" {
  name        = "allow_https"
  description = "Allow HTTPS inbound traffic"
  vpc_id      = aws_vpc.vpc.id

  ingress {
    description      = "HTTPS from VPC"
    from_port        = 443
    to_port          = 443
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "allow_https"
  }
}

#Create VPC endpoints

resource "aws_vpc_endpoint" "execute_api" {
  vpc_id            = aws_vpc.vpc.id
  service_name      = "com.amazonaws.${var.region}.execute-api"
  vpc_endpoint_type = "Interface"

  security_group_ids = [
    aws_security_group.allow_https.id,
  ]
  
  subnet_ids        = [aws_subnet.private_subnet.id]
  private_dns_enabled = true
}

data "aws_network_interface" "nic1" {
  id = tolist(aws_vpc_endpoint.execute_api.network_interface_ids)[0]
}

#data "aws_network_interface" "nic2" {
#  id = tolist(aws_vpc_endpoint.execute_api.network_interface_ids)[1]
#}

#for_each = aws_vpc_endpoint.execute_api.network_interface_ids
#  id = each.value