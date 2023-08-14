import pytest
from solutions.sol_712 import Solution

cases = [
    {
        "input": {
            "s1": "sea",
            "s2": "eat",
        },
        "output": 231,
    },
    {
        "input": {
            "s1": "delete",
            "s2": "leet",
        },
        "output": 403,
    },
]


@pytest.mark.sol_712
def test_run():
    for case in cases:
        assert (
            Solution.minimum_delete_sum(
                s1=case["input"]["s1"],
                s2=case["input"]["s2"],
            )
            == case["output"]
        )
