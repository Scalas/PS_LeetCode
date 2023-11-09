import pytest
from solutions.sol_1759 import Solution

cases = [
    {
        "input": {
            "s": "abbcccaa",
        },
        "output": 13,
    },
    {
        "input": {
            "s": "xy",
        },
        "output": 2,
    },
    {
        "input": {
            "s": "zzzzz",
        },
        "output": 15,
    },
]


@pytest.mark.sol_1759
def test_run():
    for case in cases:
        assert (
            Solution.count_homogenous(
                s=case["input"]["s"],
            )
            == case["output"]
        )
