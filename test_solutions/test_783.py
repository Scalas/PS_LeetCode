import pytest
from solutions.sol_783 import Solution
from converter.leet_code_converter import list_to_tree

cases = [
    {
        'input': {
            'root': [4, 2, 6, 1, 3],
        },
        'output': 1
    },
    {
        'input': {
            'root': [1, 0, 48, None, None, 12, 49],
        },
        'output': 1
    },
]


@pytest.mark.sol_783
def test_run():
    for case in cases:
        assert Solution.min_diff_in_bst(
            root=list_to_tree(case['input']['root']),
        ) == case['output']
