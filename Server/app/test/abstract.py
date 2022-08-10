from abc import ABCMeta, abstractmethod
from unittest import TestSuite


class CombineRunnerModel(metaclass=ABCMeta):
    @abstractmethod
    def set_runners(self) -> TestSuite:
        pass

    @abstractmethod
    def start_test(self) -> None:
        pass
