import pytest
from solutions.sol_63 import Solution

cases = [
    {
        "input": {
            "obstacle_grid": [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        },
        "output": 2,
    },
    {
        "input": {
            "obstacle_grid": [[0, 1], [0, 0]],
        },
        "output": 1,
    },
]


@pytest.mark.sol63
def test_run():
    for case in cases:
        assert (
            Solution.unique_paths_with_obstacles(
                obstacle_grid=case["input"]["obstacle_grid"],
            )
            == case["output"]
        )
