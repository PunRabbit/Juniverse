from Server.app.db.user.UserAbstract import UserEncryptionModel
from Server.app.core.configs.BaseConfig import BASE_CONFIG
from overrides import overrides


class UserBcrypt(UserEncryptionModel):
    def __init__(self):
        self.key: str = BASE_CONFIG.SERVER_BCRYPT_KEY
        self.byte_key: bytes = self.key.encode('UTF-8')

    @overrides
    def encryption(self, word: str) -> str:
        pass

    @overrides
    def decryption(self, encrypted_word: str) -> str:
        pass

    def _check_key(self) -> bool:
        pass


class UserCryptography(UserEncryptionModel):
    def __init__(self):
        pass

    @overrides
    def encryption(self, word: str) -> str:
        pass

    @overrides
    def decryption(self, encrypted_word: str) -> str:
        pass
