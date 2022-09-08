from dataclasses import dataclass
from Server.app.core.configs.BaseConfig import BaseConfig
from Server.app.core.configs.ClovaConfig import ClovaConfig
from Server.app.core.configs.DBConfig import DBConfig
from Server.app.core.configs.UserConfig import UserConfig
from Server.app.core.configs.SlackConfig import SlackConfig


@dataclass(frozen=False)
class CompactConfig:
    BASE: BaseConfig = BaseConfig()
    CLOVA: ClovaConfig = ClovaConfig()
    DB: DBConfig = DBConfig()
    USER: UserConfig = UserConfig()
    SLACK: SlackConfig = SlackConfig()


CONFIG: CompactConfig = CompactConfig()
