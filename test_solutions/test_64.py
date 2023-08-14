import pytest
from solutions.sol_64 import Solution

cases = [
    {
        "input": {
            "grid": [[1, 3, 1], [1, 5, 1], [4, 2, 1]],
        },
        "output": 7,
    },
    {
        "input": {
            "grid": [[1, 2, 3], [4, 5, 6]],
        },
        "output": 12,
    },
]


@pytest.mark.sol64
def test_run():
    for case in cases:
        assert (
            Solution.min_path_sum(
                grid=case["input"]["grid"],
            )
            == case["output"]
        )
