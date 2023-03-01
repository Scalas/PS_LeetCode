import pytest
from solutions.sol_912 import Solution

cases = [
    {
        'input': {
            'nums': [5, 2, 3, 1],
        },
        'output': [1, 2, 3, 5]
    },
    {
        'input': {
            'nums': [5, 1, 1, 2, 0, 0],
        },
        'output': [0, 0, 1, 1, 2, 5]
    },
]


@pytest.mark.sol912
def test_run():
    for case in cases:
        assert Solution.sort_array(
            nums=case['input']['nums']
        ) == case['output']
