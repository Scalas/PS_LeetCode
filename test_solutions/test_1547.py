import pytest
from solutions.sol_1547 import Solution

cases = [
    {
        'input': {
            'n': 7,
            'cuts': [1, 3, 4, 5],
        },
        'output': 16
    },
    {
        'input': {
            'n': 9,
            'cuts': [5, 6, 1, 4, 2],
        },
        'output': 22
    },
    {
        'input': {
            'n': 30,
            'cuts': [18, 15, 13, 7, 5, 26, 25, 29],
        },
        'output': 92
    },
]


@pytest.mark.sol1547
def test_run():
    for case in cases:
        assert Solution.min_cost(
            n=case['input']['n'],
            cuts=case['input']['cuts'],
        ) == case['output']
