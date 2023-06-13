import pytest
from solutions.sol_2352 import Solution

cases = [
    {
        'input': {
            'grid': [[3, 2, 1], [1, 7, 6], [2, 7, 7]],
        },
        'output': 1,
    },
    {
        'input': {
            'grid': [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]],
        },
        'output': 3,
    },
]


@pytest.mark.sol_2352
def test_run():
    for case in cases:
        assert Solution.equal_pairs(
            grid=case['input']['grid'],
        ) == case['output']
