import pytest
from solutions.sol_1675 import Solution

cases = [
    {
        'input': {
            'nums': [1, 2, 3, 4],
        },
        'output': 1
    },
    {
        'input': {
            'nums': [4, 1, 5, 20, 3],
        },
        'output': 3
    },
    {
        'input': {
            'nums': [2, 10, 8],
        },
        'output': 3
    },
]


@pytest.mark.sol1675
def test_run():
    for case in cases:
        assert Solution.minimum_deviation(
            nums=case['input']['nums'],
        ) == case['output']
