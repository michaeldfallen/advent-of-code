from utils import readInput
from .part1 import parseInput, Inventory


def calculate(inventories: Inventory) -> int:
    sums = list(map(sum, inventories))

    first_largest = max(sums)
    sums.remove(first_largest)
    second_largest = max(sums)
    sums.remove(second_largest)
    third_largest = max(sums)

    return sum([first_largest, second_largest, third_largest])


if __name__ == "__main__":
    input = readInput("input_part1.txt")
    inventories = parseInput(input)
    total = calculate(inventories)

    print(f"total of top 3 = {total}")
