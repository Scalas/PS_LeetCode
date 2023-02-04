import pytest
from solutions.sol_567 import Solution

cases = [
    {
        'input': {
            's1': 'ab',
            's2': 'eidbaooo'
        },
        'output': True
    },
    {
        'input': {
            's1': 'ab',
            's2': 'eidboaoo'
        },
        'output': False
    },
]


@pytest.mark.sol_567
def test_run():
    for case in cases:
        assert Solution.check_inclusion(
            s1=case['input']['s1'],
            s2=case['input']['s2']
        ) == case['output']
