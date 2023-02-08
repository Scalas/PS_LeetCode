import pytest
from solutions.sol_45 import Solution

cases = [
    {
        'input': {
            'nums': [2, 3, 1, 1, 4],
        },
        'output': 2
    },
    {
        'input': {
            'nums': [2, 3, 0, 1, 4],
        },
        'output': 2
    },
]


@pytest.mark.sol45
def test_run():
    for case in cases:
        assert Solution.jump(
            nums=case['input']['nums'],
        ) == case['output']
