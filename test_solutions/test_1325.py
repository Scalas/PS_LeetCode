import pytest

from converter.leet_code_utils import list_to_tree, compare_tree
from solutions.sol_1325 import Solution

cases = [
    {
        "input": {
            "root": [1, 2, 3, 2, None, 2, 4],
            "target": 2,
        },
        "output": [1, None, 3, None, 4],
    },
    {
        "input": {
            "root": [1, 3, 3, 3, 2],
            "target": 3,
        },
        "output": [1, 3, None, None, 2],
    },
    {
        "input": {
            "root": [1, 2, None, 2, None, 2],
            "target": 2,
        },
        "output": [1],
    },
]


@pytest.mark.sol_1325
def test_run():
    for case in cases:
        assert compare_tree(
            Solution.remove_leaf_nodes(
                root=list_to_tree(case["input"]["root"]),
                target=case["input"]["target"],
            ),
            list_to_tree(case["output"]),
        )
