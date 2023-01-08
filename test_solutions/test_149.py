import pytest
from solutions.sol_149 import Solution

cases = [
    {
        'input': {
            'points': [[1, 1], [2, 2], [3, 3]]
        },
        'output': 3
    },
    {
        'input': {
            'points': [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
        },
        'output': 4
    },
]


@pytest.mark.sol149
def test_run():
    for case in cases:
        assert Solution.max_points(
            points=case['input']['points'],
        ) == case['output']
