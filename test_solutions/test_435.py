import pytest
from solutions.sol_435 import Solution

cases = [
    {
        'input': {
            'intervals': [[1, 2], [2, 3], [3, 4], [1, 3]],
        },
        'output': 1,
    },
    {
        'input': {
            'intervals': [[1, 2], [1, 2], [1, 2]],
        },
        'output': 2,
    },
    {
        'input': {
            'intervals': [[1, 2], [2, 3]],
        },
        'output': 0,
    },
]


@pytest.mark.sol_435
def test_run():
    for case in cases:
        assert Solution.erase_overlap_intervals(
            intervals=case['input']['intervals'],
        ) == case['output']
