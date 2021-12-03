# aoc_202103.py

import pathlib
import sys
import pandas as pd


def parse(puzzle_input):
    """Parse input"""
    return [[e for e in line] for line in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1"""
    df = pd.DataFrame(data)
    resumen = []
    for i in df.columns.values:
        resumen.append(df[i].value_counts(ascending=False).index[0])

    epsilon = int("".join(resumen), 2)
    gamma = int("".join("1" if x == "0" else "0" for x in resumen), 2)
    power = epsilon * gamma
    return power


def sub_part2(data, orden_h: bool, orden_l: bool, default_value: str) -> int:
    """Generate the decimal value selecting de hightest or lowest occurrency, depending of the orden_h and orden_l.
    If we want to select the hightest:
        orden_h=False, orden_l=True, default_value="1"
    If we want to select the lowest:
        orden_h=True, orden_l=False, default_value="0"
    The rest of rules are based on the puzzle.
    """
    df = pd.DataFrame(data)
    array = []
    for i in df.columns.values:
        high = df[i].value_counts(ascending=orden_h).index[0]
        low = df[i].value_counts(ascending=orden_l).index[0]
        if high == low:
            v_col = default_value
        else:
            v_col = df[i].value_counts(ascending=orden_h).index[0]

        array.append(v_col)
        df = df[df[i] == v_col]
        if len(df) <= 1:
            for j in range(i + 1, len(df.columns.values)):
                array.append(df.iloc[0][j])
            break
    return int("".join(array), 2)


def part2(data):
    """Solve part 2"""
    oxygen = sub_part2(data, orden_h=False, orden_l=True, default_value="1")
    co2 = sub_part2(data, orden_h=True, orden_l=False, default_value="0")
    return oxygen * co2


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
