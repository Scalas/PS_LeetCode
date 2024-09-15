import pytest
from solutions.sol_1371 import Solution


cases = [
    {
        "input": {"s": "eleetminicoworoep"},
        "output": 13,
    },
    {
        "input": {"s": "leetcodeisgreat"},
        "output": 5,
    },
    {
        "input": {"s": "bcbcbc"},
        "output": 6,
    },
]


@pytest.mark.sol1371
def test_run():
    for case in cases:
        assert (
            Solution.find_the_longest_substring(
                s=case["input"]["s"],
            )
            == case["output"]
        )
