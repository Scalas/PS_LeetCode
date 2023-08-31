import pytest
from solutions.sol_1326 import Solution

cases = [
    {
        "input": {
            "n": 5,
            "ranges": [3, 4, 1, 1, 0, 0],
        },
        "output": 1,
    },
    {
        "input": {
            "n": 3,
            "ranges": [0, 0, 0, 0],
        },
        "output": -1,
    },
    {
        "input": {
            "n": 12,
            "ranges": [1, 0, 4, 0, 4, 1, 4, 3, 1, 1, 1, 2, 1],
        },
        "output": 3,
    },
]


@pytest.mark.sol1326
def test_run():
    for case in cases:
        assert (
                Solution.min_taps(
                    n=case["input"]["n"],
                    ranges=case["input"]["ranges"],
                )
                == case["output"]
        )
