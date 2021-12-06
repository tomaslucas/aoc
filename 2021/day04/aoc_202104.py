# aoc_202104.py

import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    puzzle_block = puzzle_input.split("\n")
    first_line = [int(e) for e in puzzle_input.split("\n")[0].split(",")]
    inicio = 2
    dblock = {}
    contador = 0
    while inicio <= len(puzzle_block):
        block = []
        for line in range(inicio, inicio + 5):
            block.append([int(e) for e in puzzle_block[line].split()])
        dblock[contador] = block
        inicio = inicio + 6
        contador += 1
    return first_line, dblock


def suma_bloque(b, dblock):
    for l in range(5):
        for e in range(5):
            if not isinstance(dblock[b][l][e], int):
                dblock[b][l][e] = 0
    suma = 0
    for l in range(5):
        for e in range(5):
            suma += dblock[b][l][e]
    return suma


def col_with_5x(block, col):
    contador = 0
    for row in range(5):
        contador += [block[row][col]].count("x")
        if contador == 5:
            return True
    return False


def row_with_5x(block, row):
    contador = 0
    for col in range(5):
        contador += [block[row][col]].count("x")
        if contador == 5:
            return True
    return False


def bingo(dblock, first_line):
    for number in first_line:
        for b in range(len(dblock)):
            for l in range(5):
                for e in range(5):
                    if number == dblock[b][l][e]:
                        dblock[b][l][e] = "x"
                        if row_with_5x(dblock[b], l) or col_with_5x(dblock[b], e):
                            return b, l, number, dblock


def bingo2(dblock, first_line):
    number_carts = 0
    rep_carts = []
    for number in first_line:
        for b in range(len(dblock)):
            for l in range(5):
                for e in range(5):
                    if number == dblock[b][l][e]:
                        dblock[b][l][e] = "x"
                        if row_with_5x(dblock[b], l) or col_with_5x(dblock[b], e):
                            if b not in rep_carts:
                                number_carts += 1
                            rep_carts.append(b)
                            if number_carts == len(dblock):
                                return b, l, number, dblock


def part1(first_line, data):
    """Solve part 1"""
    b, l, number, dblock = bingo(data, first_line)
    suma = suma_bloque(b, dblock)
    return suma * number


def part2(first_line, data):
    """Solve part 2"""
    b, l, number, dblock = bingo2(data, first_line)
    suma = suma_bloque(b, dblock)
    return suma * number


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    first_line, data = parse(puzzle_input)
    solution1 = part1(first_line, data)
    solution2 = part2(first_line, data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
