import pytest
from solutions.sol_1578 import Solution

cases = [
    {
        "input": {
            "colors": "abaac",
            "neededTime": [1, 2, 3, 4, 5],
        },
        "output": 3,
    },
    {
        "input": {
            "colors": "abc",
            "neededTime": [1, 2, 3],
        },
        "output": 0,
    },
    {
        "input": {
            "colors": "aabaa",
            "neededTime": [1, 2, 3, 4, 1],
        },
        "output": 2,
    },
]


@pytest.mark.sol1578
def test_run():
    for case in cases:
        assert (
            Solution.min_cost(
                colors=case["input"]["colors"],
                neededTime=case["input"]["neededTime"],
            )
            == case["output"]
        )
