from dataclasses import dataclass
from typing import Union
from Server.app.core.ConfigAbstract import ConfigClass, CompactConfigClass, TemplateClass
from Server.app.core.configs.BaseConfig import BaseConfig
from Server.app.core.configs.ClovaConfig import ClovaConfig
from Server.app.core.configs.DBConfig import DBConfig
from Server.app.core.configs.UserConfig import UserConfig
from Server.app.core.configs.SlackConfig import SlackConfig
from Server.app.core.configs.TeamsConfig import TeamsConfig
from Server.app.core.configs.SlackTemplates import SlackTemplates
from Server.app.core.configs.TestConfig import TestConfig


@dataclass(frozen=False)
class CompactConfig:
    BASE: Union[ConfigClass, BaseConfig] = BaseConfig()
    CLOVA: Union[ConfigClass, ClovaConfig] = ClovaConfig()
    DB: Union[ConfigClass, DBConfig] = DBConfig()
    USER: Union[ConfigClass, UserConfig] = UserConfig()
    SLACK: Union[ConfigClass, SlackConfig] = SlackConfig()
    TEAMS: Union[ConfigClass, TeamsConfig] = TeamsConfig()
    SLACK_TEMPLATES: Union[TemplateClass, SlackTemplates] = SlackTemplates()
    TEST: Union[TemplateClass, TestConfig] = TestConfig()


CONFIG: Union[CompactConfigClass, CompactConfig] = CompactConfig()
