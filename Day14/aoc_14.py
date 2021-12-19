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
    data = raw_data.split("\n\n")
    pairs, letters = parse_pairs(data[0])
    pair_gen, letter_gen = parse_pair_gen(data[1])
    solve_part_1(dict(pairs), dict(letters), pair_gen, letter_gen)
    solve_part_2(dict(pairs), dict(letters), pair_gen, letter_gen)

def solve_part_1(pairs: dict, letters: dict, pair_gen: dict, letter_gen: dict) -> None:
    for i in range(10):
        pairs = apply_step(pairs, letters, pair_gen, letter_gen)
    maximum = 0
    minimum = 1 << 64
    for letter in letters:
        if letters[letter] > maximum:
            maximum = letters[letter]
        if letters[letter] < minimum:
            minimum = letters[letter]
    print(f"Part 1: {maximum - minimum}")

def solve_part_2(pairs: dict, letters: dict, pair_gen: dict, letter_gen: dict) -> None:
    for i in range(40):
        pairs = apply_step(pairs, letters, pair_gen, letter_gen)
    maximum = 0
    minimum = 1 << 64
    for letter in letters:
        if letters[letter] > maximum:
            maximum = letters[letter]
        if letters[letter] < minimum:
            minimum = letters[letter]
    print(f"Part 2: {maximum - minimum}")

def parse_pairs(sentence: str) -> dict:
    pairs = {}
    letters = {}
    for i in range(len(sentence) - 1):
        add_to_dict(letters, sentence[i])
        add_to_dict(pairs, sentence[i:i + 2])
    add_to_dict(letters, sentence[-1])
    return pairs, letters

def parse_pair_gen(pair_rules: str) -> dict:
    pair_gen = {}
    letter_gen = {}
    for rule in pair_rules.split("\n"):
        elements = rule.split(" -> ")
        letter_gen[elements[0]] = elements[1]
        new_pairs = [elements[0][0] + elements[1], elements[1] + elements[0][1]]
        pair_gen[elements[0]] = new_pairs
    return pair_gen, letter_gen

def add_to_dict(dictionary: dict, element: str, count: int = 1) -> None:
    if element not in dictionary:
        dictionary[element] = 0
    dictionary[element] += count

def apply_step(pairs: dict, letters: dict, pair_gen: dict, letter_gen: dict) -> dict:
    new_pairs = {}
    for pair in pairs:
        if pair in letter_gen:
            add_to_dict(letters, letter_gen[pair], pairs[pair])
            add_to_dict(new_pairs, pair_gen[pair][0], pairs[pair])
            add_to_dict(new_pairs, pair_gen[pair][1], pairs[pair])
        else:
            add_to_dict(new_pairs, pair, pairs[pair])
    return new_pairs

if __name__ == "__main__":
    print(run_script("input.txt"))