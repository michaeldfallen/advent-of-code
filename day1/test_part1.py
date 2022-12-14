import pytest
from part1 import parseInput, calculate


def test_parseInput():
    input = [
        "1000",
        "2000",
        "3000",
        "",
        "4000",
        "",
        "5000",
        "6000",
        "",
        "7000",
        "8000",
        "9000",
        "",
        "10000",
    ]
    grouped = parseInput(input)
    assert grouped == [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
    ]


def test_parseInput_badFormat():
    input = [1, 2, 3, "", None]
    with pytest.raises(TypeError):
        parseInput(input)


def test_calculate():
    input = [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
    ]
    largest = calculate(input)
    assert largest == 24000
