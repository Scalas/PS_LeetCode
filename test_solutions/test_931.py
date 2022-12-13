import pytest
from solutions.sol_931 import Solution

cases = [
    {
        'input': {
            'matrix': [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
        },
        'output': 13
    },
    {
        'input': {
            'matrix': [[-19, 57], [-40, -5]]
        },
        'output': -59
    },
]


@pytest.mark.sol931
def test_run():
    for case in cases:
        assert Solution.min_falling_path_sum(
            matrix=case['input']['matrix']
        ) == case['output']
