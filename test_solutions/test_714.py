import pytest
from solutions.sol_714 import Solution

cases = [
    {
        "input": {"prices": [1, 3, 2, 8, 4, 9], "fee": 2},
        "output": 8,
    },
    {
        "input": {"prices": [1, 3, 7, 5, 10, 3], "fee": 3},
        "output": 6,
    },
]


@pytest.mark.sol_714
def test_run():
    for case in cases:
        assert (
            Solution.max_profit(
                prices=case["input"]["prices"],
                fee=case["input"]["fee"],
            )
            == case["output"]
        )
