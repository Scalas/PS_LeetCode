import pytest
from solutions.sol_518 import Solution

cases = [
    {
        'input': {
            'amount': 5,
            'coins': [1, 2, 5],
        },
        'output': 4,
    },
    {
        'input': {
            'amount': 3,
            'coins': [2],
        },
        'output': 0,
    },
    {
        'input': {
            'amount': 10,
            'coins': [10],
        },
        'output': 1,
    },
]


@pytest.mark.sol_518
def test_run():
    for case in cases:
        assert Solution.change(
            amount=case['input']['amount'],
            coins=case['input']['coins'],
        ) == case['output']
