from abc import ABCMeta, abstractmethod


class DataToDTO(metaclass=ABCMeta):
    """
    Error는 내부에서 Assert로 잡아낼 것
    """
    @abstractmethod
    def convert(self) -> None:
        pass

