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


def serve():
    import uvicorn

    settings = get_settings()
    uvicorn.run("pathguard.api:app", host=settings.api_host, port=settings.api_port)


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: pathguard <command>")
        print("Commands: analyze, serve")
        return 1

    command = sys.argv[1]

    if command == "analyze":
        return analyze()

    if command == "serve":
        serve()
        return 0

    print(f"Unknown command: {command}")
    return 1


if __name__ == "__main__":
    sys.exit(main())