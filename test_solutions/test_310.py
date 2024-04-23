import pytest
from solutions.sol_310 import Solution

cases = [
    {"input": {"n": 4, "edges": [[1, 0], [1, 2], [1, 3]]}, "output": [1]},
    {
        "input": {"n": 6, "edges": [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]},
        "output": [3, 4],
    },
    {"input": {"n": 3, "edges": [[0, 1], [0, 2]]}, "output": [0]},
]


@pytest.mark.sol_310
def test_run():
    for case in cases:
        assert (
            Solution.find_min_height_trees(
                n=case["input"]["n"], edges=case["input"]["edges"]
            )
            == case["output"]
        )
