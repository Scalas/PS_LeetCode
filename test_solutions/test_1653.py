import pytest
from solutions.sol_1653 import Solution


cases = [
    {
        "input": {"s": "aababbab"},
        "output": 2,
    },
    {
        "input": {"s": "bbaaaaabb"},
        "output": 2,
    },
]


@pytest.mark.sol1653
def test_run():
    for case in cases:
        assert (
            Solution.minimum_deletions(
                s=case["input"]["s"],
            )
            == case["output"]
        )
