import pytest
from solutions.sol_59 import Solution

cases = [
    {
        'input': {
            'n': 3,
        },
        'output': [[1, 2, 3], [8, 9, 4], [7, 6, 5]],
    },
    {
        'input': {
            'n': 1,
        },
        'output': [[1]],
    },
]


@pytest.mark.sol59
def test_run():
    for case in cases:
        assert Solution.generate_matrix(
            n=case['input']['n'],
        ) == case['output']
