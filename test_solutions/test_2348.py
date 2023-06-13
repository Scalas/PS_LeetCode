import pytest
from solutions.sol_2348 import Solution

cases = [
    {
        'input': {
            'nums': [1, 3, 0, 0, 2, 0, 0, 4],
        },
        'output': 6,
    },
    {
        'input': {
            'nums': [0, 0, 0, 2, 0, 0],
        },
        'output': 9,
    },
    {
        'input': {
            'nums': [2, 10, 2019],
        },
        'output': 0,
    },
]


@pytest.mark.sol_2348
def test_run():
    for case in cases:
        assert Solution.zero_filled_sub_array(
            nums=case['input']['nums'],
        ) == case['output']
