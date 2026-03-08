import sys

from pathguard.config import get_settings


def analyze() -> int:
    settings = get_settings()
    print("PathGuard initialized")
    print(f"AWS region: {settings.aws_region}")
    print(f"Output path: {settings.output_path}")
    return 0


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