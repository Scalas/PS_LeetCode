import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_530 import Solution

cases = [
    {
        'input': {
            'root': [4, 2, 6, 1, 3]
        },
        'output': 1
    },
    {
        'input': {
            'root': [1, 0, 48, None, None, 12, 49]
        },
        'output': 1
    },
    {
        'input': {
            'root': [1, None, 2]
        },
        'output': 1
    },
]


@pytest.mark.sol_530
def test_run():
    for case in cases:
        assert Solution.get_minimum_difference(
            root=list_to_tree(case['input']['root'])
        ) == case['output']
