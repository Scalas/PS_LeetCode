import pytest
from solutions.sol_1470 import Solution

cases = [
    {
        'input': {
            'nums': [2, 5, 1, 3, 4, 7],
            'n': 3,
        },
        'output': [2, 3, 5, 4, 1, 7]
    },
    {
        'input': {
            'nums': [1, 2, 3, 4, 4, 3, 2, 1],
            'n': 4,
        },
        'output': [1, 4, 2, 3, 3, 2, 4, 1]
    },
    {
        'input': {
            'nums': [1, 1, 2, 2],
            'n': 2,
        },
        'output': [1, 2, 1, 2]
    },
]


@pytest.mark.sol1470
def test_run():
    for case in cases:
        assert Solution.shuffle(
            nums=case['input']['nums'],
            n=case['input']['n']
        ) == case['output']
