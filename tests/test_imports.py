from pathguard.config import get_settings
from pathguard.collector import AWSNetworkCollector


def test_imports():
    settings = get_settings()
    collector = AWSNetworkCollector(region=settings.aws_region)

    assert settings.aws_region
    assert collector.region == settings.aws_region