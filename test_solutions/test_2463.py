import pytest
from solutions.sol_2463 import Solution


cases = [
    {
        "input": {"robot": [0, 4, 6], "factory": [[2, 2], [6, 2]]},
        "output": 4,
    },
    {
        "input": {"robot": [1, -1], "factory": [[-2, 1], [2, 1]]},
        "output": 2,
    },
]


@pytest.mark.sol2463
def test_run():
    for case in cases:
        assert (
            Solution.minimum_total_distance(
                factory=case["input"]["factory"],
                robot=case["input"]["robot"],
            )
            == case["output"]
        )
