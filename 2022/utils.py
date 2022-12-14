import __main__
from os import path
from typing import Iterable, Callable


Input = Iterable[str]


def stripNewLine(s: str) -> str:
    return s.strip("\n")


def readInput(
    filename: str, folder: str | None = None, mapFunc: Callable | None = None
) -> Input:
    if mapFunc is None:
        mapFunc = stripNewLine
    if folder is None:
        folder = path.dirname(path.realpath(__main__.__file__))
    with open(path.join(folder, filename), "r") as file:
        yield from map(mapFunc, file)
