import pytest
from solutions.sol_875 import Solution

cases = [
    {
        "input": {
            "piles": [3, 6, 7, 11],
            "h": 8,
        },
        "output": 4,
    },
    {
        "input": {
            "piles": [30, 11, 23, 4, 20],
            "h": 5,
        },
        "output": 30,
    },
    {
        "input": {
            "piles": [30, 11, 23, 4, 20],
            "h": 6,
        },
        "output": 23,
    },
]


@pytest.mark.sol875
def test_run():
    for case in cases:
        assert (
            Solution.min_eating_speed(
                piles=case["input"]["piles"], h=case["input"]["h"]
            )
            == case["output"]
        )
