import pytest
from solutions.sol_209 import Solution

cases = [
    {
        'input': {
            'target': 7,
            'nums': [2, 3, 1, 2, 4, 3],
        },
        'output': 2
    },
    {
        'input': {
            'target': 4,
            'nums': [1, 4, 4],
        },
        'output': 1,
    },
    {
        'input': {
            'target': 11,
            'nums': [1, 1, 1, 1, 1, 1, 1, 1],
        },
        'output': 0,
    },
    {
        'input': {
            'target': 11,
            'nums': [1, 2, 3, 4, 5],
        },
        'output': 3,
    },
]


@pytest.mark.sol209
def test_run():
    for case in cases:
        assert Solution.min_sub_array_len(
            target=case['input']['target'],
            nums=case['input']['nums'],
        ) == case['output']
