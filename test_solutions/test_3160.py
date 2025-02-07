import pytest
from solutions.sol_3160 import Solution


cases = [
    {
        "input": {"limit": 4, "queries": [[1, 4], [2, 5], [1, 3], [3, 4]]},
        "output": [1, 2, 2, 3],
    },
    {
        "input": {"limit": 4, "queries": [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]},
        "output": [1, 2, 2, 3, 4],
    },
]


@pytest.mark.sol3160
def test_run():
    for case in cases:
        assert (
            Solution.queryResults(
                limit=case["input"]["limit"],
                queries=case["input"]["queries"],
            )
            == case["output"]
        )
