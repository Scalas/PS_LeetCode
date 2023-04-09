import pytest
from solutions.sol_1857 import Solution

cases = [
    {
        'input': {
            'colors': 'abaca',
            'edges': [[0, 1], [0, 2], [2, 3], [3, 4]],
        },
        'output': 3,
    },
    {
        'input': {
            'colors': 'a',
            'edges': [[0, 0]],
        },
        'output': -1,
    },
]


@pytest.mark.sol1857
def test_run():
    for case in cases:
        assert Solution.largest_path_value(
            colors=case['input']['colors'],
            edges=case['input']['edges']
        ) == case['output']
