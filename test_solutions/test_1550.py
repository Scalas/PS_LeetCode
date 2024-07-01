import pytest
from solutions.sol_1550 import Solution


cases = [
    {
        "input": {"arr": [2, 6, 4, 1]},
        "output": False,
    },
    {
        "input": {"arr": [1, 2, 34, 3, 4, 5, 7, 23, 12]},
        "output": True,
    },
]


@pytest.mark.sol1550
def test_run():
    for case in cases:
        assert (
            Solution.three_consecutive_odds(
                arr=case["input"]["arr"],
            )
            == case["output"]
        )
