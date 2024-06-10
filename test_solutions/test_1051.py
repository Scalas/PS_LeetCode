import pytest
from solutions.sol_1051 import Solution

cases = [
    {
        "input": {
            "heights": [1, 1, 4, 2, 1, 3],
        },
        "output": 3,
    },
    {
        "input": {
            "heights": [5, 1, 2, 3, 4],
        },
        "output": 5,
    },
    {
        "input": {
            "heights": [1, 2, 3, 4, 5],
        },
        "output": 0,
    },
]


@pytest.mark.sol1051
def test_run():
    for case in cases:
        assert (
            Solution.height_checker(
                heights=case["input"]["heights"],
            )
            == case["output"]
        )
