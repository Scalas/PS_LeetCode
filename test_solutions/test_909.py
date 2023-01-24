import pytest
from solutions.sol_909 import Solution

cases = [
    {
        'input': {
            'board': [
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 35, -1, -1, 13, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 15, -1, -1, -1, -1]
            ]
        },
        'output': 4
    },
    {
        'input': {
            'board': [
                [-1, -1],
                [-1, 3]
            ]
        },
        'output': 1
    },
]


@pytest.mark.sol909
def test_run():
    for case in cases:
        assert Solution.snakes_and_ladders(
            board=case['input']['board']
        ) == case['output']
