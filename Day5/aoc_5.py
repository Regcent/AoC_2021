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
    vents = {}
    vents_str = raw_data.split("\n")
    for segment in vents_str:
        points = segment.split(" -> ")
        start = points[0].split(",")
        end = points[1].split(",")
        x0 = int(start[0])
        y0 = int(start[1])
        x1 = int(end[0])
        y1 = int(end[1])
        if x0 != x1 and y0 != y1:
            if x0 < x1 and y0 < y1:
                for i in range(x1 - x0 + 1):
                    if (x0 + i, y0 + i) not in vents:
                        vents[(x0 + i, y0 + i)] = 0
                    vents[(x0 + i, y0 + i)] += 1
            elif x0 > x1 and y0 > y1:
                for i in range(x0 - x1 + 1):
                    if (x1 + i, y1 + i) not in vents:
                        vents[(x1 + i, y1 + i)] = 0
                    vents[(x1 + i, y1 + i)] += 1
            elif x0 < x1 and y0 > y1:
                for i in range(x1 - x0 + 1):
                    if (x0 + i, y0 - i) not in vents:
                        vents[(x0 + i, y0 - i)] = 0
                    vents[(x0 + i, y0 - i)] += 1
            else:
                for i in range(x0 - x1 + 1):
                    if (x1 + i, y1 - i) not in vents:
                        vents[(x1 + i, y1 - i)] = 0
                    vents[(x1 + i, y1 - i)] += 1
        if x0 == x1:
            if y0 > y1:
                for i in range(y1, y0 + 1):
                    if (x0, i) not in vents:
                        vents[(x0, i)] = 0
                    vents[(x0, i)] += 1
            else:
                 for i in range(y0, y1 + 1):
                    if (x0, i) not in vents:
                        vents[(x0, i)] = 0
                    vents[(x0, i)] += 1
        if y0 == y1:
            if x1 > x0:
                for i in range(x0, x1 + 1):
                    if (i, y0) not in vents:
                        vents[(i, y0)] = 0
                    vents[(i, y0)] += 1
            else:
                for i in range(x1, x0 + 1):
                    if (i, y0) not in vents:
                        vents[(i, y0)] = 0
                    vents[(i, y0)] += 1
    risk_count = 0
    for position in vents:
        if vents[position] > 1:
            risk_count += 1
    print(f"Part 1: {risk_count}")

if __name__ == "__main__":
    print(run_script("input.txt"))