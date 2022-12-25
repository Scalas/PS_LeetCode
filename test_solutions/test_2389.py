import pytest
from solutions.sol_2389 import Solution

cases = [
    {
        'input': {
            'nums': [4, 5, 2, 1],
            'queries': [3, 10, 21],
        },
        'output': [2, 3, 4]
    },
    {
        'input': {
            'nums': [2, 3, 4, 5],
            'queries': [1],
        },
        'output': [0]
    },
    {
        'input': {
            'nums': [736411, 184882, 914641, 37925, 214915],
            'queries': [331244, 273144, 118983, 118252, 305688, 718089, 665450],
        },
        'output': [2, 2, 1, 1, 2, 3, 3]
    },
]


@pytest.mark.sol_2389
def test_run():
    for case in cases:
        assert Solution.answer_queries(
            nums=case['input']['nums'],
            queries=case['input']['queries']
        ) == case['output']
