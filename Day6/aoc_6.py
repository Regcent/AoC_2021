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
    """
    Time to code! Write your code here to solve today's problem
    """
    fishes = {}
    for i in range(9):
        fishes[i] = 0
    start = [int(i) for i in raw_data.split(",")]
    for val in start:
        fishes[val] += 1
    for i in range(80):
        new_fishes = {}
        for i in range(8):
            new_fishes[i] = fishes[i + 1]
        new_fishes[6] += fishes[0]
        new_fishes[8] = fishes[0]
        fishes = new_fishes
    total = 0
    for i in range(9):
        total += fishes[i]
    print(f"Part 1: {total}")
    for i in range(176):
        new_fishes = {}
        for i in range(8):
            new_fishes[i] = fishes[i + 1]
        new_fishes[6] += fishes[0]
        new_fishes[8] = fishes[0]
        fishes = new_fishes
    total = 0
    for i in range(9):
        total += fishes[i]
    print(f"Part 2: {total}")

if __name__ == "__main__":
    print(run_script("input.txt"))