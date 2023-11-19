import pytest
from solutions.sol_1887 import Solution

cases = [
    {
        "input": {
            "nums": [5, 1, 3],
        },
        "output": 3,
    },
    {
        "input": {
            "nums": [1, 1, 1],
        },
        "output": 0,
    },
    {
        "input": {
            "nums": [1, 1, 2, 2, 3],
        },
        "output": 4,
    },
]


@pytest.mark.sol1887
def test_run():
    for case in cases:
        assert (
            Solution.reduction_operations(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
