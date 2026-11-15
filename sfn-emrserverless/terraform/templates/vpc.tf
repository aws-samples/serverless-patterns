resource "aws_vpc" "emr_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "${var.app}-${var.stage_name}-VPC"
    Environment = var.stage_name
    Application = var.app
  }
}

resource "aws_subnet" "emr_public_subnet1" {
  vpc_id     = aws_vpc.emr_vpc.id
  cidr_block = "10.0.0.0/24"

  tags = {
    Name = "${var.app}-${var.stage_name}-public-subnet1"
    Environment = var.stage_name
    Application = var.app
  }
}

resource "aws_subnet" "emr_private_subnet1" {
  vpc_id     = aws_vpc.emr_vpc.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "${var.app}-${var.stage_name}-private-subnet1"
    Environment = var.stage_name
    Application = var.app
  }
}

resource "aws_internet_gateway" "emr_igw" {
  vpc_id = aws_vpc.emr_vpc.id
    tags = {
    Name = "${var.app}-${var.stage_name}-igw"
    Environment = var.stage_name
    Application = var.app
  }
}

resource "aws_route_table" "emr_route_table" {
  vpc_id = aws_vpc.emr_vpc.id
    tags = {
    Name = "${var.app}-${var.stage_name}-route-tbl"
    Environment = var.stage_name
    Application = var.app
  }
}

resource "aws_route" "emr_public_route" {
  route_table_id         = aws_route_table.emr_route_table.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.emr_igw.id
}

resource "aws_route_table_association" "emr_route_table_association1" {
  subnet_id      = aws_subnet.emr_public_subnet1.id
  route_table_id = aws_route_table.emr_route_table.id
}

resource "aws_eip" "emr_ip" {
  domain = "vpc"

  tags = {
    Name = "${var.app}-${var.stage_name}-elastic-ip"
    Environment = var.stage_name
    Application = var.app
  }
}

resource "aws_nat_gateway" "emr_ngw" {
  allocation_id = aws_eip.emr_ip.id
  subnet_id     = aws_subnet.emr_public_subnet1.id

  tags = {
    Name = "${var.app}-${var.stage_name}-nat-gw"
    Environment = var.stage_name
    Application = var.app
  }
}

resource "aws_route_table" "emr_ngw_route_table" {
  vpc_id = aws_vpc.emr_vpc.id
}

resource "aws_route" "emr_ngw_route" {
  route_table_id         = aws_route_table.emr_ngw_route_table.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_nat_gateway.emr_ngw.id
}

resource "aws_route_table_association" "emr_ngw_route_table_association1" {
  subnet_id      = aws_subnet.emr_private_subnet1.id
  route_table_id = aws_route_table.emr_ngw_route_table.id
}

resource "aws_route_table" "emr_vpce_route_table" {
  vpc_id = aws_vpc.emr_vpc.id
}

resource "aws_route" "emr_vpce_route" {
  route_table_id         = aws_route_table.emr_vpce_route_table.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_nat_gateway.emr_ngw.id
}

resource "aws_security_group" "emr_security_group" {
  name        = "${var.app}-${var.stage_name}-sg"
  description = "Allowed Ports"
  vpc_id      = aws_vpc.emr_vpc.id
    tags = {
    Name = "${var.app}-${var.stage_name}-sg"
    Environment = var.stage_name
    Application = var.app
  }
}

resource "aws_security_group_rule" "emr_security_group_rule" {
  type              = "egress"
  protocol          = "-1"
  from_port         = 0
  to_port           = 0
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.emr_security_group.id
}
