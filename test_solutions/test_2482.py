import pytest
from solutions.sol_2482 import Solution

cases = [
    {
        "input": {
            "grid": [[0, 1, 1], [1, 0, 1], [0, 0, 1]],
        },
        "output": [[0, 0, 4], [0, 0, 4], [-2, -2, 2]],
    },
]


@pytest.mark.sol_2482
def test_run():
    for case in cases:
        assert (
            Solution.ones_minus_zeros(
                grid=case["input"]["grid"],
            )
            == case["output"]
        )
