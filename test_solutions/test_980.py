import pytest
from solutions.sol_980 import Solution

cases = [
    {
        "input": {
            "grid": [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]],
        },
        "output": 2,
    },
    {
        "input": {
            "grid": [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]],
        },
        "output": 4,
    },
    {
        "input": {
            "grid": [[0, 1], [2, 0]],
        },
        "output": 0,
    },
]


@pytest.mark.sol980
def test_run():
    for case in cases:
        assert Solution.unique_paths_3(grid=case["input"]["grid"]) == case["output"]
