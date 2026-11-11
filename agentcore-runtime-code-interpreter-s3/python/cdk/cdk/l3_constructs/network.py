from aws_cdk import aws_ec2 as ec2
from constructs import Construct

MIN_AVAILABILITY_ZONES = 2


class Network(Construct):
    """Amazon VPC with isolated private subnets: no internet gateway and no NAT gateway,
    so code running in Code Interpreter sessions can reach only resources inside the VPC, plus
    the Amazon S3 gateway endpoint that the CodeInterpreter construct adds. See
    https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-vpc.html#agentcore-internet-access

    AgentCore supports VPC connectivity only in some Availability Zones, which it lists by
    zone ID: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-vpc.html#agentcore-supported-azs
    Pass those IDs in `availability_zone_ids`, separated by commas (for example
    "usw2-az1,usw2-az2"), to create one subnet in each. Without them, an
    environment-agnostic stack like this one gets the first two Availability Zones that AWS
    CloudFormation returns for the Region (see maxAzs in
    https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_ec2/Vpc.html).
    """

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        availability_zone_ids: str | None = None,
    ) -> None:
        super().__init__(scope, construct_id)

        zone_ids = [zone_id.strip() for zone_id in (availability_zone_ids or "").split(",") if zone_id.strip()]
        if zone_ids:
            if len(zone_ids) < MIN_AVAILABILITY_ZONES:
                raise ValueError(f"Pass at least {MIN_AVAILABILITY_ZONES} Availability Zone IDs, got {zone_ids}.")
            if len(set(zone_ids)) != len(zone_ids):
                raise ValueError(f"Availability Zone IDs must be unique, got {zone_ids}.")

        self.vpc = ec2.Vpc(
            self,
            "Vpc",
            # ec2.Vpc accepts only zone names, so the zone IDs go in here as placeholders,
            # one per subnet, and are moved to the subnet's AvailabilityZoneId property below:
            # https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-subnet.html
            availability_zones=zone_ids or None,
            max_azs=None if zone_ids else MIN_AVAILABILITY_ZONES,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(name="Isolated", subnet_type=ec2.SubnetType.PRIVATE_ISOLATED),
            ],
        )

        if zone_ids:
            for subnet, zone_id in zip(self.vpc.isolated_subnets, zone_ids, strict=True):
                cfn_subnet = subnet.node.default_child
                cfn_subnet.add_property_deletion_override("AvailabilityZone")
                cfn_subnet.add_property_override("AvailabilityZoneId", zone_id)
