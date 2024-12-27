import pytest
from solutions.sol_1014 import Solution


cases = [
    {
        "input": {"values": [8, 1, 5, 2, 6]},
        "output": 11,
    },
    {
        "input": {"values": [1, 2]},
        "output": 2,
    },
]


@pytest.mark.sol1014
def test_run():
    for case in cases:
        assert (
            Solution.max_score_sightseeing_pair(
                values=case["input"]["values"],
            )
            == case["output"]
        )
