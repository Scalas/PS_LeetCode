import pytest
from solutions.sol_953 import Solution

cases = [
    {
        'input': {
            'words': ['hello', 'leetcode'],
            'order': 'hlabcdefgijkmnopqrstuvwxyz'
        },
        'output': True
    },
    {
        'input': {
            'words': ['word', 'world', 'row'],
            'order': 'worldabcefghijkmnpqstuvxyz'
        },
        'output': False
    },
    {
        'input': {
            'words': ['apple', 'app'],
            'order': 'abcdefghijklmnopqrstuvwxyz'
        },
        'output': False
    },
]


@pytest.mark.sol953
def test_run():
    for case in cases:
        assert Solution.is_alien_sorted(
            words=case['input']['words'],
            order=case['input']['order']
        ) == case['output']
