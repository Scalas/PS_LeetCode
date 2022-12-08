import pytest
from solutions.sol1512 import Solution

cases = [
    {
        'input': {
            'nums': [1, 2, 3, 1, 1, 3]
        },
        'output': 4
    },
    {
        'input': {
            'nums': [1, 1, 1, 1]
        },
        'output': 6
    },
    {
        'input': {
            'nums': [1, 2, 3]
        },
        'output': 0
    },
]


@pytest.mark.sol1512
def test_run():
    for case in cases:
        assert Solution.num_identical_pairs(
            nums=case['input']['nums']
        ) == case['output']
