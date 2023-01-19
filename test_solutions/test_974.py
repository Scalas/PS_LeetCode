import pytest
from solutions.sol_974 import Solution

cases = [
    {
        'input': {
            'nums': [4, 5, 0, -2, -3, 1],
            'k': 5
        },
        'output': 7
    },
    {
        'input': {
            'nums': [5],
            'k': 9
        },
        'output': 0
    },
]


@pytest.mark.sol974
def test_run():
    for case in cases:
        assert Solution.sub_arrays_div_by_k(
            nums=case['input']['nums'],
            k=case['input']['k']
        ) == case['output']
