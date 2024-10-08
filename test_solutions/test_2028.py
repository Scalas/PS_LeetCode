import pytest
from solutions.sol_2028 import Solution


cases = [
    {
        "input": {"rolls": [3, 2, 4, 3], "mean": 4, "n": 2},
        "output": [6, 6],
    },
    {
        "input": {"rolls": [1, 5, 6], "mean": 3, "n": 4},
        "output": [3, 2, 2, 2],
    },
    {
        "input": {"rolls": [1, 2, 3, 4], "mean": 6, "n": 4},
        "output": [],
    },
]


@pytest.mark.sol2028
def test_run():
    for case in cases:
        assert (
            Solution.missing_rolls(
                n=case["input"]["n"],
                mean=case["input"]["mean"],
                rolls=case["input"]["rolls"],
            )
            == case["output"]
        )
