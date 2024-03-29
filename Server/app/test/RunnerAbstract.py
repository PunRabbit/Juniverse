from abc import ABCMeta, abstractmethod
from unittest import TestSuite, TestResult


class CompactRunnerModel(metaclass=ABCMeta):
    @abstractmethod
    def set_runners(self) -> TestSuite:
        pass

    @abstractmethod
    def start_test(self) -> TestResult:
        pass
