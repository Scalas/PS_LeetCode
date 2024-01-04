import pytest
from solutions.sol_2870 import Solution

cases = [
    {
        "input": {
            "nums": [2, 3, 3, 2, 2, 4, 2, 3, 4],
        },
        "output": 4,
    },
    {
        "input": {
            "nums": [2, 1, 2, 2, 3, 3],
        },
        "output": -1,
    },
]


@pytest.mark.sol_2870
def test_run():
    for case in cases:
        assert Solution.min_operations(nums=case["input"]["nums"]) == case["output"]
