import time
from typing import Union
from copy import deepcopy

class BingoBoard:

    def __init__(self):
        self.remaining_numbers = dict()
        self.board = dict()
        self.rows = [[], [], [], [], []]
        self.cols = [[], [], [], [], []]
        self.bingo = False

    def add_number(self, number: int, row: int, col: int):
        self.remaining_numbers[number] = (row, col)
        self.board[(row, col)] = number
        self.rows[row].append(number)
        self.cols[col].append(number)

    def remove_number(self, number : int):
        if number not in self.remaining_numbers:
            return
        (row, col) = self.remaining_numbers[number]
        self.rows[row].remove(number)
        if len(self.rows[row]) == 0:
            self.bingo = True
        self.cols[col].remove(number)
        if len(self.cols[col]) == 0:
            self.bingo = True
        del self.remaining_numbers[number]

    def parse_board(self, str_board: str):
        rows = str_board.split("\n")
        for row in range(len(rows)):
            numbers_unfiltered = rows[row].split(" ")
            while len(numbers_unfiltered) > 5:
                numbers_unfiltered.remove("")
            numbers = [int(i) for i in numbers_unfiltered]
            for col in range(len(numbers)):
                self.add_number(numbers[col], row, col)

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
    elements = raw_data.split("\n\n")
    drawn_numbers = [int(i) for i in elements[0].split(",")]
    elements.pop(0)
    boards = []
    for str_board in elements:
        board = BingoBoard()
        board.parse_board(str_board)
        boards.append(board)
    part_1(deepcopy(boards), drawn_numbers)
    part_2(deepcopy(boards), drawn_numbers)

def part_1(boards: list, drawn_numbers: list) -> None:
    bingo = False
    last_drawn = -1
    winning_board = None
    while not bingo:
        for number in drawn_numbers:
            if bingo:
                break
            last_drawn = number
            for board in boards:
                board.remove_number(number)
                if board.bingo:
                    winning_board = board
                    bingo = True
                    break
    print(f"Part 1: {last_drawn * sum(list(winning_board.remaining_numbers))}")

def part_2(boards: list, drawn_numbers: list) -> None:
    board_count = len(boards)
    bingo_count = 0
    last_drawn = -1
    last_board = None
    while not bingo_count == board_count:
        for number in drawn_numbers:
            if last_board:
                break
            last_drawn = number
            to_remove = []
            for board in boards:
                board.remove_number(number)
                if board.bingo:
                    bingo_count += 1
                    if bingo_count == board_count:
                        last_board = board
                    else:
                        to_remove.append(board)
            for board in to_remove:
                boards.remove(board)
    print(f"Part 2: {last_drawn * sum(list(last_board.remaining_numbers))}")

if __name__ == "__main__":
    print(run_script("input.txt"))