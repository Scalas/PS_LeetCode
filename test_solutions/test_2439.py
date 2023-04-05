import pytest
from solutions.sol_2439 import Solution

cases = [
    {
        'input': {
            'nums': [3, 7, 1, 6],
        },
        'output': 5
    },
    {
        'input': {
            'nums': [10, 1],
        },
        'output': 10,
    },
]


@pytest.mark.sol_2439
def test_run():
    for case in cases:
        assert Solution.minimize_array_value(
            nums=case['input']['nums'],
        ) == case['output']
