import pytest
from solutions.sol_944 import Solution

cases = [
    {
        'input': {
            'strs': ["cba", "daf", "ghi"]
        },
        'output': 1
    },
    {
        'input': {
            'strs': ["a", "b"]
        },
        'output': 0
    },
    {
        'input': {
            'strs': ["zyx", "wvu", "tsr"]
        },
        'output': 3
    },
]


@pytest.mark.sol944
def test_run():
    for case in cases:
        assert Solution.min_deletion_size(
            strs=case['input']['strs']
        ) == case['output']
