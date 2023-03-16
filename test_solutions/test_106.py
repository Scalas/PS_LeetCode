import pytest
from solutions.sol_106 import Solution
from converter.leet_code_utils import list_to_tree, compare_tree

cases = [
    {
        'input': {
            'inorder': [9, 3, 15, 20, 7],
            'postorder': [9, 15, 7, 20, 3],
        },
        'output': [3, 9, 20, None, None, 15, 7]
    },
    {
        'input': {
            'inorder': [-1],
            'postorder': [-1],
        },
        'output': [-1]
    },
]


@pytest.mark.sol106
def test_run():
    for case in cases:
        assert compare_tree(Solution.build_tree(
            inorder=case['input']['inorder'],
            postorder=case['input']['postorder'],
        ), list_to_tree(case['output']))
