import pytest
from solutions.sol_1631 import Solution

cases = [
    {
        "input": {
            "heights": [[1, 2, 2], [3, 8, 2], [5, 3, 5]],
        },
        "output": 2,
    },
    {
        "input": {
            "heights": [[1, 2, 3], [3, 8, 4], [5, 3, 5]],
        },
        "output": 1,
    },
    {
        "input": {
            "heights": [
                [1, 2, 1, 1, 1],
                [1, 2, 1, 2, 1],
                [1, 2, 1, 2, 1],
                [1, 2, 1, 2, 1],
                [1, 1, 1, 2, 1],
            ],
        },
        "output": 0,
    },
]


@pytest.mark.sol1631
def test_run():
    for case in cases:
        assert (
            Solution.minimum_effort_path(
                heights=case["input"]["heights"],
            )
            == case["output"]
        )
