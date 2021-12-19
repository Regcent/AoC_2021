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
    print(f"Part 1 : {part_1(raw_data)}")
    print(f"Part 2 : {part_2(raw_data)}")

def part_1(raw_data: str) -> int:
    x = 0
    y = 0
    commands = raw_data.split("\n")
    for command in commands:
        command = command.split()
        if command[0] == "forward":
            x += int(command[1])
        elif command[0] == "down":
            y += int(command[1])
        elif command[0] == "up":
            y -= int(command[1])
        else:
            print(f"Abnormal command : {command}")
    return x * y

def part_2(raw_data: str) -> int:
    x = 0
    y = 0
    aim = 0
    commands = raw_data.split("\n")
    for command in commands:
        command = command.split()
        if command[0] == "forward":
            x += int(command[1])
            y += aim * int(command[1])
        elif command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])
        else:
            print(f"Abnormal command : {command}")
    return x * y
    
if __name__ == "__main__":
    print(run_script("input.txt"))