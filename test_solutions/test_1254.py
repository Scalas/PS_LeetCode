import pytest
from solutions.sol_1254 import Solution

cases = [
    {
        'input': {
            'grid': [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0],
                     [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]],
        },
        'output': 2,
    },
    {
        'input': {
            'grid': [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]],
        },
        'output': 1,
    },
]


@pytest.mark.sol1254
def test_run():
    for case in cases:
        assert Solution.closed_island(
            grid=case['input']['grid'],
        ) == case['output']
