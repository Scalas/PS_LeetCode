import pytest
from solutions.sol_368 import Solution

cases = [
    {"input": {"nums": [1, 2, 3]}, "output": [1, 2]},
    {"input": {"nums": [1, 2, 4, 8]}, "output": [1, 2, 4, 8]},
    {"input": {"nums": [3, 4, 16, 8]}, "output": [4, 8, 16]},
]


@pytest.mark.sol_368
def test_run():
    for case in cases:
        assert (
            Solution.largest_divisible_subset(nums=case["input"]["nums"])
            == case["output"]
        )
