import pytest
from solutions.sol_46 import Solution

cases = [
    {
        'input': {
            'nums': [1, 2, 3],
        },
        'output': [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
    },
    {
        'input': {
            'nums': [0, 1],
        },
        'output': [[0, 1], [1, 0]],
    },
    {
        'input': {
            'nums': [1],
        },
        'output': [[1]],
    },
]


@pytest.mark.sol46
def test_run():
    for case in cases:
        assert Solution.permute(
            nums=case['input']['nums'],
        ) == case['output']
