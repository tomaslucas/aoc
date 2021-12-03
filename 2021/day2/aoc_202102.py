# aoc_202102.py

import pathlib
import sys
import pandas as pd

def parse(puzzle_input):
    """Parse input"""
    return pd.read_csv(puzzle_input, delim_whitespace=True, names=['position','units'], header=None)


def part1(data):
    """Solve part 1"""
    grupo = (data.groupby("position").sum())
    vertical = grupo.loc['down']['units'] - grupo.loc['up']['units'] 
    horizontal = grupo.loc['forward']['units']
    return vertical * horizontal


def part2(data):
    """Solve part 2"""
    vertical = 0
    horizontal = 0
    aim = 0
    lista = list(data.values)
    for i in lista:
        if i[0] == 'down':
            vertical += i[1]
        elif i[0] == 'up':
            vertical -= i[1]
        else:
            horizontal += i[1]
            aim += (vertical * i[1])
    return(horizontal * aim)



def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path)
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))