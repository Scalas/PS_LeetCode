import pytest
from solutions.sol_1758 import Solution

cases = [
    {
        "input": {
            "s": "0100",
        },
        "output": 1,
    },
    {
        "input": {
            "s": "10",
        },
        "output": 0,
    },
    {
        "input": {
            "s": "1111",
        },
        "output": 2,
    },
]


@pytest.mark.sol_1758
def test_run():
    for case in cases:
        assert (
            Solution.min_operations(
                s=case["input"]["s"],
            )
            == case["output"]
        )
