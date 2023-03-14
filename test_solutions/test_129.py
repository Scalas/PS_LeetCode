import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_129 import Solution

cases = [
    {
        'input': {
            'root': [1, 2, 3],
        },
        'output': 25
    },
    {
        'input': {
            'root': [4, 9, 0, 5, 1],
        },
        'output': 1026
    },
]


@pytest.mark.sol129
def test_run():
    for case in cases:
        assert Solution.sum_numbers(
            root=list_to_tree(case['input']['root']),
        ) == case['output']
