import pytest
from solutions.sol_1218 import Solution

cases = [
    {
        'input': {
            'arr': [1, 2, 3, 4],
            'difference': 1,
        },
        'output': 4,
    },
    {
        'input': {
            'arr': [1, 3, 5, 7],
            'difference': 1,
        },
        'output': 1,
    },
    {
        'input': {
            'arr': [1, 5, 7, 8, 5, 3, 4, 2, 1],
            'difference': -2,
        },
        'output': 4,
    },
]


@pytest.mark.sol1218
def test_run():
    for case in cases:
        assert Solution.longest_subsequence(
            arr=case['input']['arr'],
            difference=case['input']['difference'],
        ) == case['output']
