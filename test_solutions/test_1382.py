import pytest

from converter.leet_code_utils import list_to_tree, compare_tree
from solutions.sol_1382 import Solution


cases = [
    {
        "input": {"root": [1, None, 2, None, 3, None, 4, None, None]},
        "output": [2, 1, 3, None, None, None, 4],
    },
    {
        "input": {"root": [2, 1, 3]},
        "output": [2, 1, 3],
    },
]


@pytest.mark.sol1382
def test_run():
    for case in cases:
        assert compare_tree(
            Solution.balance_bst(
                root=list_to_tree(case["input"]["root"]),
            ),
            list_to_tree(case["output"]),
        )
