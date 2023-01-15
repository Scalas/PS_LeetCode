import pytest
from solutions.sol_2421 import Solution

cases = [
    {
        'input': {
            'vals': [1,3,2,1,3],
            'edges': [[0,1],[0,2],[2,3],[2,4]],
        },
        'output': 6
    },
    {
        'input': {
            'vals': [1,1,2,2,3],
            'edges': [[0,1],[1,2],[2,3],[2,4]],
        },
        'output': 7
    },
    {
        'input': {
            'vals': [1],
            'edges': [],
        },
        'output': 1
    },
]


@pytest.mark.sol_2421
def test_run():
    for case in cases:
        assert Solution.number_of_good_paths(
            vals=case['input']['vals'],
            edges=case['input']['edges']
        ) == case['output']
