import pytest
from solutions.sol_16 import Solution

cases = [
    {
        'input': {
            'nums': [-1, 2, 1, -4],
            'target': 1
        },
        'output': 2
    },
    {
        'input': {
            'nums': [0, 0, 0],
            'target': 1
        },
        'output': 0
    },
]


@pytest.mark.sol16
def test_run():
    for case in cases:
        assert Solution.three_sum_closest(
            nums=case['input']['nums'],
            target=case['input']['target']
        ) == case['output']
