import pytest
from solutions.sol_1568 import Solution


cases = [
    {
        "input": {"grid": [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]},
        "output": 2,
    },
    {
        "input": {"grid": [[1, 1]]},
        "output": 2,
    },
    {
        "input": {"grid": [[1, 0], [0, 1]]},
        "output": 0,
    },
]


@pytest.mark.sol1568
def test_run():
    for case in cases:
        assert (
            Solution.min_days(
                grid=case["input"]["grid"],
            )
            == case["output"]
        )
