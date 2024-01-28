import pytest
from solutions.sol_1074 import Solution

cases = [
    {
        "input": {
            "matrix": [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
            "target": 0,
        },
        "output": 4,
    },
    {
        "input": {
            "matrix": [[1, -1], [-1, 1]],
            "target": 0,
        },
        "output": 5,
    },
    {
        "input": {
            "matrix": [[904]],
            "target": 0,
        },
        "output": 0,
    },
]


@pytest.mark.sol1074
def test_run():
    for case in cases:
        assert (
            Solution.num_submatrix_sum_target(
                matrix=case["input"]["matrix"],
                target=case["input"]["target"],
            )
            == case["output"]
        )
