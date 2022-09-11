import os
from dataclasses import dataclass


@dataclass(frozen=True)
class SlackConfig:
    TOKEN: str = os.getenv("SLACK_TOKEN")

