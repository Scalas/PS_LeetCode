import pytest
from solutions.sol_77 import Solution

cases = [
    {
        'input': {
            'n': 4,
            'k': 2,
        },
        'output': [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],
    },
    {
        'input': {
            'n': 1,
            'k': 1,
        },
        'output': [[1]],
    },
]


@pytest.mark.sol77
def test_run():
    for case in cases:
        assert Solution.combine(
            n=case['input']['n'],
            k=case['input']['k'],
        ) == case['output']
