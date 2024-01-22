import pytest

from solutions.sol_645 import Solution

cases = [
    {"input": {"nums": [1, 2, 2, 4]}, "output": [2, 3]},
    {"input": {"nums": [1, 1]}, "output": [1, 2]},
]


@pytest.mark.sol_645
def test_run():
    for case in cases:
        assert (
            Solution.find_error_nums(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
