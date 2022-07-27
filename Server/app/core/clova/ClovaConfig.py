from dataclasses import dataclass


@dataclass(frozen=True)
class ClovaConfig(object):
    USER_ID: str = ""
    USER_PWD: str = ""


clova_config: ClovaConfig = ClovaConfig()

