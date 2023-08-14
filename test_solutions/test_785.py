import pytest
from solutions.sol_785 import Solution

cases = [
    {
        "input": {
            "graph": [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]],
        },
        "output": False,
    },
    {
        "input": {
            "graph": [[1, 3], [0, 2], [1, 3], [0, 2]],
        },
        "output": True,
    },
]


@pytest.mark.sol_785
def test_run():
    for case in cases:
        assert (
            Solution.is_bipartite(
                graph=case["input"]["graph"],
            )
            == case["output"]
        )
