import pytest
from solutions.sol_744 import Solution

cases = [
    {
        'input': {
            'letters': ['c', 'f', 'j'],
            'target': 'a'
        },
        'output': 'c'
    },
    {
        'input': {
            'letters': ['c', 'f', 'j'],
            'target': 'c'
        },
        'output': 'f'
    },
    {
        'input': {
            'letters': ['x', 'x', 'y', 'y'],
            'target': 'z'
        },
        'output': 'x'
    },
]


@pytest.mark.sol_744
def test_run():
    for case in cases:
        assert Solution.next_greatest_letter(
            letters=case['input']['letters'],
            target=case['input']['target'],
        ) == case['output']
