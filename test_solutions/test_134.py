import pytest
from solutions.sol_134 import Solution

cases = [
    {
        'input': {
            'gas': [1, 2, 3, 4, 5],
            'cost': [3, 4, 5, 1, 2]
        },
        'output': 3
    },
    {
        'input': {
            'gas': [2, 3, 4],
            'cost': [3, 4, 3]
        },
        'output': -1
    },
]


@pytest.mark.sol134
def test_run():
    for case in cases:
        assert Solution.can_complete_circuit(
            gas=case['input']['gas'],
            cost=case['input']['cost']
        ) == case['output']
