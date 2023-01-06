import pytest
from solutions.sol_1833 import Solution

cases = [
    {
        'input': {
            'costs': [1, 3, 2, 4, 1],
            'coins': 7
        },
        'output': 4
    },
    {
        'input': {
            'costs': [10, 6, 8, 7, 7, 8],
            'coins': 5
        },
        'output': 0
    },
    {
        'input': {
            'costs': [1, 6, 3, 1, 2, 5],
            'coins': 20
        },
        'output': 6
    },
]


@pytest.mark.sol1833
def test_run():
    for case in cases:
        assert Solution.max_ice_cream(
            costs=case['input']['costs'],
            coins=case['input']['coins']
        ) == case['output']
