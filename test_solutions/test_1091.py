import pytest
from solutions.sol_1091 import Solution

cases = [
    {
        "input": {
            "grid": [[0, 1], [1, 0]],
        },
        "output": 2,
    },
    {
        "input": {
            "grid": [[0, 0, 0], [1, 1, 0], [1, 1, 0]],
        },
        "output": 4,
    },
    {
        "input": {
            "grid": [[1, 0, 0], [1, 1, 0], [1, 1, 0]],
        },
        "output": -1,
    },
    {
        "input": {
            "grid": [[0, 0, 0], [1, 1, 0], [1, 1, 1]],
        },
        "output": -1,
    },
]


@pytest.mark.sol1091
def test_run():
    for case in cases:
        assert (
            Solution.shortest_path_binary_matrix(
                grid=case["input"]["grid"],
            )
            == case["output"]
        )
