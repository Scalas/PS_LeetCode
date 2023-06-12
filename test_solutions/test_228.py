import pytest
from solutions.sol_228 import Solution

cases = [
    {
        'input': {
            'nums': [0, 1, 2, 4, 5, 7],
        },
        'output': ["0->2", "4->5", "7"],
    },
    {
        'input': {
            'nums': [0, 2, 3, 4, 6, 8, 9]
        },
        'output': ["0", "2->4", "6", "8->9"]
    },
    {
        'input': {
            'nums': []
        },
        'output': []
    }
]


@pytest.mark.sol228
def test_run():
    for case in cases:
        assert Solution.summary_ranges(
            nums=case['input']['nums']
        ) == case['output']
