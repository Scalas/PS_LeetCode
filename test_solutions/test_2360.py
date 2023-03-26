import pytest
from solutions.sol_2360 import Solution

cases = [
    {
        'input': {
            'edges': [3, 3, 4, 2, 3],
        },
        'output': 3,
    },
    {
        'input': {
            'edges': [2, -1, 3, 1],
        },
        'output': -1,
    },
]


@pytest.mark.sol_2360
def test_run():
    for case in cases:
        assert Solution.longest_cycle(
            edges=case['input']['edges'],
        ) == case['output']
