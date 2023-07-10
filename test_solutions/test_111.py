import pytest
from solutions.sol_111 import Solution
from converter.leet_code_utils import list_to_tree

cases = [
    {
        'input': {
            'root': [3, 9, 20, None, None, 15, 7],
        },
        'output': 2,
    },
    {
        'input': {
            'root': [2, None, 3, None, 4, None, 5, None, 6],
        },
        'output': 5,
    },
    {
        'input': {
            'root': [],
        },
        'output': 0,
    },
]


@pytest.mark.sol104
def test_run():
    for case in cases:
        assert Solution.min_depth(
            root=list_to_tree(case['input']['root']),
        ) == case['output']
