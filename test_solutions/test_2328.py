import pytest
from solutions.sol_2328 import Solution

cases = [
    {
        'input': {
            'grid': [[1, 1], [3, 4]],
        },
        'output': 8,
    },
    {
        'input': {
            'grid': [[1], [2]],
        },
        'output': 3,
    },
]


@pytest.mark.sol_2328
def test_run():
    for case in cases:
        assert Solution.count_paths(
            grid=case['input']['grid'],
        ) == case['output']
