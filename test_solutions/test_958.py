import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_958 import Solution

cases = [
    {
        'input': {
            'root': [1, 2, 3, 4, 5, 6],
        },
        'output': True,
    },
    {
        'input': {
            'root': [1, 2, 3, 4, 5, None, 7],
        },
        'output': False,
    },
]


@pytest.mark.sol958
def test_run():
    for case in cases:
        assert Solution.is_complete_tree(
            root=list_to_tree(case['input']['root']),
        ) == case['output']
