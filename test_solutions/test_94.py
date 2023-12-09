import pytest
from solutions.sol_94 import Solution
from converter.leet_code_utils import list_to_tree

cases = [
    {
        "input": {
            "root": [1, None, 2, 3],
        },
        "output": [1, 3, 2],
    },
    {
        "input": {
            "root": [],
        },
        "output": [],
    },
    {
        "input": {
            "root": [1],
        },
        "output": [1],
    },
]


@pytest.mark.sol94
def test_run():
    for case in cases:
        assert (
            Solution.inorder_traversal(
                root=list_to_tree(case["input"]["root"]),
            )
            == case["output"]
        )
