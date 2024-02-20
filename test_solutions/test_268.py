import pytest
from solutions.sol_268 import Solution

cases = [
    {
        "input": {
            "nums": [3, 0, 1],
        },
        "output": 2,
    },
    {
        "input": {
            "nums": [0, 1],
        },
        "output": 2,
    },
    {
        "input": {
            "nums": [9, 6, 4, 2, 3, 5, 7, 0, 1],
        },
        "output": 8,
    },
]


@pytest.mark.sol268
def test_run():
    for case in cases:
        assert (
            Solution.missing_number(
                nums=case["input"]["nums"],
            )
            == case["output"]
        )
