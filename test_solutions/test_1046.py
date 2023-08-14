import pytest
from solutions.sol_1046 import Solution

cases = [
    {
        "input": {
            "stones": [2, 7, 4, 1, 8, 1],
        },
        "output": 1,
    },
    {
        "input": {
            "stones": [1],
        },
        "output": 1,
    },
]


@pytest.mark.sol1046
def test_run():
    for case in cases:
        assert (
            Solution.last_stone_weight(
                stones=case["input"]["stones"],
            )
            == case["output"]
        )
