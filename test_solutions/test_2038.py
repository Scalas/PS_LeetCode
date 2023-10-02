import pytest
from solutions.sol_2038 import Solution

cases = [
    {
        "input": {
            "colors": "AAABABB",
        },
        "output": True,
    },
    {
        "input": {
            "colors": "AA",
        },
        "output": False,
    },
    {
        "input": {
            "colors": "ABBBBBBBAAA",
        },
        "output": False,
    },
]


@pytest.mark.sol_2038
def test_run():
    for case in cases:
        assert (
            Solution.winner_of_game(
                colors=case["input"]["colors"],
            )
            == case["output"]
        )
