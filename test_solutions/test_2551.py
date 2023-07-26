import pytest
from solutions.sol_1870 import Solution

cases = [
    {
        'input': {
            'dist': [1, 3, 2],
            'hour': 6,
        },
        'output': 1,
    },
    {
        'input': {
            'dist': [1, 3, 2],
            'hour': 2.7,
        },
        'output': 3,
    },
    {
        'input': {
            'dist': [1, 3, 2],
            'hour': 1.9,
        },
        'output': -1,
    },
]


@pytest.mark.sol_1870
def test_run():
    for case in cases:
        assert Solution.min_speed_on_time(
            dist=case['input']['dist'],
            hour=case['input']['hour']
        ) == case['output']
