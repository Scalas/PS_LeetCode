import pytest
from solutions.sol_540 import Solution

cases = [
    {
        'input': {
            'nums': [1, 1, 2, 3, 3, 4, 4, 8, 8],
        },
        'output': 2,
    },
    {
        'input': {
            'nums': [3, 3, 7, 7, 10, 11, 11],
        },
        'output': 10,
    },
]


@pytest.mark.sol_540
def test_run():
    for case in cases:
        assert Solution.single_non_duplicate(
            nums=case['input']['nums'],
        ) == case['output']
