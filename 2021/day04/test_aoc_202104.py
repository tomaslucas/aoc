# test_aoc_202104.py

import pathlib
import pytest
import aoc_202104 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    first_line, data = aoc.parse(puzzle_input)
    return first_line, data


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    first_line, data = aoc.parse(puzzle_input)
    return first_line, data


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly"""
    first_line, example1_d = example1
    assert first_line == [
        7,
        4,
        9,
        5,
        11,
        17,
        23,
        2,
        0,
        14,
        21,
        24,
        10,
        16,
        13,
        6,
        15,
        25,
        12,
        22,
        18,
        20,
        8,
        19,
        3,
        26,
        1,
    ]
    assert example1_d == {
        0: [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19],
        ],
        1: [
            [3, 15, 0, 2, 22],
            [9, 18, 13, 17, 5],
            [19, 8, 7, 25, 23],
            [20, 11, 10, 24, 4],
            [14, 21, 16, 12, 6],
        ],
        2: [
            [14, 21, 17, 24, 4],
            [10, 16, 15, 9, 19],
            [18, 8, 23, 26, 20],
            [22, 11, 13, 6, 5],
            [2, 0, 12, 3, 7],
        ],
    }


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    first_line, example1_d = example1
    assert aoc.part1(first_line, example1_d) == 4512


def test_part1_example2(example2):
    """Test part 1 on example input"""
    first_line, example2_d = example2
    assert aoc.part1(first_line, example2_d) == 4512


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input"""
    first_line, example1_d = example1
    assert aoc.part2(first_line, example1_d) == 1924


def test_part2_example2(example2):
    """Test part 2 on example input"""
    first_line, example2_d = example2
    assert aoc.part2(first_line, example2_d) == 1924
