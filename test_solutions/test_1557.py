import pytest
from solutions.sol_1557 import Solution

cases = [
    {
        'input': {
            'n': 6,
            'edges': [[0,1],[0,2],[2,5],[3,4],[4,2]],
        },
        'output': {0, 3},
    },
    {
        'input': {
            'n': 5,
            'edges': [[0,1],[2,1],[3,1],[1,4],[2,4]],
        },
        'output': {0, 2, 3},
    },
]


@pytest.mark.sol1557
def test_run():
    for case in cases:
        assert Solution.find_smallest_set_of_vertices(
            n=case['input']['n'],
            edges=case['input']['edges'],
        ) == case['output']
