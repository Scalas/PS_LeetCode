import pytest
from solutions.sol_2272 import Solution

cases = [
    {
        'input': {
            's': 'aababbb'
        },
        'output': 3
    },
    {
        'input': {
            's': 'abcde'
        },
        'output': 0
    },
    {
        'input': {
            's': 'icexiahccknibwuwgi'
        },
        'output': 3
    },
    {
        'input': {
            's': 'lripaa'
        },
        'output': 1
    },
]


@pytest.mark.sol_2272
def test_run():
    for case in cases:
        assert Solution.largest_variance(
            s=case['input']['s']
        ) == case['output']
