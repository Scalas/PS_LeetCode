import pytest
from solutions.sol_121 import Solution

cases = [
    {
        'input': {
            'prices': [7, 1, 5, 3, 6, 4],
        },
        'output': 5
    },
    {
        'input': {
            'prices': [7, 6, 4, 3, 1],
        },
        'output': 0
    },
]


@pytest.mark.sol121
def test_run():
    for case in cases:
        assert Solution.max_profit(
            prices=case['input']['prices'],
        ) == case['output']
