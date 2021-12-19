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
    numbers = raw_data.split("\n")
    counts = [0] * len(numbers[0])
    for number in numbers:
        for i in range(len(number)):
            if number[i] == "1":
                counts[i] += 1
    epsilon = ""
    gamma = ""
    for count in counts:
        if count > len(numbers) / 2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    print(f"Part 1 : {int(gamma, 2) * int(epsilon, 2)}")
    oxygen = find_oxygen(list(numbers))
    co2 = find_co2(list(numbers))
    print(f"Part 2 : {int(oxygen, 2) * int(co2, 2)}")

def find_oxygen(numbers: list) -> int:
    idx = 0
    while len(numbers) > 1:
        count = 0
        to_remove = list()
        for number in numbers:
            if number[idx] == "1":
                count += 1
        if count >= len(numbers) / 2:
            for number in numbers:
                if number[idx] == "0":
                    to_remove.append(number)
        else:
            for number in numbers:
                if number[idx] == "1":
                    to_remove.append(number)
        for number in to_remove:
            numbers.remove(number)
        idx += 1
    return numbers[0]

def find_co2(numbers: list) -> int:
    idx = 0
    while len(numbers) > 1:
        count = 0
        to_remove = list()
        for number in numbers:
            if number[idx] == "1":
                count += 1
        if count < len(numbers) / 2:
            for number in numbers:
                if number[idx] == "0":
                    to_remove.append(number)
        else:
            for number in numbers:
                if number[idx] == "1":
                    to_remove.append(number)
        for number in to_remove:
            numbers.remove(number)
        idx += 1
    return numbers[0]

if __name__ == "__main__":
    print(run_script("input.txt"))