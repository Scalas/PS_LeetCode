import pytest
from solutions.sol_1489 import Solution

cases = [
    {
        "input": {
            "n": 5,
            "edges": [
                [0, 1, 1],
                [1, 2, 1],
                [2, 3, 2],
                [0, 3, 2],
                [0, 4, 3],
                [3, 4, 3],
                [1, 4, 6],
            ],
        },
        "output": [[0, 1], [2, 3, 4, 5]],
    },
    {
        "input": {
            "n": 4,
            "edges": [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]],
        },
        "output": [[], [0, 1, 2, 3]],
    },
    {
        "input": {
            "n": 6,
            "edges": [
                [0, 1, 1],
                [1, 2, 1],
                [0, 2, 1],
                [2, 3, 4],
                [3, 4, 2],
                [3, 5, 2],
                [4, 5, 2],
            ],
        },
        "output": [[3], [0, 1, 2, 4, 5, 6]],
    },
]


@pytest.mark.sol1489
def test_run():
    for case in cases:
        assert (
            Solution.find_critical_and_pseudo_critical_edges(
                n=case["input"]["n"], edges=case["input"]["edges"]
            )
            == case["output"]
        )
