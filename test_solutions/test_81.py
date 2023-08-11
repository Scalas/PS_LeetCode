import pytest
from solutions.sol_81 import Solution

cases = [
    {
        'input': {
            'nums': [2, 5, 6, 0, 0, 1, 2],
            'target': 0,
        },
        'output': True,
    },
    {
        'input': {
            'nums': [2, 5, 6, 0, 0, 1, 2],
            'target': 3,
        },
        'output': False,
    },
]


@pytest.mark.sol81
def test_run():
    for case in cases:
        assert Solution.search(
            nums=case['input']['nums'],
            target=case['input']['target'],
        ) == case['output']
