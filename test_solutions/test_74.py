import pytest
from solutions.sol_74 import Solution

cases = [
    {
        'input': {
            'matrix': [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            'target': 3,
        },
        'output': True,
    },
    {
        'input': {
            'matrix': [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            'target': 13,
        },
        'output': False,
    },
]


@pytest.mark.sol74
def test_run():
    for case in cases:
        assert Solution.search_matrix(
            matrix=case['input']['matrix'],
            target=case['input']['target']
        ) == case['output']
