import pytest
from solutions.sol_300 import Solution

cases = [
    {"input": {"nums": [10, 9, 2, 5, 3, 7, 101, 18]}, "output": 4},
    {"input": {"nums": [0, 1, 0, 3, 2, 3]}, "output": 4},
    {"input": {"nums": [7, 7, 7, 7, 7, 7, 7]}, "output": 1},
]


@pytest.mark.sol_300
def test_run():
    for case in cases:
        assert (
            Solution.length_of_lis(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
