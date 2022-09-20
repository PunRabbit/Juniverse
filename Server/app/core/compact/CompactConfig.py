from dataclasses import dataclass
from Server.app.core.ConfigAbstract import ConfigClass
from Server.app.core.configs.BaseConfig import BaseConfig
from Server.app.core.configs.ClovaConfig import ClovaConfig
from Server.app.core.configs.DBConfig import DBConfig
from Server.app.core.configs.UserConfig import UserConfig
from Server.app.core.configs.SlackConfig import SlackConfig
from Server.app.core.configs.TeamsConfig import TeamsConfig
from Server.app.core.configs.SlackTemplates import SlackTemplates


@dataclass(frozen=False)
class CompactConfig:
    BASE: ConfigClass = BaseConfig()
    CLOVA: ConfigClass = ClovaConfig()
    DB: ConfigClass = DBConfig()
    USER: ConfigClass = UserConfig()
    SLACK: ConfigClass = SlackConfig()
    TEAMS: ConfigClass = TeamsConfig()
    SLACK_TEMPLATES: ConfigClass = SlackTemplates()


CONFIG: CompactConfig = CompactConfig()
