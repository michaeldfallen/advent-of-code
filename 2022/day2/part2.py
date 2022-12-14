from typing import Iterable
from utils import Input, readInput
from .part1 import Round, Result, Throw, score_round


def parseLine(line: str) -> Round:
    [theirChar, resultChar] = line.split(" ")
    their_throw = Throw.parse(theirChar)
    result = Result.parse(resultChar)
    return Round(
        my=Throw.to_produce_result(their_throw, result), their=their_throw
    )


def parse(input: Input) -> Iterable[Round]:
    return map(parseLine, input)


if __name__ == "__main__":
    input = readInput("input_part1.txt")
    rounds = parse(input)
    total = sum(map(score_round, rounds))
    print(f"Total score: {total}")
