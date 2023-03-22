import pytest
from solutions.sol_2492 import Solution

cases = [
    {
        'input': {
            'n': 4,
            'roads': [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]],
        },
        'output': 5,
    },
    {
        'input': {
            'n': 4,
            'roads': [[1, 2, 2], [1, 3, 4], [3, 4, 7]],
        },
        'output': 2,
    },
]


@pytest.mark.sol_2492
def test_run():
    for case in cases:
        assert Solution.min_score(
            n=case['input']['n'],
            roads=case['input']['roads']
        ) == case['output']
