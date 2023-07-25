import pytest
from solutions.sol_852 import Solution

cases = [
    {
        'input': {
            'arr': [0, 1, 0]
        },
        'output': 1
    },
    {
        'input': {
            'arr': [0, 2, 1, 0]
        },
        'output': 1
    },
    {
        'input': {
            'arr': [0, 10, 5, 2]
        },
        'output': 1
    },
]


@pytest.mark.sol852
def test_run():
    for case in cases:
        assert Solution.peak_index_in_mountain_array(
            arr=case['input']['arr']
        ) == case['output']
