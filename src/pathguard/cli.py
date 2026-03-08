import sys

from pathguard.config import get_settings
from pathguard.collector import AWSNetworkCollector


def analyze():
    settings = get_settings()

    collector = AWSNetworkCollector(region=settings.aws_region)
    data = collector.collect_all()

    print("PathGuard inventory summary")
    print(f"Region: {settings.aws_region}")
    print(f"VPCs found: {len(data['vpcs'])}")
    print(f"Subnets found: {len(data['subnets'])}")

def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: py -m pathguard.cli analyze")
        return 1

    command = sys.argv[1]

    if command == "analyze":
        return analyze()

    print(f"Unknown command: {command}")
    return 1


if __name__ == "__main__":
    sys.exit(main())