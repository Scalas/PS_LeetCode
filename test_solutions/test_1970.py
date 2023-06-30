import pytest
from solutions.sol_1970 import Solution

cases = [
    {
        'input': {
            'row': 2,
            'col': 2,
            'cells': [[1, 1], [2, 1], [1, 2], [2, 2]],
        },
        'output': 2,
    },
    {
        'input': {
            'row': 2,
            'col': 2,
            'cells': [[1, 1], [1, 2], [2, 1], [2, 2]],
        },
        'output': 1,
    },
    {
        'input': {
            'row': 3,
            'col': 3,
            'cells': [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]],
        },
        'output': 3,
    },
]


@pytest.mark.sol1970
def test_run():
    for case in cases:
        assert Solution.latest_day_to_cross(
            row=case['input']['row'],
            col=case['input']['col'],
            cells=case['input']['cells'],
        ) == case['output']
