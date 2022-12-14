from .part1 import Round, Throw, parse, score_round


def test_parse():
    input = [
        "A Y",
        "B X",
        "C Z",
    ]
    rounds = list(parse(input))
    assert rounds == [
        Round(their=Throw.Rock, my=Throw.Paper),
        Round(their=Throw.Paper, my=Throw.Rock),
        Round(their=Throw.Scissors, my=Throw.Scissors),
    ]


def test_score_round():
    assert score_round(Round(their=Throw.Rock, my=Throw.Paper)) == 8
    assert score_round(Round(their=Throw.Paper, my=Throw.Rock)) == 1
    assert score_round(Round(their=Throw.Scissors, my=Throw.Scissors)) == 6
