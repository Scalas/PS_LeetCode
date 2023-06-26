import pytest
from solutions.sol_2462 import Solution

cases = [
    {
        'input': {
            'costs': [17,12,10,2,7,2,11,20,8],
            'k': 3,
            'candidates': 4
        },
        'output': 11,
    },
    {
        'input': {
            'costs': [1, 2, 4, 1],
            'k': 3,
            'candidates': 3
        },
        'output': 4,
    },
    {
        'input': {
            'costs': [31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58],
            'k': 11,
            'candidates': 2
        },
        'output': 423,
    },
]


@pytest.mark.sol_2462
def test_run():
    for case in cases:
        assert Solution.total_cost(
            costs=case['input']['costs'],
            k=case['input']['k'],
            candidates=case['input']['candidates'],
        ) == case['output']
