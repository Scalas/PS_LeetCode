import pytest
from solutions.sol_18 import Solution

cases = [
    {
        'input': {
            'nums': [1, 0, -1, 0, -2, 2],
            'target': 0
        },
        'output': [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    },
    {
        'input': {
            'nums': [2, 2, 2, 2, 2],
            'target': 8
        },
        'output': [[2, 2, 2, 2]]
    },
]


@pytest.mark.sol18
def test_run():
    for case in cases:
        assert sorted(Solution.four_sum(
            nums=case['input']['nums'],
            target=case['input']['target']
        )) == sorted(case['output'])
