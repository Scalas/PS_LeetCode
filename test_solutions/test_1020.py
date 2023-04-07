import pytest
from solutions.sol_1020 import Solution

cases = [
    {
        'input': {
            'grid': [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
        },
        'output': 3,
    },
    {
        'input': {
            'grid': [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]],
        },
        'output': 0,
    },
]


@pytest.mark.sol1020
def test_run():
    for case in cases:
        assert Solution.num_enclaves(
            grid=case['input']['grid'],
        ) == case['output']
