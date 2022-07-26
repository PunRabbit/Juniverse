from dataclasses import dataclass


@dataclass
class ClovaConfig(object):
    USER_ID: str = ""
    USER_PWD: str = ""


clova_config: ClovaConfig = ClovaConfig()

