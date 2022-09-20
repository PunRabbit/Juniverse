import os
from dataclasses import dataclass
from Server.app.core.ConfigAbstract import ConfigClass


@dataclass(frozen=True)
class SlackConfig(ConfigClass):
    TOKEN: str = os.getenv("SLACK_TOKEN")

