from dataclasses import dataclass
from Server.app.core.ConfigAbstract import ConfigClass


@dataclass(frozen=True)
class UserConfig(ConfigClass):
    pass
