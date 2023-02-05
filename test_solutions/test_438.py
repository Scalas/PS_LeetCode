import pytest
from solutions.sol_438 import Solution

cases = [
    {
        'input': {
            's': 'cbaebabacd',
            'p': 'abc'
        },
        'output': [0, 6]
    },
    {
        'input': {
            's': 'abab',
            'p': 'ab'
        },
        'output': [0, 1, 2]
    },
]


@pytest.mark.sol_438
def test_run():
    for case in cases:
        assert Solution.find_anagrams(
            s=case['input']['s'],
            p=case['input']['p'],
        ) == case['output']
