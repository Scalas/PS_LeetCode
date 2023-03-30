import pytest
from solutions.sol_87 import Solution

cases = [
    {
        'input': {
            's1': 'great',
            's2': 'rgeat'
        },
        'output': True
    },
    {
        'input': {
            's1': 'abcde',
            's2': 'caebd'
        },
        'output': False
    },
    {
        'input': {
            's1': 'a',
            's2': 'a'
        },
        'output': True
    },
    {
        'input': {
            's1': 'eebaacbcbcadaaedceaaacadccd',
            's2': 'eadcaacabaddaceacbceaabeccd'
        },
        'output': False
    },
]


@pytest.mark.sol87
def test_run():
    for case in cases:
        assert Solution.is_scramble(
            s1=case['input']['s1'],
            s2=case['input']['s2']
        ) == case['output']
