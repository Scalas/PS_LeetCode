import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_1161 import Solution

cases = [
    {
        'input': {
            'root': [1, 7, 0, 7, -8, None, None],
        },
        'output': 2,
    },
    {
        'input': {
            'root': [989, None, 10250, 98693, -89388, None, None, None, -32127],
        },
        'output': 2.
    },
]


@pytest.mark.sol_1161
def test_run():
    for case in cases:
        assert Solution.max_level_sum(
            root=list_to_tree(case['input']['root'])
        ) == case['output']
