import pytest
from solutions.sol_1535 import Solution

cases = [
    {
        "input": {
            "arr": [2, 1, 3, 5, 4, 6, 7],
            "k": 2,
        },
        "output": 5,
    },
    {
        "input": {
            "arr": [3, 2, 1],
            "k": 10,
        },
        "output": 3,
    },
    {
        "input": {
            "arr": [1, 9, 8, 2, 3, 7, 6, 4, 5],
            "k": 7,
        },
        "output": 9,
    },
    {
        "input": {
            "arr": [1, 25, 35, 42, 68, 70],
            "k": 1,
        },
        "output": 25,
    },
]


@pytest.mark.sol1535
def test_run():
    for case in cases:
        assert (
            Solution.get_winner(
                arr=case["input"]["arr"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
