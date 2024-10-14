import pytest
from solutions.sol_2491 import Solution


cases = [
    {
        "input": {"skill": [3, 2, 5, 1, 3, 4]},
        "output": 22,
    },
    {
        "input": {"skill": [3, 4]},
        "output": 12,
    },
    {
        "input": {"skill": [1, 1, 2, 3]},
        "output": -1,
    },
]


@pytest.mark.sol2491
def test_run():
    for case in cases:
        assert (
            Solution.divide_players(
                skill=case["input"]["skill"],
            )
            == case["output"]
        )
