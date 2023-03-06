import pytest
from solutions.sol_1539 import Solution

cases = [
    {
        'input': {
            'arr': [2, 3, 4, 7, 11],
            'k': 5,
        },
        'output': 9
    },
    {
        'input': {
            'arr': [1, 2, 3, 4],
            'k': 2,
        },
        'output': 6
    },
]


@pytest.mark.sol1539
def test_run():
    for case in cases:
        assert Solution.find_kth_positive(
            arr=case['input']['arr'],
            k=case['input']['k'],
        ) == case['output']
