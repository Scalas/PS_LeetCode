import pytest
from solutions.sol_1416 import Solution

cases = [
    {
        'input': {
            's': '1000',
            'k': 10000,
        },
        'output': 1,
    },
    {
        'input': {
            's': '1000',
            'k': 10,
        },
        'output': 0,
    },
    {
        'input': {
            's': '1317',
            'k': 2000,
        },
        'output': 8,
    },
]


@pytest.mark.sol1416
def test_run():
    for case in cases:
        assert Solution.number_of_arrays(
            s=case['input']['s'],
            k=case['input']['k']
        ) == case['output']
