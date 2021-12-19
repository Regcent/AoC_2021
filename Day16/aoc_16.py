import time
from typing import Union

class Packet:

    def __init__(self, version, type, subdata):
        self.version = version
        self.type = type
        self.subdata = subdata

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
    bits = ""
    for char in raw_data:
        bits += bin(int(char, 16))[2:]
    packets = parse_packets(bits)

def parse_packets(bits: str) -> list:
    idx = 0
    

if __name__ == "__main__":
    print(run_script("input.txt"))