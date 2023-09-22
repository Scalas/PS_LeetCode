import pytest
from solutions.sol_392 import Solution

cases = [
    {
        "input": {
            "s": "abc",
            "t": "ahbgdc",
        },
        "output": True,
    },
    {
        "input": {
            "s": "axc",
            "t": "ahbgdc",
        },
        "output": False,
    },
]


@pytest.mark.sol392
def test_run():
    for case in cases:
        assert (
            Solution.is_subsequence(
                s=case["input"]["s"],
                t=case["input"]["t"],
            )
            == case["output"]
        )
