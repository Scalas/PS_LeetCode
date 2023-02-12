import pytest
from solutions.sol_2477 import Solution

cases = [
    {
        'input': {
            'roads': [[0, 1], [0, 2], [0, 3]],
            'seats': 5,
        },
        'output': 3
    },
    {
        'input': {
            'roads': [[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]],
            'seats': 2,
        },
        'output': 7
    },
    {
        'input': {
            'roads': [],
            'seats': 1,
        },
        'output': 0
    },
]


@pytest.mark.sol_2477
def test_run():
    for case in cases:
        assert Solution.minimum_fuel_cost(
            roads=case['input']['roads'],
            seats=case['input']['seats']
        ) == case['output']
