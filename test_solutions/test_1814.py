import pytest
from solutions.sol_1814 import Solution

cases = [
    {
        "input": {
            "nums": [42, 11, 1, 97],
        },
        "output": 2,
    },
    {
        "input": {
            "nums": [13, 10, 35, 24, 76],
        },
        "output": 4,
    },
]


@pytest.mark.sol1814
def test_run():
    for case in cases:
        assert (
            Solution.count_nice_pairs(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
