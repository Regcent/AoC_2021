import time
from typing import Union
import re

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
    result = re.findall("-?\d+", raw_data) 
    x0_target = int(result[0])
    x1_target = int(result[1])
    y0_target = int(result[2])
    y1_target = int(result[3])
    candidate_y = []
    for y in range(abs(y0_target)):
        total = 0
        i = 1
        while total > y0_target:
            total -= y + i 
            if total <= y1_target:
                candidate_y.append(y)
                break
            i += 1
    print(f"Part 1: {candidate_y[-1] * (candidate_y[-1] + 1) / 2}")
    for i in range(len(candidate_y)):
        candidate_y.append(- candidate_y[i] - 1)
    candidate_x = []
    for x in range(x1_target, 0, -1):
        total = 0
        i = 0
        while total < x1_target:
            total += x - i 
            if total >= x0_target and total <= x1_target:
                candidate_x.append(x)
                break
            i += 1
            if i >= x:
                break
    initial_speeds = []
    for y in candidate_y:
        for x in candidate_x:
            if check_valid(x, y, x0_target, x1_target, y0_target, y1_target):
                initial_speeds.append((x, y))
    print(f"Part 2: {len(initial_speeds)}")
    
def check_valid(x: int, y: int, x0_target: int, x1_target: int, y0_target: int, y1_target: int):
    current_x = 0
    current_y = 0
    speed_x = x
    speed_y = y
    while True:
        current_x += speed_x
        current_y += speed_y
        if current_x >= x0_target and current_x <= x1_target and current_y >= y0_target and current_y <= y1_target:
            return True
        if current_x > x1_target:
            return False
        if current_y < y0_target:
            return False
        if abs(speed_x) > 0:
            speed_x -= 1
        speed_y -= 1

if __name__ == "__main__":
    print(run_script("input.txt"))