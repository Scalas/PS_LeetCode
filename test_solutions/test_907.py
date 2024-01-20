import pytest
from solutions.sol_907 import Solution

cases = [
    {"input": {"arr": [3, 1, 2, 4]}, "output": 17},
    {"input": {"arr": [11, 81, 94, 43, 3]}, "output": 444},
    {"input": {"arr": [71, 55, 82, 55]}, "output": 593},
]


@pytest.mark.sol907
def test_run():
    for case in cases:
        assert (
            Solution.sum_subarray_mins(
                arr=case["input"]["arr"],
            )
            == case["output"]
        )
