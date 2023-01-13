import pytest
from solutions.sol_2246 import Solution

cases = [
    {
        'input': {
            'parent': [-1, 0, 0, 1, 1, 2],
            's': 'abacbe'
        },
        'output': 3
    },
    {
        'input': {
            'parent': [-1, 0, 0, 0],
            's': 'aabc'
        },
        'output': 3
    },
]


@pytest.mark.sol_2246
def test_run():
    for case in cases:
        assert Solution.longest_path(
            parent=case['input']['parent'],
            s=case['input']['s']
        ) == case['output']
