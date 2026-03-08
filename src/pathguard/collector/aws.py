class AWSNetworkCollector:
    def __init__(self, region: str) -> None:
        self.region = region

    def collect_vpcs(self):
        return []

    def collect_subnets(self):
        return []

    def collect_route_tables(self):
        return []

    def collect_security_groups(self):
        return []

    def collect_internet_gateways(self):
        return []

    def collect_nat_gateways(self):
        return []

    def collect_network_interfaces(self):
        return []

    def collect_all(self):
        return {
            "vpcs": self.collect_vpcs(),
            "subnets": self.collect_subnets(),
            "route_tables": self.collect_route_tables(),
            "security_groups": self.collect_security_groups(),
            "internet_gateways": self.collect_internet_gateways(),
            "nat_gateways": self.collect_nat_gateways(),
            "network_interfaces": self.collect_network_interfaces(),
        }