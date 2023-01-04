import pytest
from solutions.sol_2244 import Solution

cases = [
    {
        'input': {
            'tasks': [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
        },
        'output': 4
    },
    {
        'input': {
            'tasks': [2, 3, 3]
        },
        'output': -1
    },
]


@pytest.mark.sol_2244
def test_run():
    for case in cases:
        assert Solution.minimum_rounds(
            tasks=case['input']['tasks']
        ) == case['output']
