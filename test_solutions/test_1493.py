import pytest
from solutions.sol_1493 import Solution

cases = [
    {
        "input": {
            "nums": [1, 1, 0, 1],
        },
        "output": 3,
    },
    {
        "input": {
            "nums": [0, 1, 1, 1, 0, 1, 1, 0, 1],
        },
        "output": 5,
    },
    {
        "input": {
            "nums": [1, 1, 1],
        },
        "output": 2,
    },
]


@pytest.mark.sol1493
def test_run():
    for case in cases:
        assert (
            round(
                Solution.longest_subarray(
                    nums=case["input"]["nums"],
                ),
                5,
            )
            == case["output"]
        )
