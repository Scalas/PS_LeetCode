import pytest
from solutions.sol_1697 import Solution

cases = [
    {
        "input": {
            "n": 3,
            "edge_list": [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]],
            "queries": [[0, 1, 2], [0, 2, 5]],
        },
        "output": [False, True],
    },
    {
        "input": {
            "n": 5,
            "edge_list": [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]],
            "queries": [[0, 4, 14], [1, 4, 13]],
        },
        "output": [True, False],
    },
]


@pytest.mark.sol1697
def test_run():
    for case in cases:
        assert (
            Solution.distance_limited_paths_exist(
                n=case["input"]["n"],
                edge_list=case["input"]["edge_list"],
                queries=case["input"]["queries"],
            )
            == case["output"]
        )
