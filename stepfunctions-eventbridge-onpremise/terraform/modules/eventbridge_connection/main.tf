resource "aws_security_group" "resource_gateway_sg" {
  name_prefix = "resource-gateway-sg"
  description = "Security group for resource gateway"
  vpc_id      = var.vpc_id

  egress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = [var.on_premises_cidr]
    description = "Allow HTTPS traffic to on-premises"
  }

  egress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = [var.on_premises_cidr]
    description = "Allow HTTP traffic to on-premises"
  }
}

resource "aws_vpclattice_resource_gateway" "on_premise_resource_gateway" {
  name                = "resource-gateway"
  ip_address_type     = "IPV4"
  vpc_id              = var.vpc_id
  security_group_ids  = [aws_security_group.resource_gateway_sg.id]
  subnet_ids          = var.private_subnet_ids
}

resource "aws_vpclattice_resource_configuration" "on_premise_resource_configuration" {
  name                          = "resource-config"
  port_ranges                   = ["80", "443"]
  protocol                      = "TCP"
  resource_gateway_identifier   = aws_vpclattice_resource_gateway.on_premise_resource_gateway.id
  type                          = "SINGLE"

  resource_configuration_definition {
    # uncomment if using ip address
    # ip_resource {
    #   ip_address = var.api_ip_address
    # }

    # remove if using ip address
    dns_resource {
      domain_name      = var.api_domain_name
      ip_address_type  = "IPV4"
    }
  }
}

data "aws_secretsmanager_secret_version" "api_key" {
  secret_id = var.api_key_secret_arn
}

resource "aws_cloudwatch_event_connection" "on_premise_connection" {
  name               = "on-premise-connection"
  description        = "Connection to on premises API"
  authorization_type = "API_KEY"

  auth_parameters {
    # configure basic or oauth instead of api_key, depending on your authentication method
    api_key {
      key   = "x-api-key"
      value = data.aws_secretsmanager_secret_version.api_key.secret_string
    }
    # eventually add http parameters (header, body or query string) to the connection
    invocation_http_parameters {
      header {
        key = "x-origin"
        value = "aws-state-machine"
      }
    }
  }

  invocation_connectivity_parameters {
    resource_parameters {
      resource_configuration_arn = aws_vpclattice_resource_configuration.on_premise_resource_configuration.arn
    }
  }
}
