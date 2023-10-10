import pytest
from solutions.sol_2009 import Solution

cases = [
    {
        "input": {
            "nums": [4, 2, 5, 3],
        },
        "output": 0,
    },
    {
        "input": {
            "nums": [1, 2, 3, 5, 6],
        },
        "output": 1,
    },
    {
        "input": {
            "nums": [1, 10, 100, 1000],
        },
        "output": 3,
    },
]


@pytest.mark.sol_2009
def test_run():
    for case in cases:
        assert (
            Solution.min_operations(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
