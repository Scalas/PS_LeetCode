import pytest
from solutions.sol_290 import Solution

cases = [
    {
        'input': {
            'pattern': "abba",
            's': "dog cat cat dog"
        },
        'output': True
    },
    {
        'input': {
            'pattern': "abba",
            's': "dog cat cat fish"
        },
        'output': False
    },
    {
        'input': {
            'pattern': "abba",
            's': "dog cat cat dog"
        },
        'output': True
    },
    {
        'input': {
            'pattern': "aaaa",
            's': "dog cat cat dog"
        },
        'output': False
    },
]


@pytest.mark.sol_290
def test_run():
    for case in cases:
        assert Solution.word_pattern(
            pattern=case['input']['pattern'],
            s=case['input']['s']
        ) == case['output']
