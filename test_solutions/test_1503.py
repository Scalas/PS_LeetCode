import pytest
from solutions.sol_1503 import Solution

cases = [
    {
        "input": {
            "n": 4,
            "left": [4, 3],
            "right": [0, 1],
        },
        "output": 4,
    },
    {
        "input": {
            "n": 7,
            "left": [0, 1, 2, 3, 4, 5, 6, 7],
            "right": [],
        },
        "output": 7,
    },
    {
        "input": {
            "n": 7,
            "left": [],
            "right": [0, 1, 2, 3, 4, 5, 6, 7],
        },
        "output": 7,
    },
]


@pytest.mark.sol1503
def test_run():
    for case in cases:
        assert (
            Solution.get_last_moment(
                n=case["input"]["n"],
                left=case["input"]["left"],
                right=case["input"]["right"],
            )
            == case["output"]
        )
