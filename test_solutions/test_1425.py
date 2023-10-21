import pytest
from solutions.sol_1425 import Solution

cases = [
    {
        "input": {
            "nums": [10, 2, -10, 5, 20],
            "k": 2,
        },
        "output": 37,
    },
    {
        "input": {
            "nums": [-1, -2, -3],
            "k": 1,
        },
        "output": -1,
    },
    {
        "input": {
            "nums": [10, -2, -10, -5, 20],
            "k": 2,
        },
        "output": 23,
    },
]


@pytest.mark.sol1425
def test_run():
    for case in cases:
        assert (
            Solution.constrained_subset_sum(
                nums=case["input"]["nums"], k=case["input"]["k"]
            )
            == case["output"]
        )
