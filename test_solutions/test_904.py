import pytest
from solutions.sol_904 import Solution

cases = [
    {
        'input': {
            'fruits': [1, 2, 1]
        },
        'output': 3
    },
    {
        'input': {
            'fruits': [0, 1, 2, 2]
        },
        'output': 3
    },
    {
        'input': {
            'fruits': [1, 2, 3, 2, 2]
        },
        'output': 4
    },

]


@pytest.mark.sol904
def test_run():
    for case in cases:
        assert Solution.total_fruit(
            fruits=case['input']['fruits'],
        ) == case['output']
