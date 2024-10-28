import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_2458 import Solution


cases = [
    {
        "input": {
            "root": [1, 3, 4, 2, None, 6, 5, None, None, None, None, None, 7],
            "queries": [4],
        },
        "output": [2],
    },
    {
        "input": {"root": [5, 8, 9, 2, 1, 3, 7, 4, 6], "queries": [3, 2, 4, 8]},
        "output": [3, 2, 3, 2],
    },
]


@pytest.mark.sol2458
def test_run():
    for case in cases:
        assert (
            Solution.tree_queries(
                root=list_to_tree(case["input"]["root"]),
                queries=case["input"]["queries"],
            )
            == case["output"]
        )
