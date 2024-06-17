import pytest
from solutions.sol_330 import Solution

cases = [
    {"input": {"nums": [1, 3], "n": 6}, "output": 1},
    {"input": {"nums": [1, 5, 10], "n": 20}, "output": 2},
    {"input": {"nums": [1, 2, 2], "n": 5}, "output": 0},
]


@pytest.mark.sol_330
def test_run():
    for case in cases:
        assert (
            Solution.min_patches(nums=case["input"]["nums"], n=case["input"]["n"])
            == case["output"]
        )
