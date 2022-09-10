from Server.app.outer.db.user.UserEncryption import UserBcrypt
from Server.app.outer.db.user.UserAbstract import UserEncryptionModel


class UserDTO(object):
    __slots__ = [
        "id",
        "_password",
        "name",
        "authority_level",
        "country",
        "email",
        "type",
        "encryption_module"
    ]

    def __init__(self):
        self.id: str
        self._password: str
        self.name: str
        self.authority_level: int
        self.country: str
        self.email: str
        self.type: str
        self.encryption_module: UserEncryptionModel = UserBcrypt()

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password: str):
        self._password = self.encryption_module.encryption(word=password)




