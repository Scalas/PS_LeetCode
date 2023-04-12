import pytest
from solutions.sol_70 import Solution

cases = [
    {
        'input': {
            'n': 2,
        },
        'output': 2,
    },
    {
        'input': {
            'n': 3,
        },
        'output': 3,
    },
]


@pytest.mark.sol70
def test_run():
    for case in cases:
        assert Solution.climb_stairs(
            n=case['input']['n']
        ) == case['output']
