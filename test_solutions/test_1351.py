import pytest
from solutions.sol_1351 import Solution

cases = [
    {
        'input': {
            'grid': [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]],
        },
        'output': 8,
    },
    {
        'input': {
            'grid': [[3, 2], [1, 0]],
        },
        'output': 0,
    },
]


@pytest.mark.sol1351
def test_run():
    for case in cases:
        assert Solution.count_negatives(
            grid=case['input']['grid']
        ) == case['output']
