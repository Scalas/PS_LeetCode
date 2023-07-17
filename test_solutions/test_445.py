import pytest

from converter.leet_code_utils import list_to_linked_list, compare_linked_list
from solutions.sol_445 import Solution

cases = [
    {
        'input': {
            'l1': [7, 2, 4, 3],
            'l2': [5, 6, 4],
        },
        'output': [7, 8, 0, 7],
    },
    {
        'input': {
            'l1': [2, 4, 3],
            'l2': [5, 6, 4],
        },
        'output': [8, 0, 7],
    },
    {
        'input': {
            'l1': [0],
            'l2': [0],
        },
        'output': [0],
    },
]


@pytest.mark.sol_445
def test_run():
    for case in cases:
        assert compare_linked_list(Solution.add_two_numbers(
            l1=list_to_linked_list(case['input']['l1']),
            l2=list_to_linked_list(case['input']['l2']),
        ), list_to_linked_list(case['output']))
