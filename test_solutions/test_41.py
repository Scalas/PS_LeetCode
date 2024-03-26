import pytest
from solutions.sol_41 import Solution

cases = [
    {"input": {"nums": [1, 2, 0]}, "output": 3},
    {"input": {"nums": [3, 4, -1, 1]}, "output": 2},
    {"input": {"nums": [7, 8, 9, 11, 12]}, "output": 1},
]


@pytest.mark.sol41
def test_run():
    for case in cases:
        assert (
            Solution.first_missing_positive(nums=case["input"]["nums"])
            == case["output"]
        )
