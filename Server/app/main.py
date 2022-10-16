import sys
import os
sys.path.append(os.getcwd()[:-11])

import uvicorn
from unittest import TestResult
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from Server.app.core.compact.CompactConfig import CONFIG
from Server.app.test.compactRunner.CompactRunner import CompactRunnerModule


app: FastAPI = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[CONFIG.BASE.SERVER_ALLOW_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


if __name__ == "__main__":
    try:
        run_flag: str = sys.argv[1]
        if run_flag == "test":
            test_result: TestResult = CompactRunnerModule().start_test()
            stream = os.popen("coverage report")
            output = stream.read()
            coverage_int: int = int(output[-4:-2])
            if coverage_int < CONFIG.TEST.SCORE:
                print(f"현재 커버리지: {coverage_int}%. 기준 커버리지 {CONFIG.TEST.SCORE}% 에 도달하지 못했습니다.")
                sys.exit(1)
            elif test_result.wasSuccessful() is True:
                print(f"현재 커버리지: {coverage_int}%. 기준 커버리지 {CONFIG.TEST.SCORE}% 를 상회합니다.")
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

