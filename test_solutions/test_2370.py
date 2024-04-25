import pytest
from solutions.sol_2370 import Solution

cases = [
    {
        "input": {
            "s": "acfgbd",
            "k": 2,
        },
        "output": 4,
    },
    {
        "input": {
            "s": "abcd",
            "k": 3,
        },
        "output": 4,
    },
    {
        "input": {
            "s": "eduktdb",
            "k": 15,
        },
        "output": 5,
    },
]


@pytest.mark.sol_2370
def test_run():
    for case in cases:
        assert (
            Solution.longest_ideal_string(
                s=case["input"]["s"],
                k=case["input"]["k"],
            )
            == case["output"]
        )
