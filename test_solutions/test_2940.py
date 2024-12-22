import pytest
from solutions.sol_2940 import Solution


cases = [
    {
        "input": {
            "heights": [6, 4, 8, 5, 2, 7],
            "queries": [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]],
        },
        "output": [2, 5, -1, 5, 2],
    },
    {
        "input": {
            "heights": [5, 3, 8, 2, 6, 1, 4, 6],
            "queries": [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]],
        },
        "output": [7, 6, -1, 4, 6],
    },
]


@pytest.mark.sol2940
def test_run():
    for case in cases:
        assert (
            Solution.leftmost_building_queries(
                queries=case["input"]["queries"],
                heights=case["input"]["heights"],
            )
            == case["output"]
        )
