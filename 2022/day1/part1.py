from typing import Iterable
from utils import readInput


Inventory = Iterable[int]
Input = Iterable[str]


def parseInput(lines: Inventory) -> Iterable[Inventory]:
    parsed = []
    current = []
    for line in lines:
        if line == "":
            parsed.append(current)
            current = []
        else:
            current.append(int(line))
    parsed.append(current)
    return parsed


def calculate(inventories: Inventory) -> int:
    sums = map(sum, inventories)
    largest = max(sums)
    return largest


if __name__ == "__main__":
    input = readInput("input_part1.txt")
    inventories = parseInput(input)
    largest = calculate(inventories)
    print(f"largest calories = {largest}")
