import pytest
from solutions.sol_2706 import Solution

cases = [
    {
        "input": {
            "prices": [1, 2, 2],
            "money": 3,
        },
        "output": 0,
    },
    {
        "input": {
            "prices": [3, 2, 3],
            "money": 3,
        },
        "output": 3,
    },
    {
        "input": {
            "prices": [98, 54, 6, 34, 66, 63, 52, 39],
            "money": 62,
        },
        "output": 22,
    },
]


@pytest.mark.sol_2706
def test_run():
    for case in cases:
        assert (
            Solution.buy_choco(
                prices=case["input"]["prices"], money=case["input"]["money"]
            )
            == case["output"]
        )
