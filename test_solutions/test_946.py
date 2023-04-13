import pytest
from solutions.sol_946 import Solution

cases = [
    {
        'input': {
            'pushed': [1, 2, 3, 4, 5],
            'popped': [4, 5, 3, 2, 1],
        },
        'output': True,
    },
    {
        'input': {
            'pushed': [1, 2, 3, 4, 5],
            'popped': [4, 3, 5, 1, 2],
        },
        'output': False,
    },
]


@pytest.mark.sol946
def test_run():
    for case in cases:
        assert Solution.validate_stack_sequences(
            pushed=case['input']['pushed'],
            popped=case['input']['popped']
        ) == case['output']
