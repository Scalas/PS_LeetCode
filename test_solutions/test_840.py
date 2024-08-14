import pytest
from solutions.sol_840 import Solution


cases = [
    {
        "input": {"grid": [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]},
        "output": 1,
    },
    {
        "input": {"grid": [[8]]},
        "output": 0,
    },
]


@pytest.mark.sol840
def test_run():
    for case in cases:
        assert (
            Solution.num_magic_squares_inside(
                grid=case["input"]["grid"],
            )
            == case["output"]
        )
