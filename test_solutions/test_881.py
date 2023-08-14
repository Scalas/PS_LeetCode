import pytest
from solutions.sol_881 import Solution

cases = [
    {
        "input": {
            "people": [1, 2],
            "limit": 3,
        },
        "output": 1,
    },
    {
        "input": {
            "people": [3, 2, 2, 1],
            "limit": 3,
        },
        "output": 3,
    },
    {
        "input": {
            "people": [3, 5, 3, 4],
            "limit": 5,
        },
        "output": 4,
    },
]


@pytest.mark.sol881
def test_run():
    for case in cases:
        assert (
            Solution.num_rescue_boats(
                people=case["input"]["people"], limit=case["input"]["limit"]
            )
            == case["output"]
        )
