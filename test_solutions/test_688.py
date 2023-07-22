import pytest
from solutions.sol_688 import Solution

cases = [
    {
        'input': {
            'n': 3,
            'k': 2,
            'row': 0,
            'column': 0,
        },
        'output': 0.06250,
    },
    {
        'input': {
            'n': 1,
            'k': 0,
            'row': 0,
            'column': 0,
        },
        'output': 1.00000,
    },
]


@pytest.mark.sol_688
def test_run():
    for case in cases:
        assert Solution.knight_probability(
            n=case['input']['n'],
            k=case['input']['k'],
            row=case['input']['row'],
            column=case['input']['column'],
        ) == case['output']
