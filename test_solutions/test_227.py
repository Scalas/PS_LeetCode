import pytest
from solutions.sol_227 import Solution

cases = [
    {
        'input': {
            's': "3+2*2"
        },
        'output': 7
    },
    {
        'input': {
            's': " 3/2 "
        },
        'output': 1
    },
    {
        'input': {
            's': " 3+5 / 2 "
        },
        'output': 5
    },
    {
        'input': {
            's': "1+1-1"
        },
        'output': 1
    },
    {
        'input': {
            's': "1+1+1"
        },
        'output': 3
    },
    {
        'input': {
            's': "1*2-3/4+5*6-7*8+9/10"
        },
        'output': -24
    },
]


@pytest.mark.sol227
def test_run():
    for case in cases:
        assert Solution.calculate(
            s=case['input']['s']
        ) == case['output']
