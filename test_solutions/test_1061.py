import pytest
from solutions.sol_1061 import Solution

cases = [
    {
        'input': {
            's1': 'parker',
            's2': 'morris',
            'base_str': 'parser'
        },
        'output': 'makkek'
    },
    {
        'input': {
            's1': 'hello',
            's2': 'world',
            'base_str': 'hold'
        },
        'output': 'hdld'
    },
    {
        'input': {
            's1': 'leetcode',
            's2': 'programs',
            'base_str': 'sourcecode'
        },
        'output': 'aauaaaaada'
    },
]


@pytest.mark.sol1061
def test_run():
    for case in cases:
        assert Solution.smallest_equivalent_string(
            s1=case['input']['s1'],
            s2=case['input']['s2'],
            base_str=case['input']['base_str']
        ) == case['output']
