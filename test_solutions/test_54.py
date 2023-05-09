import pytest
from solutions.sol_54 import Solution

cases = [
    {
        'input': {
            'matrix': [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        },
        'output': [1, 2, 3, 6, 9, 8, 7, 4, 5],
    },
    {
        'input': {
            'matrix': [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
        },
        'output': [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
    },
]


@pytest.mark.sol54
def test_run():
    for case in cases:
        assert Solution.spiral_order(
            matrix=case['input']['matrix'],
        ) == case['output']
