import pytest
from solutions.sol_802 import Solution

cases = [
    {
        "input": {
            "graph": [[1, 2], [2, 3], [5], [0], [5], [], []],
        },
        "output": [2, 4, 5, 6],
    },
    {
        "input": {
            "graph": [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []],
        },
        "output": [4],
    },
]


@pytest.mark.sol_802
def test_run():
    for case in cases:
        assert (
            Solution.eventual_safe_nodes(graph=case["input"]["graph"]) == case["output"]
        )
