import pytest

from converter.leet_code_utils import list_to_linked_list, compare_linked_list
from solutions.sol_21 import Solution

cases = [
    {
        'input': {
            'list1': [1, 2, 4],
            'list2': [1, 3, 4],
        },
        'output': [1, 1, 2, 3, 4, 4],
    },
    {
        'input': {
            'list1': [],
            'list2': [],
        },
        'output': [],
    },
    {
        'input': {
            'list1': [],
            'list2': [0],
        },
        'output': [0],
    },
]


@pytest.mark.sol21
def test_run():
    for case in cases:
        assert compare_linked_list(Solution.merge_two_lists(
            list1=list_to_linked_list(case['input']['list1']),
            list2=list_to_linked_list(case['input']['list2'])
        ), list_to_linked_list(case['output']))
