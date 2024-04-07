import pytest
from solutions.sol_678 import Solution

cases = [
    {
        "input": {
            "s": "()",
        },
        "output": True,
    },
    {
        "input": {
            "s": "(*)",
        },
        "output": True,
    },
    {
        "input": {
            "s": "(*))",
        },
        "output": True,
    },
]


@pytest.mark.sol_678
def test_run():
    for case in cases:
        assert (
            Solution.check_valid_string(
                s=case["input"]["s"],
            )
            == case["output"]
        )
