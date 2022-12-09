import pytest
from solutions.sol_1800 import Solution

cases = [
    {
        'input': {
            'nums': [10, 20, 30, 5, 10, 50]
        },
        'output': 65
    },
    {
        'input': {
            'nums': [10, 20, 30, 40, 50]
        },
        'output': 150
    },
    {
        'input': {
            'nums': [12, 17, 15, 13, 10, 11, 12]
        },
        'output': 33
    },
]


@pytest.mark.sol1800
def test_run():
    for case in cases:
        assert Solution.max_ascending_sum(
            nums=case['input']['nums']
        ) == case['output']
