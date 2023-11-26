import pytest

from solutions.sol_1727 import Solution

cases = [
    {
        "input": {
            "matrix": [[0, 0, 1], [1, 1, 1], [1, 0, 1]],
        },
        "output": 4,
    },
    {
        "input": {
            "matrix": [[1, 0, 1, 0, 1]],
        },
        "output": 3,
    },
    {
        "input": {
            "matrix": [[1, 1, 0], [1, 0, 1]],
        },
        "output": 2,
    },
]


@pytest.mark.sol1727
def test_run():
    for case in cases:
        assert (
            Solution.largest_sub_matrix(
                matrix=case["input"]["matrix"],
            )
            == case["output"]
        )
