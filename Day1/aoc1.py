import time
from typing import Union

def run_script(filepath: str) -> Union[int, str, float, bool]:
    with open(filepath, "r") as f:
        raw_data = f.read()
    return main_function(raw_data)

def main_function(raw_data: str) -> Union[int, str, float, bool]:
    start_time = time.time()
    
    result = your_script(raw_data)

    elapsed_time = time.time() - start_time
    print(f"Time elapsed : {elapsed_time}s")
    return result

def your_script(raw_data: str) -> Union[int, str, float, bool]:
    depths = [int(i) for i in raw_data.split("\n")]
    increases = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            increases += 1
    print(f"Part 1 : {increases}")
    sliding_increases = 0
    for i in range(3, len(depths)):
        common = depths[i - 2] + depths[i - 1] 
        first = depths[i - 3] + common
        second = common + depths[i]
        if second > first: 
            sliding_increases += 1
    print(f"Part 2 : {sliding_increases}")

if __name__ == "__main__":
    print(run_script("input.txt"))