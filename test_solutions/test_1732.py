import pytest

from solutions.sol_1732 import Solution

cases = [
    {
        'input': {
            'gain': [-5, 1, 5, 0, -7],
        },
        'output': 1,
    },
    {
        'input': {
            'gain': [-4, -3, -2, -1, 4, 3, 2],
        },
        'output': 0,
    },
]


@pytest.mark.sol1732
def test_run():
    for case in cases:
        assert Solution.largest_altitude(
            gain=case['input']['gain'],
        ) == case['output']
