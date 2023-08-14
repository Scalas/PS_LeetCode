import pytest
from solutions.sol_1572 import Solution

cases = [
    {
        "input": {
            "mat": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        },
        "output": 25,
    },
    {
        "input": {"mat": [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]},
        "output": 8,
    },
    {
        "input": {
            "mat": [[5]],
        },
        "output": 5,
    },
]


@pytest.mark.sol1572
def test_run():
    for case in cases:
        assert (
            Solution.diagonal_sum(
                mat=case["input"]["mat"],
            )
            == case["output"]
        )
