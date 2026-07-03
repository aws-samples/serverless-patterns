# Optional production-oriented network profile: a VPC with a private subnet whose
# egress is constrained (no internet gateway on the private subnet) and optional
# VPC Flow Logs to CloudWatch for network-flow evidence. Enable with
# enable_vpc_egress = true. This is a reference for routing MicroVM egress through
# a controlled VPC connector rather than AWS-managed INTERNET_EGRESS.

resource "aws_vpc" "egress" {
  count                = var.enable_vpc_egress ? 1 : 0
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags                 = merge(local.common_tags, { Name = "${var.project_name}-egress" })
}

resource "aws_subnet" "private" {
  count             = var.enable_vpc_egress ? 1 : 0
  vpc_id            = aws_vpc.egress[0].id
  cidr_block        = cidrsubnet(var.vpc_cidr, 8, 1)
  availability_zone = data.aws_availability_zones.available[0].names[0]
  tags              = merge(local.common_tags, { Name = "${var.project_name}-private" })
}

data "aws_availability_zones" "available" {
  count = var.enable_vpc_egress ? 1 : 0
  state = "available"
}

# Restrictive security group: no inbound; egress only to HTTPS by default. Tighten
# the cidr_blocks / add a prefix list to reach only an allowlisted canary endpoint.
resource "aws_security_group" "egress" {
  count       = var.enable_vpc_egress ? 1 : 0
  name        = "${var.project_name}-egress"
  description = "Restricted egress for MicroVM analysis traffic"
  vpc_id      = aws_vpc.egress[0].id

  egress {
    description = "HTTPS egress (replace 0.0.0.0/0 with an allowlisted canary CIDR/prefix list)"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(local.common_tags, { Name = "${var.project_name}-egress" })
}

# --- Optional VPC Flow Logs to CloudWatch (network-flow metadata evidence) ---
resource "aws_cloudwatch_log_group" "flow_logs" {
  count             = var.enable_vpc_egress && var.enable_vpc_flow_logs ? 1 : 0
  name              = "/${var.project_name}/vpc-flow-logs"
  retention_in_days = 14
  tags              = local.common_tags
}

data "aws_iam_policy_document" "flow_logs_trust" {
  count = var.enable_vpc_egress && var.enable_vpc_flow_logs ? 1 : 0
  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["vpc-flow-logs.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "flow_logs" {
  count              = var.enable_vpc_egress && var.enable_vpc_flow_logs ? 1 : 0
  name               = "${var.project_name}-flow-logs-role"
  assume_role_policy = data.aws_iam_policy_document.flow_logs_trust[0].json
  tags               = local.common_tags
}

data "aws_iam_policy_document" "flow_logs" {
  count = var.enable_vpc_egress && var.enable_vpc_flow_logs ? 1 : 0
  statement {
    effect = "Allow"
    actions = [
      "logs:CreateLogStream",
      "logs:PutLogEvents",
      "logs:DescribeLogGroups",
      "logs:DescribeLogStreams",
    ]
    resources = ["${aws_cloudwatch_log_group.flow_logs[0].arn}:*"]
  }
}

resource "aws_iam_role_policy" "flow_logs" {
  count  = var.enable_vpc_egress && var.enable_vpc_flow_logs ? 1 : 0
  name   = "flow-logs-policy"
  role   = aws_iam_role.flow_logs[0].id
  policy = data.aws_iam_policy_document.flow_logs[0].json
}

resource "aws_flow_log" "vpc" {
  count                    = var.enable_vpc_egress && var.enable_vpc_flow_logs ? 1 : 0
  iam_role_arn             = aws_iam_role.flow_logs[0].arn
  log_destination          = aws_cloudwatch_log_group.flow_logs[0].arn
  traffic_type             = "ALL"
  vpc_id                   = aws_vpc.egress[0].id
  max_aggregation_interval = 60
  tags                     = local.common_tags
}
