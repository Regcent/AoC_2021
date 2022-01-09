import time
from typing import Union

class DiracDice:

    def __init__(self, p1_pos: int, p2_pos: int, p1_score: int, p2_score: int, max_score: int):
        self.p1_pos = p1_pos
        self.p2_pos = p2_pos
        self.p1_score = p1_score
        self.p2_score = p2_score
        self.max_score = max_score
        self.finished = False
        self.p1_wins = None

    def advance_p1(self, value: int):
        self.p1_pos += value
        if self.p1_pos > 10:
            self.p1_pos -= 10
        self.p1_score += self.p1_pos
    
    def advance_p2(self, value: int):
        self.p2_pos += value
        if self.p2_pos > 10:
            self.p2_pos -= 10
        self.p2_score += self.p2_pos

    def check(self):
        if self.p1_score >= self.max_score:
            self.finished = True
            self.p1_wins = True
        if self.p2_score >= self.max_score:
            self.finished = True
            self.p1_wins = False

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
    lines = raw_data.split("\n")
    p1_pos = int(lines[0][-2:])
    p2_pos = int(lines[1][-2:])
    print(f"Part 1: {part_one(p1_pos, p2_pos)}")

def part_one(p1_pos: int, p2_pos: int) -> int:
    dice = 1
    turn_count = 0
    game = DiracDice(p1_pos, p2_pos, 0, 0, 1000)
    while not game.finished:
        progress = (dice * 3 + 3) % 10
        if turn_count % 2 == 0:
            game.advance_p1(progress)
        else:
            game.advance_p2(progress)
        turn_count += 1
        dice += 3
        game.check()
        if dice >= 10:
            dice = dice - 10
    if game.p1_wins:
        return game.p2_score * turn_count * 3
    else:
        return game.p1_score * turn_count * 3

if __name__ == "__main__":
    print(run_script("input.txt"))