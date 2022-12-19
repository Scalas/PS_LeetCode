import pytest
from solutions.sol_1971 import Solution

cases = [
    {
        'input': {
            'n': 3,
            'edges': [[0, 1], [1, 2], [2, 0]],
            'source': 0,
            'destination': 2,
        },
        'output': True
    },
    {
        'input': {
            'n': 3,
            'edges': [[0, 1], [1, 2], [2, 0]],
            'source': 0,
            'destination': 2,
        },
        'output': True
    },
    {
        'input': {
            'n': 6,
            'edges': [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]],
            'source': 0,
            'destination': 5,
        },
        'output': False
    },
]


@pytest.mark.sol_1971
def test_run():
    for case in cases:
        assert Solution.valid_path(
            n=case['input']['n'],
            edges=case['input']['edges'],
            source=case['input']['source'],
            destination=case['input']['destination']
        ) == case['output']
