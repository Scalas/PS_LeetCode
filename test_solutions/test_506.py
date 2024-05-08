import pytest
from solutions.sol_506 import Solution

cases = [
    {
        "input": {
            "score": [5, 4, 3, 2, 1],
        },
        "output": ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"],
    },
    {
        "input": {
            "score": [10, 3, 8, 9, 4],
        },
        "output": ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"],
    },
]


@pytest.mark.sol_506
def test_run():
    for case in cases:
        assert (
            Solution.find_relative_ranks(
                score=case["input"]["score"],
            )
            == case["output"]
        )
