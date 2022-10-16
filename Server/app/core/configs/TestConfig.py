import os
from dataclasses import dataclass
from Server.app.core.ConfigAbstract import ConfigClass


@dataclass(frozen=True)
class TestConfig(ConfigClass):
    SCORE: int = int(os.getenv("TEST_SCORE"))


