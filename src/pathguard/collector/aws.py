import boto3


class AWSNetworkCollector:
    def __init__(self, region: str):
        self.region = region
        self.ec2 = boto3.client("ec2", region_name=region)

    def collect_vpcs(self):
        response = self.ec2.describe_vpcs()

        vpcs = []
        for vpc in response.get("Vpcs", []):
            vpcs.append({
                "vpc_id": vpc.get("VpcId"),
                "cidr_block": vpc.get("CidrBlock"),
                "state": vpc.get("State"),
                "tags": vpc.get("Tags", [])
            })

        return vpcs

    def collect_subnets(self):
        response = self.ec2.describe_subnets()

        subnets = []
        for subnet in response.get("Subnets", []):
            subnets.append({
                "subnet_id": subnet.get("SubnetId"),
                "vpc_id": subnet.get("VpcId"),
                "cidr_block": subnet.get("CidrBlock"),
                "availability_zone": subnet.get("AvailabilityZone"),
                "state": subnet.get("State"),
                "tags": subnet.get("Tags", [])
            })

        return subnets

    def collect_all(self):
        return {
            "vpcs": self.collect_vpcs(),
            "subnets": self.collect_subnets(),
        }