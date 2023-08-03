import pytest

from solutions.sol_26 import Solution

cases = [
    {
        'input': {
            'nums': [1, 1, 2],
        },
        'output': [2, [1, 2, 2]],
    },
    {
        'input': {
            'nums': [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        },
        'output': [5, [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]],
    },
]


@pytest.mark.sol26
def test_run():
    for case in cases:
        assert Solution.remove_duplicates(
            nums=case['input']['nums'],
        ) == case['output'][0]
        assert case['input']['nums'] == case['output'][1]
