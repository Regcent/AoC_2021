import time
from typing import Union

class Packet:

    def __init__(self, version, ptype, value, subpackets):
        self.version = version
        self.ptype = ptype
        self.value = value
        self.subpackets = subpackets

    def __str__(self):
        subpackets_str = "[" + "; ".join([str(sub) for sub in self.subpackets]) + "]"
        return f"Version {self.version}, Type {self.ptype}, Value {self.value}, Subpackets {subpackets_str}"

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
        new_bits = bin(int(char, 16))[2:]
        while len(new_bits) < 4:
            new_bits = "0" + new_bits
        bits += new_bits
    packets = []
    parse_packets(bits, packets)
    print(f"Part 1: {total_version(packets)}")
    print(f"Part 2: {resolve_packet(packets[0])}")

def parse_packets(bits: str, packets: list, max_count: int = 1000) -> int:
    packet_count = 0
    idx = 0
    while idx < len(bits) - 10 and packet_count < max_count:
        version = int(bits[idx:idx + 3], 2)
        idx += 3
        ptype = int(bits[idx:idx + 3], 2)
        idx += 3
        if ptype == 4:
            literal_value_str = ""
            while bits[idx] == "1":
                literal_value_str += bits[idx + 1:idx + 5]
                idx += 5
            literal_value_str += bits[idx + 1:idx + 5]
            idx += 5
            packets.append(Packet(version, ptype, int(literal_value_str, 2), []))
            packet_count += 1
        else:
            if bits[idx] == "0":
                length = int(bits[idx+1:idx+16], 2)
                idx += 16
                subpackets = []
                subp_count, sub_idx = parse_packets(bits[idx:idx + length], subpackets)
                idx += sub_idx
                packets.append(Packet(version, ptype, 0, subpackets))
                packet_count += 1
            else:
                number = int(bits[idx+1:idx+12], 2)
                idx += 12
                subpackets = []
                subp_count, sub_idx = parse_packets(bits[idx:], subpackets, number)
                idx += sub_idx
                packets.append(Packet(version, ptype, 0, subpackets))
                packet_count += 1
    return packet_count, idx

def resolve_packet(packet: Packet) -> int:
    if packet.ptype == 0:
        subp_vals = []
        for sub in packet.subpackets:
            subp_vals.append(resolve_packet(sub))
        return sum(subp_vals)
    elif packet.ptype == 1:
        total = 1
        for sub in packet.subpackets:
            total *= resolve_packet(sub)
        return total
    elif packet.ptype == 2:
        subp_vals = []
        for sub in packet.subpackets:
            subp_vals.append(resolve_packet(sub))
        return min(subp_vals)
    elif packet.ptype == 3:
        subp_vals = []
        for sub in packet.subpackets:
            subp_vals.append(resolve_packet(sub))
        return max(subp_vals)
    elif packet.ptype == 4:
        return packet.value
    elif packet.ptype == 5:
        subp_vals = []
        for sub in packet.subpackets:
            subp_vals.append(resolve_packet(sub))
        return 1 if subp_vals[0] > subp_vals[1] else 0
    elif packet.ptype == 6:
        subp_vals = []
        for sub in packet.subpackets:
            subp_vals.append(resolve_packet(sub))
        return 1 if subp_vals[0] < subp_vals[1] else 0
    elif packet.ptype == 7:
        subp_vals = []
        for sub in packet.subpackets:
            subp_vals.append(resolve_packet(sub))
        return 1 if subp_vals[0] == subp_vals[1] else 0

def total_version(packets: list):
    total = 0
    for packet in packets:
        total += packet.version
        total += total_version(packet.subpackets)
    return total

if __name__ == "__main__":
    print(run_script("input.txt"))