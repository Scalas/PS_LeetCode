import pytest
from solutions.sol_2316 import Solution

cases = [
    {
        "input": {
            "n": 3,
            "edges": [[0, 1], [0, 2], [1, 2]],
        },
        "output": 0,
    },
    {
        "input": {
            "n": 7,
            "edges": [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]],
        },
        "output": 14,
    },
]


@pytest.mark.sol_2316
def test_run():
    for case in cases:
        assert (
            Solution.count_pairs(
                n=case["input"]["n"],
                edges=case["input"]["edges"],
            )
            == case["output"]
        )
