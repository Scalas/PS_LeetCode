import pytest
from solutions.sol_523 import Solution

cases = [
    {"input": {"nums": [23, 2, 4, 6, 7], "k": 6}, "output": True},
    {"input": {"nums": [23, 2, 6, 4, 7], "k": 6}, "output": True},
    {"input": {"nums": [23, 2, 6, 4, 7], "k": 13}, "output": False},
]


@pytest.mark.sol_523
def test_run():
    for case in cases:
        assert (
            Solution.check_subarray_sum(
                nums=case["input"]["nums"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
