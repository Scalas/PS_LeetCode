import pytest
from solutions.sol_1615 import Solution

cases = [
    {
        "input": {
            "n": 4,
            "roads": [[0, 1], [0, 3], [1, 2], [1, 3]],
        },
        "output": 4,
    },
    {
        "input": {
            "n": 5,
            "roads": [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [2, 4]],
        },
        "output": 5,
    },
    {
        "input": {
            "n": 8,
            "roads": [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]],
        },
        "output": 5,
    },
]


@pytest.mark.sol1615
def test_run():
    for case in cases:
        assert (
            Solution.maximal_network_rank(
                n=case["input"]["n"],
                roads=case["input"]["roads"],
            )
            == case["output"]
        )
