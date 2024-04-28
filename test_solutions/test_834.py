import pytest
from solutions.sol_834 import Solution

cases = [
    {
        "input": {
            "n": 6,
            "edges": [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]],
        },
        "output": [8, 12, 6, 10, 10, 10],
    },
    {
        "input": {
            "n": 1,
            "edges": [],
        },
        "output": [0],
    },
    {
        "input": {
            "n": 2,
            "edges": [[1, 0]],
        },
        "output": [1, 1],
    },
]


@pytest.mark.sol_834
def test_run():
    for case in cases:
        assert (
            Solution.sum_of_distances_in_tree(
                n=case["input"]["n"], edges=case["input"]["edges"]
            )
            == case["output"]
        )
