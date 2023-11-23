import pytest
from solutions.sol_1630 import Solution

cases = [
    {
        "input": {
            "nums": [4, 6, 5, 9, 3, 7],
            "l": [0, 0, 2],
            "r": [2, 3, 5],
        },
        "output": [True, False, True],
    },
    {
        "input": {
            "nums": [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10],
            "l": [0, 1, 6, 4, 8, 7],
            "r": [4, 4, 9, 7, 9, 10],
        },
        "output": [False, True, False, False, True, True],
    },
]


@pytest.mark.sol1630
def test_run():
    for case in cases:
        assert (
            Solution.check_arithmetic_subarrays(
                nums=case["input"]["nums"],
                l=case["input"]["l"],
                r=case["input"]["r"],
            )
            == case["output"]
        )
