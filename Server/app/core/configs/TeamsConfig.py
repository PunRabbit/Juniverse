import os
from dataclasses import dataclass
from Server.app.core.ConfigAbstract import ConfigClass


@dataclass(frozen=True)
class TeamsConfig(ConfigClass):
    pass
