import pytest
from solutions.sol_1395 import Solution


cases = [
    {
        "input": {"rating": [2, 5, 3, 4, 1]},
        "output": 3,
    },
    {
        "input": {"rating": [2, 1, 3]},
        "output": 0,
    },
    {
        "input": {"rating": [1, 2, 3, 4]},
        "output": 4,
    },
]


@pytest.mark.sol1395
def test_run():
    for case in cases:
        assert (
            Solution.num_teams(
                rating=case["input"]["rating"],
            )
            == case["output"]
        )
