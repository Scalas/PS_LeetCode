import pytest
from solutions.sol_989 import Solution

cases = [
    {
        'input': {
            'num': [1, 2, 0, 0],
            'k': 34,
        },
        'output': [1, 2, 3, 4]
    },
    {
        'input': {
            'num': [2, 7, 4],
            'k': 181,
        },
        'output': [4, 5, 5]
    },
    {
        'input': {
            'num': [2, 1, 5],
            'k': 806,
        },
        'output': [1, 0, 2, 1]
    },
]


@pytest.mark.sol989
def test_run():
    for case in cases:
        assert Solution.add_to_array_form(
            num=case['input']['num'],
            k=case['input']['k'],
        ) == case['output']
