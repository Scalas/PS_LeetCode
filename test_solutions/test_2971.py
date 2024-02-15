import pytest
from solutions.sol_2971 import Solution

cases = [
    {
        "input": {"nums": [5, 5, 5]},
        "output": 15,
    },
    {
        "input": {"nums": [1, 12, 1, 2, 5, 50, 3]},
        "output": 12,
    },
    {
        "input": {"nums": [5, 5, 50]},
        "output": -1,
    },
]


@pytest.mark.sol_2971
def test_run():
    for case in cases:
        assert Solution.largest_perimeter(nums=case["input"]["nums"]) == case["output"]
