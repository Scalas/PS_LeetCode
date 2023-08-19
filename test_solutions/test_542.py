import pytest
from solutions.sol_542 import Solution

cases = [
    {
        "input": {
            "mat": [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        },
        "output": [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
    },
    {
        "input": {
            "mat": [[0, 0, 0], [0, 1, 0], [1, 1, 1]],
        },
        "output": [[0, 0, 0], [0, 1, 0], [1, 2, 1]],
    },
]


@pytest.mark.sol_542
def test_run():
    for case in cases:
        assert (
            Solution.update_matrix(
                mat=case["input"]["mat"],
            )
            == case["output"]
        )
