import pytest
from solutions.sol_1443 import Solution

cases = [
    {
        'input': {
            'n': 7,
            'edges': [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            'has_apple': [False, False, True, False, True, True, False],
        },
        'output': 8,
    },
    {
        'input': {
            'n': 7,
            'edges': [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            'has_apple': [False, False, True, False, False, True, False],
        },
        'output': 6,
    },
    {
        'input': {
            'n': 7,
            'edges': [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            'has_apple': [False, False, False, False, False, False, False],
        },
        'output': 0,
    },
]


@pytest.mark.sol1443
def test_run():
    for case in cases:
        assert Solution.min_time(
            n=case['input']['n'],
            edges=case['input']['edges'],
            has_apple=case['input']['has_apple']
        ) == case['output']
