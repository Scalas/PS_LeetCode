import pytest
from solutions.sol_1822 import Solution

cases = [
    {
        'input': {
            'nums': [-1, -2, -3, -4, 3, 2, 1],
        },
        'output': 1,
    },
    {
        'input': {
            'nums': [1, 5, 0, 2, -3],
        },
        'output': 0,
    },
    {
        'input': {
            'nums': [-1, 1, -1, 1, -1],
        },
        'output': -1,
    },
]


@pytest.mark.sol1822
def test_run():
    for case in cases:
        assert Solution.array_sign(
            nums=case['input']['nums']
        ) == case['output']
