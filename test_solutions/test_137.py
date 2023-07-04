import pytest
from solutions.sol_137 import Solution

cases = [
    {
        'input': {
            'nums': [2, 2, 3, 2],
        },
        'output': 3
    },
    {
        'input': {
            'nums': [0, 1, 0, 1, 0, 1, 99],
        },
        'output': 99
    },
]


@pytest.mark.sol137
def test_run():
    for case in cases:
        assert Solution.single_number(
            nums=case['input']['nums'],
        ) == case['output']
