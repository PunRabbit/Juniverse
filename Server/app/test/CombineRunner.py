from unittest import TextTestRunner, TestCase, TestSuite
from overrides import overrides
from dataclasses import dataclass
from Server.app.test.Abstract import CombineRunnerModel
from Server.app.test.TestCaseList import TestCaseList


class CombineRunnerModule(CombineRunnerModel, TextTestRunner):
    def __init__(self):
        super().__init__(verbosity=2)
        self.test_case_list: dataclass = TestCaseList()

    @overrides(check_signature=True)
    def set_runners(self) -> TestSuite:
        suite: TestSuite = TestSuite()

        for target_instance in self._find_instance_in_dataclass():
            suite: TestSuite = self._combine_test_to_suite(init_suite=suite,
                                                           target_class=target_instance)

        return suite

    @overrides(check_signature=True)
    def start_test(self) -> None:
        self.run(self.set_runners())

    def _find_instance_in_dataclass(self) -> list:
        dataclass_attribute_list: list = []
        target_instance_list: list = []

        for target_attribute in dir(self.test_case_list):
            if target_attribute[:2] != "__" and target_attribute[:1] != "_":
                dataclass_attribute_list.append(target_attribute)

        for target_instance in dataclass_attribute_list:
            target_instance_list.append(getattr(self.test_case_list, target_instance))

        return target_instance_list

    def _combine_test_to_suite(self, init_suite: TestSuite, target_class: TestCase):
        method_list: list = self._find_test_method(target_class=target_class)

        for method in method_list:
            init_suite.addTest(type(target_class)(f"{method}"))

        return init_suite

    @classmethod
    def _find_test_method(cls, target_class: TestCase) -> list:
        method_list: list = []
        target_method_list: list = [i for i in range(len(dir(target_class))) if "test_" in dir(target_class)[i]]

        for target_method in target_method_list:
            method_list.append(dir(target_class)[target_method])

        return method_list
