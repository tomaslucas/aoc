# aoc_202101.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input"""
    return [int(line) for line in puzzle_input.split("\n")]

def part1(data):
    """Solve part 1"""
    counter = 0
    base_value = data[0]
    for i in range(1,len(data)):
        if data[i] > base_value:
            counter += 1
        base_value = data[i]
    return counter
                

def part2(data):
    """Solve part 2"""
    sum_values = [(data[i] + data[i+1] + data[i+2]) for i in range(0, len(data)) if i+2 < len(data)]
    counter = 0
    base_value = sum_values[0]
    for i in range(1, len(sum_values)):
        if sum_values[i] > base_value:
            counter += 1
        base_value = sum_values[i]
    return counter


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))