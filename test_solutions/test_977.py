import pytest
from solutions.sol_977 import Solution

cases = [
    {"input": {"nums": [-4, -1, 0, 3, 10]}, "output": [0, 1, 9, 16, 100]},
    {"input": {"nums": [-7, -3, 2, 3, 11]}, "output": [4, 9, 9, 49, 121]},
]


@pytest.mark.sol977
def test_run():
    for case in cases:
        assert Solution.sorted_squares(nums=case["input"]["nums"]) == case["output"]
