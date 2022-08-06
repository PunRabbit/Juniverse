from abc import ABCMeta, abstractmethod


class UserEncryptionModel(metaclass=ABCMeta):
    @abstractmethod
    def encryption(self, word: str) -> str:
        pass

    @abstractmethod
    def decryption(self, encrypted_word: str) -> str:
        pass
