from abc import ABCMeta, abstractmethod
from typing import List


class BaseDBSelectModel(metaclass=ABCMeta):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def single_select(self, query: str) -> str:
        pass

    @abstractmethod
    def multi_select(self, query: str) -> List[str]:
        pass


class BaseDBInsertModel(metaclass=ABCMeta):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def single_insert(self) -> bool:
        pass

    @abstractmethod
    def multi_insert(self) -> bool:
        pass


class BaseDBUpdateModel(metaclass=ABCMeta):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def single_update(self) -> bool:
        pass

    @abstractmethod
    def multi_update(self) -> bool:
        pass


class BaseDBDeleteModel(metaclass=ABCMeta):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def single_delete(self) -> bool:
        pass

    @abstractmethod
    def multi_delete(self) -> bool:
        pass

    @abstractmethod
    def truncate(self) -> bool:
        pass


class DataToDTO(metaclass=ABCMeta):
    """
    Error는 내부에서 Assert로 잡아낼 것
    """
    @abstractmethod
    def convert(self) -> None:
        pass
