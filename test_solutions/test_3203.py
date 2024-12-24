import pytest
from solutions.sol_3203 import Solution

cases = [
    {
        "input": {"edges1": [[0, 1], [0, 2], [0, 3]], "edges2": [[0, 1]]},
        "output": 3,
    },
    {
        "input": {
            "edges1": [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
            "edges2": [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
        },
        "output": 5,
    },
    {
        "input": {
            "edges1": [
                [0, 1],
                [2, 0],
                [3, 2],
                [3, 6],
                [8, 7],
                [4, 8],
                [5, 4],
                [3, 5],
                [3, 9],
            ],
            "edges2": [[0, 1], [0, 2], [0, 3]],
        },
        "output": 7,
    },
    {
        "input": {
            "edges1": [],
            "edges2": [[0, 1]],
        },
        "output": 2,
    },
]


@pytest.mark.sol3203
def test_run():
    for case in cases:
        assert (
            Solution.minimum_diameter_after_merge(
                edges1=case["input"]["edges1"],
                edges2=case["input"]["edges2"],
            )
            == case["output"]
        )
