import pytest
from solutions.sol_859 import Solution

cases = [
    {
        "input": {
            "s": "ab",
            "goal": "ba",
        },
        "output": True,
    },
    {
        "input": {
            "s": "ab",
            "goal": "ab",
        },
        "output": False,
    },
    {
        "input": {
            "s": "aa",
            "goal": "aa",
        },
        "output": True,
    },
    {
        "input": {
            "s": "ab",
            "goal": "babb",
        },
        "output": False,
    },
]


@pytest.mark.sol859
def test_run():
    for case in cases:
        assert (
            Solution.buddy_strings(
                s=case["input"]["s"],
                goal=case["input"]["goal"],
            )
            == case["output"]
        )
