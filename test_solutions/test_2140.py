import pytest
from solutions.sol_2140 import Solution

cases = [
    {
        'input': {
            'questions': [[3, 2], [4, 3], [4, 4], [2, 5]],
        },
        'output': 5,
    },
    {
        'input': {
            'questions': [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
        },
        'output': 7,
    },
]


@pytest.mark.sol_2140
def test_run():
    for case in cases:
        assert Solution.most_points(
            questions=case['input']['questions'],
        ) == case['output']
