import uvicorn
import sys
import os
from unittest import TestResult
from Server.app.test.compactRunner.CompactRunner import CompactRunnerModule
from Server.app.runner.LoadDelay import server_load_counter
from Server.app.core.compact.CompactConfig import CONFIG


def main_run():
    try:
        run_flag: str = sys.argv[1]
        if run_flag == "test":
            test_result: TestResult = CompactRunnerModule().start_test()
            stream = os.popen("coverage report")
            output: str = stream.read()
            coverage_int: int = int(output[-4:-2])
            if coverage_int < CONFIG.TEST.SCORE:
                print(f"현재 커버리지: {coverage_int}%. 기준 커버리지 {CONFIG.TEST.SCORE}% 에 도달하지 못했습니다.")
                sys.exit(1)
            elif test_result.wasSuccessful() is True:
                print(f"현재 커버리지: {coverage_int}%. 기준 커버리지 {CONFIG.TEST.SCORE}% 를 상회합니다.")
                server_load_counter(delay_time=CONFIG.TEST.LOAD_DELAY)
                uvicorn.run(
                    CONFIG.BASE.DEFAULT_BRIDGE,
                    host=CONFIG.BASE.SERVER_URL,
                    port=CONFIG.BASE.SERVER_PORT,
                    workers=CONFIG.BASE.SERVER_WORKER_NUM,
                    reload=True
                )
            else:
                print(f"현재 커버리지: {coverage_int}%. 기준 커버리지 {CONFIG.TEST.SCORE}% 를 넘겼으나 테스트 실패입니다.")
                sys.exit(1)
    except IndexError:
        os.system("coverage run -m main test discover")


