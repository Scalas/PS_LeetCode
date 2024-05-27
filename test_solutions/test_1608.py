import pytest
from solutions.sol_1608 import Solution

cases = [
    {
        "input": {
            "nums": [3, 5],
        },
        "output": 2,
    },
    {
        "input": {
            "nums": [0, 0],
        },
        "output": -1,
    },
    {
        "input": {
            "nums": [0, 4, 3, 0, 4],
        },
        "output": 3,
    },
]


@pytest.mark.sol1608
def test_run():
    for case in cases:
        assert Solution.special_array(nums=case["input"]["nums"]) == case["output"]
