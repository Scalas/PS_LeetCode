import pytest
from solutions.sol_839 import Solution

cases = [
    {
        'input': {
            'strs': ['tars', 'rats', 'arts', 'star'],
        },
        'output': 2,
    },
    {
        'input': {
            'strs': ['omv', 'ovm'],
        },
        'output': 1,
    },
]


@pytest.mark.sol_839
def test_run():
    for case in cases:
        assert Solution.num_similar_groups(
            strs=case['input']['strs']
        ) == case['output']
