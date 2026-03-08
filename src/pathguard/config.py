from dataclasses import dataclass
import os


@dataclass
class Settings:
    aws_region: str = os.getenv("PATHGUARD_AWS_REGION", "us-east-1")
    output_path: str = os.getenv("PATHGUARD_OUTPUT_PATH", "reports")


def get_settings() -> Settings:
    return Settings()