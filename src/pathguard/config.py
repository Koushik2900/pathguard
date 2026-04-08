from dataclasses import dataclass
import os


@dataclass
class Settings:
    aws_region: str = os.getenv("PATHGUARD_AWS_REGION", "us-east-1")
    output_path: str = os.getenv("PATHGUARD_OUTPUT_PATH", "reports")
    api_host: str = os.getenv("PATHGUARD_API_HOST", "0.0.0.0")
    api_port: int = int(os.getenv("PATHGUARD_API_PORT", "8080"))


def get_settings() -> Settings:
    return Settings()