import pytest
from solutions.sol_72 import Solution

cases = [
    {
        'input': {
            'word1': 'horse',
            'word2': 'ros'
        },
        'output': 3
    },
    {
        'input': {
            'word1': 'intention',
            'word2': 'execution'
        },
        'output': 5
    },
]


@pytest.mark.sol72
def test_run():
    for case in cases:
        assert Solution.min_distance(
            word1=case['input']['word1'],
            word2=case['input']['word2']
        ) == case['output']
