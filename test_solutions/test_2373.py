import pytest
from solutions.sol_2373 import Solution

cases = [
    {
        "input": {
            "grid": [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]],
        },
        "output": [[9, 9], [8, 6]],
    },
    {
        "input": {
            "grid": [
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 2, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
            ],
        },
        "output": [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
    },
]


@pytest.mark.sol_2373
def test_run():
    for case in cases:
        assert (
            Solution.largest_local(
                grid=case["input"]["grid"],
            )
            == case["output"]
        )
