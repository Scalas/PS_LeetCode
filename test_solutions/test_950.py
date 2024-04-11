import pytest
from solutions.sol_950 import Solution

cases = [
    {
        "input": {
            "deck": [17, 13, 11, 2, 3, 5, 7],
        },
        "output": [2, 13, 3, 11, 5, 17, 7],
    },
    {
        "input": {
            "deck": [1, 1000],
        },
        "output": [1, 1000],
    },
    {
        "input": {
            "deck": [17, 11, 2, 3, 5, 7],
        },
        "output": [2, 7, 3, 17, 5, 11],
    },
    {
        "input": {
            "deck": [1],
        },
        "output": [1],
    },
    {
        "input": {
            "deck": [1, 2, 3, 4, 5, 6, 7, 8, 9],
        },
        "output": [1, 9, 2, 6, 3, 8, 4, 7, 5],
    },
]


@pytest.mark.sol950
def test_run():
    for case in cases:
        assert (
            Solution.deck_revealed_increasing(
                deck=case["input"]["deck"],
            )
            == case["output"]
        )
