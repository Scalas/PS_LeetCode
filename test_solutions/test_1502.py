import pytest
from solutions.sol_1502 import Solution

cases = [
    {
        "input": {
            "arr": [3, 5, 1],
        },
        "output": True,
    },
    {
        "input": {
            "arr": [1, 2, 4],
        },
        "output": False,
    },
]


@pytest.mark.sol1502
def test_run():
    for case in cases:
        assert (
            round(
                Solution.can_make_arithmetic_progression(
                    arr=case["input"]["arr"],
                ),
                5,
            )
            == case["output"]
        )
