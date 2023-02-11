import pytest
from solutions.sol_1129 import Solution

cases = [
    {
        'input': {
            'n': 3,
            'red_edges': [[0, 1], [1, 2]],
            'blue_edges': [],
        },
        'output': [0, 1, -1]
    },
    {
        'input': {
            'n': 3,
            'red_edges': [[0, 1]],
            'blue_edges': [[2, 1]],
        },
        'output': [0, 1, -1]
    },
]


@pytest.mark.sol1129
def test_run():
    for case in cases:
        assert Solution.shortest_alternating_paths(
            n=case['input']['n'],
            red_edges=case['input']['red_edges'],
            blue_edges=case['input']['blue_edges'],
        ) == case['output']
