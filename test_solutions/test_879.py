import pytest
from solutions.sol_879 import Solution

cases = [
    {
        'input': {
            'n': 5,
            'min_profit': 3,
            'group': [2, 2],
            'profit': [2, 3],
        },
        'output': 2,
    },
    {
        'input': {
            'n': 10,
            'min_profit': 5,
            'group': [2, 3, 5],
            'profit': [6, 7, 8],
        },
        'output': 7,
    },
]


@pytest.mark.sol879
def test_run():
    for case in cases:
        assert Solution.profitable_schemes(
            n=case['input']['n'],
            min_profit=case['input']['min_profit'],
            group=case['input']['group'],
            profit=case['input']['profit'],
        ) == case['output']
