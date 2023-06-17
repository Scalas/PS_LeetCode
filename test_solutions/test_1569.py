import pytest
from solutions.sol_1569 import Solution

cases = [
    {
        'input': {
            'nums': [2, 1, 3],
        },
        'output': 1,
    },
    {
        'input': {
            'nums': [3, 4, 5, 1, 2],
        },
        'output': 5,
    },
    {
        'input': {
            'nums': [1, 2, 3],
        },
        'output': 0,
    },
]


@pytest.mark.sol1569
def test_run():
    for case in cases:
        assert Solution.num_of_ways(
            nums=case['input']['nums'],
        ) == case['output']
