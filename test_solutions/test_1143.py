import pytest
from solutions.sol_1143 import Solution

cases = [
    {
        'input': {
            'text1': 'abcde',
            'text2': 'ace'
        },
        'output': 3
    },
    {
        'input': {
            'text1': 'abc',
            'text2': 'abc'
        },
        'output': 3
    },
    {
        'input': {
            'text1': 'abc',
            'text2': 'def'
        },
        'output': 0
    },
]


@pytest.mark.sol1143
def test_run():
    for case in cases:
        assert Solution.longest_common_subsequence(
            text1=case['input']['text1'],
            text2=case['input']['text2']
        ) == case['output']
