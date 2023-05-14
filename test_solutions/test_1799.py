import pytest
from solutions.sol_1799 import Solution

cases = [
    {
        'input': {
            'nums': [1, 2],
        },
        'output': 1,
    },
    {
        'input': {
            'nums': [3, 4, 6, 8],
        },
        'output': 11,
    },
    {
        'input': {
            'nums': [1, 2, 3, 4, 5, 6],
        },
        'output': 14,
    },
    {
        'input': {
            'nums': [171651, 546244, 880754, 412358],
        },
        'output': 60,
    },
    {
        'input': {
            'nums': [109497, 983516, 698308, 409009, 310455, 528595, 524079, 18036, 341150, 641864, 913962, 421869,
                     943382, 295019],
        },
        'output': 527,
    },
]


@pytest.mark.sol1799
def test_run():
    for case in cases:
        assert Solution.max_score(
            nums=case['input']['nums'],
        ) == case['output']
