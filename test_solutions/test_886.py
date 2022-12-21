import pytest
from solutions.sol_886 import Solution

cases = [
    {
        'input': {
            'n': 4,
            'dislikes': [[1, 2], [1, 3], [2, 4]]
        },
        'output': True
    },
    {
        'input': {
            'n': 3,
            'dislikes': [[1, 2], [1, 3], [2, 3]]
        },
        'output': False
    },
    {
        'input': {
            'n': 5,
            'dislikes': [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
        },
        'output': False
    },
]


@pytest.mark.sol886
def test_run():
    for case in cases:
        assert Solution.possible_bi_partition(
            n=case['input']['n'],
            dislikes=case['input']['dislikes']
        ) == case['output']
