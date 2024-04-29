import pytest
from solutions.sol_2997 import Solution

cases = [
    {
        "input": {"nums": [2, 1, 3, 4], "k": 1},
        "output": 2,
    },
    {
        "input": {"nums": [2, 0, 2, 0], "k": 0},
        "output": 0,
    },
]


@pytest.mark.sol_2971
def test_run():
    for case in cases:
        assert (
            Solution.min_operations(nums=case["input"]["nums"], k=case["input"]["k"])
            == case["output"]
        )
