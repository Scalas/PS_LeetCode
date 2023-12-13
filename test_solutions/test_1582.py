import pytest
from solutions.sol_1582 import Solution

cases = [
    {
        "input": {
            "mat": [[1, 0, 0], [0, 0, 1], [1, 0, 0]],
        },
        "output": 1,
    },
    {
        "input": {
            "mat": [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        },
        "output": 3,
    },
]


@pytest.mark.sol1582
def test_run():
    for case in cases:
        assert (
            Solution.num_special(
                mat=case["input"]["mat"],
            )
            == case["output"]
        )
