# Network-ALB.tf

#################################################################
# Network - Virtual Private Cloud (VPC)
#################################################################
# Creating the VPC with "10.0.0.0/16" CIDR range with feched data info
resource "aws_vpc" "MyVPC-VPC" {
    cidr_block = "10.0.0.0/16"
    
    enable_dns_hostnames = true
    enable_dns_support = true
    
    tags = {
        Name = "MyVPC-VPC"
    }
}

# Creating 2 private subnets in each different AZ
resource "aws_subnet" "MySubnet-privateA" {
    cidr_block        = cidrsubnet(aws_vpc.MyVPC-VPC.cidr_block, 8, 1)
    availability_zone = data.aws_availability_zones.available.names[1]
    vpc_id            = aws_vpc.MyVPC-VPC.id
    
    tags = {
        Name = "MySubnet-privateA"
    }
}

resource "aws_subnet" "MySubnet-privateB" {
    cidr_block        = cidrsubnet(aws_vpc.MyVPC-VPC.cidr_block, 8, 2)
    availability_zone = data.aws_availability_zones.available.names[2]
    vpc_id            = aws_vpc.MyVPC-VPC.id
    
    tags = {
        Name = "MySubnet-privateB"
    }
}

# Creating 2 public subnets in each different AZ
resource "aws_subnet" "MySubnet-publicA" {
    cidr_block              = cidrsubnet(aws_vpc.MyVPC-VPC.cidr_block, 8, 3)
    availability_zone       = data.aws_availability_zones.available.names[1]
    vpc_id                  = aws_vpc.MyVPC-VPC.id
    map_public_ip_on_launch = true
    
    tags = {
        Name = "MySubnet-publicA"
    }
}

resource "aws_subnet" "MySubnet-publicB" {
    cidr_block              = cidrsubnet(aws_vpc.MyVPC-VPC.cidr_block, 8, 4)
    availability_zone       = data.aws_availability_zones.available.names[2]
    vpc_id                  = aws_vpc.MyVPC-VPC.id
    map_public_ip_on_launch = true
    
    tags = {
        Name = "MySubnet-publicB"
    }
}

# Internet Gateway for the public subnet
resource "aws_internet_gateway" "MyIGW-IG" {
    vpc_id = aws_vpc.MyVPC-VPC.id
    
    tags = {
        Name = "MyIGW-IG"
    }

}

# Routing the public subnet traffic through the IGW
resource "aws_route" "internet_access" {
    route_table_id         = aws_vpc.MyVPC-VPC.main_route_table_id
    destination_cidr_block = "0.0.0.0/0"
    gateway_id             = aws_internet_gateway.MyIGW-IG.id
}

# Creating one NAT Gateway in each AZ with an Elastic IP for each private subnet to get internet connectivity
resource "aws_eip" "MyEIP-EIPA" {
    depends_on = [aws_internet_gateway.MyIGW-IG]
    
    tags = {
        Name = "MyEIP-EIPA"
    }
}

resource "aws_eip" "MyEIP-EIPB" {
    depends_on = [aws_internet_gateway.MyIGW-IG]
    
    tags = {
        Name = "MyEIP-EIPB"
    }
}

resource "aws_nat_gateway" "MyNATGW-NATGWA" {
    subnet_id     = element(aws_subnet.MySubnet-publicA.*.id, 1)
    allocation_id = element(aws_eip.MyEIP-EIPA.*.id, 1)
    
    tags = {
        Name = "MyNATGW-NATGWA"
    }
}

resource "aws_nat_gateway" "MyNATGW-NATGWB" {
    subnet_id     = element(aws_subnet.MySubnet-publicB.*.id, 2)
    allocation_id = element(aws_eip.MyEIP-EIPB.*.id, 2)
    
    tags = {
        Name = "MyNATGW-NATGWB"
    }
    
}

# Routing public subnets, making non-local traffic pass through Internet Gateway to the internet
resource "aws_route_table" "MyRouteTable-publicA" {
    vpc_id = aws_vpc.MyVPC-VPC.id
    
    route {
        cidr_block     = "0.0.0.0/0"
        gateway_id     = aws_internet_gateway.MyIGW-IG.id
    }
    
    tags = {
        Name = "MyRouteTable-publicA"
    }
}

resource "aws_route_table" "MyRouteTable-publicB" {
    vpc_id = aws_vpc.MyVPC-VPC.id
    
    route {
        cidr_block     = "0.0.0.0/0"
        gateway_id     = aws_internet_gateway.MyIGW-IG.id
    }
    
    tags = {
        Name = "MyRouteTable-publicB"
    }
}

# Routing private subnets, making non-local traffic pass through each NAT gateway to the internet
resource "aws_route_table" "MyRouteTable-privateA" {
    vpc_id = aws_vpc.MyVPC-VPC.id

    route {
        cidr_block     = "0.0.0.0/0"
        nat_gateway_id = element(aws_nat_gateway.MyNATGW-NATGWA.*.id, 1)
    }
    
    tags = {
        Name = "MyRouteTable-privateA"
    }

}

resource "aws_route_table" "MyRouteTable-privateB" {
    vpc_id = aws_vpc.MyVPC-VPC.id

    route {
        cidr_block     = "0.0.0.0/0"
        nat_gateway_id = element(aws_nat_gateway.MyNATGW-NATGWB.*.id, 2)
    }
    
    tags = {
        Name = "MyRouteTable-privateB"
    }
}

# Associating the previously created routes to the public and private subnets (so they don't default to the main MyVPC-VPC route table)
resource "aws_route_table_association" "privateA" {
    subnet_id      = element(aws_subnet.MySubnet-privateA.*.id, 1)
    route_table_id = element(aws_route_table.MyRouteTable-privateA.*.id, 1)
}

resource "aws_route_table_association" "privateB" {
    subnet_id      = element(aws_subnet.MySubnet-privateB.*.id, 2)
    route_table_id = element(aws_route_table.MyRouteTable-privateB.*.id, 2)
}

resource "aws_route_table_association" "publicA" {
    subnet_id      = element(aws_subnet.MySubnet-publicA.*.id, 1)
    route_table_id = element(aws_route_table.MyRouteTable-publicA.*.id, 1)
}

resource "aws_route_table_association" "publicB" {
    subnet_id      = element(aws_subnet.MySubnet-publicB.*.id, 2)
    route_table_id = element(aws_route_table.MyRouteTable-publicB.*.id, 2)
}
