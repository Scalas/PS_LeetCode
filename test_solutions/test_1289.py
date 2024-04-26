import pytest
from solutions.sol_1289 import Solution

cases = [
    {
        "input": {
            "grid": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        },
        "output": 13,
    },
    {
        "input": {
            "grid": [[7]],
        },
        "output": 7,
    },
]


@pytest.mark.sol1289
def test_run():
    for case in cases:
        assert (
            Solution.min_falling_path_sum(
                grid=case["input"]["grid"],
            )
            == case["output"]
        )
