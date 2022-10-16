import time
from tqdm import tqdm


def server_load_counter(delay_time: int):
    print(f"{delay_time}초 뒤에 서버가 시작됩니다.")
    load_counter: int = 0
    for i in tqdm(range(delay_time * 10)):
        time.sleep(0.1)
        load_counter += i
    print(load_counter)
