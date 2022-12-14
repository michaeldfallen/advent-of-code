import enum
from typing import Iterable, NamedTuple
from utils import Input, readInput


class Throw(enum.Enum):
    Rock: "Throw" = 1
    Paper: "Throw" = 2
    Scissors: "Throw" = 3

    def parse(char: str) -> "Throw":
        if char == "A" or char == "X":
            return Throw.Rock
        if char == "B" or char == "Y":
            return Throw.Paper
        if char == "C" or char == "Z":
            return Throw.Scissors
        raise ValueError

    def to_produce_result(their: "Throw", result: "Result") -> "Throw":
        if their == Throw.Rock:
            if result == Result.Win:
                return Throw.Paper
            if result == Result.Draw:
                return Throw.Rock
            if result == Result.Loss:
                return Throw.Scissors
        if their == Throw.Paper:
            if result == Result.Win:
                return Throw.Scissors
            if result == Result.Draw:
                return Throw.Paper
            if result == Result.Loss:
                return Throw.Rock
        if their == Throw.Scissors:
            if result == Result.Win:
                return Throw.Rock
            if result == Result.Draw:
                return Throw.Scissors
            if result == Result.Loss:
                return Throw.Paper
        raise ValueError


class Result(enum.Enum):
    Win: "Result" = 6
    Draw: "Result" = 3
    Loss: "Result" = 0

    def create(my: Throw, their: Throw) -> "Result":
        if my == Throw.Rock:
            if their == Throw.Rock:
                return Result.Draw
            if their == Throw.Paper:
                return Result.Loss
            if their == Throw.Scissors:
                return Result.Win
        if my == Throw.Paper:
            if their == Throw.Rock:
                return Result.Win
            if their == Throw.Paper:
                return Result.Draw
            if their == Throw.Scissors:
                return Result.Loss
        if my == Throw.Scissors:
            if their == Throw.Rock:
                return Result.Loss
            if their == Throw.Paper:
                return Result.Win
            if their == Throw.Scissors:
                return Result.Draw
        raise ValueError

    def parse(s: str) -> "Result":
        if s == "X":
            return Result.Loss
        if s == "Y":
            return Result.Draw
        if s == "Z":
            return Result.Win
        raise ValueError


class Round(NamedTuple):
    my: Throw
    their: Throw


def parseLine(line: str) -> Round:
    [theirChar, myChar] = line.split(" ")
    return Round(my=Throw.parse(myChar), their=Throw.parse(theirChar))


def parse(input: Input) -> Iterable[Round]:
    return map(parseLine, input)


def score_round(round: Round) -> int:
    result = Result.create(round.my, round.their)
    return round.my.value + result.value


if __name__ == "__main__":
    input = readInput("input_part1.txt")
    rounds = parse(input)
    total = sum(map(score_round, rounds))
    print(f"Total score: {total}")
