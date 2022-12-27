import pytest
from solutions.sol_2279 import Solution

cases = [
    {
        'input': {
            'capacity': [2, 3, 4, 5],
            'rocks': [1, 2, 4, 4],
            'additional_rocks': 2,
        },
        'output': 3
    },
    {
        'input': {
            'capacity': [10, 2, 2],
            'rocks': [2, 2, 0],
            'additional_rocks': 100,
        },
        'output': 3
    },
]


@pytest.mark.sol_2279
def test_run():
    for case in cases:
        assert Solution.maximum_bags(
            capacity=case['input']['capacity'],
            rocks=case['input']['rocks'],
            additional_rocks=case['input']['additional_rocks'],
        ) == case['output']
