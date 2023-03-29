import pytest
from solutions.sol_1402 import Solution

cases = [
    {
        'input': {
            'satisfaction': [-1, -8, 0, 5, -9],
        },
        'output': 14,
    },
    {
        'input': {
            'satisfaction': [4, 3, 2],
        },
        'output': 20,
    },
    {
        'input': {
            'satisfaction': [-1, -4, -5],
        },
        'output': 0,
    },
]


@pytest.mark.sol1402
def test_run():
    for case in cases:
        assert Solution.max_satisfaction(
            satisfaction=case['input']['satisfaction']
        ) == case['output']
