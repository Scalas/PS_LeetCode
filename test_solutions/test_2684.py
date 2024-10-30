import pytest
from solutions.sol_2684 import Solution


cases = [
    {
        "input": {"grid": [[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]},
        "output": 3,
    },
    {
        "input": {"grid": [[3, 2, 4], [2, 1, 9], [1, 1, 7]]},
        "output": 0,
    },
]


@pytest.mark.sol2684
def test_run():
    for case in cases:
        assert (
            Solution.max_moves(
                grid=case["input"]["grid"],
            )
            == case["output"]
        )
