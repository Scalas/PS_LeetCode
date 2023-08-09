import pytest
from solutions.sol_2616 import Solution

cases = [
    {
        'input': {
            'nums': [10, 1, 2, 7, 1, 3],
            'p': 2,
        },
        'output': 1,
    },
    {
        'input': {
            'nums': [4, 2, 1, 2],
            'p': 1,
        },
        'output': 0,
    },
    {
        'input': {
            'nums': [3, 4, 2, 3, 2, 1, 2],
            'p': 3,
        },
        'output': 1,
    },
]


@pytest.mark.sol_2616
def test_run():
    for case in cases:
        assert Solution.minimize_max(
            nums=case['input']['nums'],
            p=case['input']['p']
        ) == case['output']
