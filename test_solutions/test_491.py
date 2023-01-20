import pytest
from solutions.sol_491 import Solution

cases = [
    {
        'input': {
            'nums': [4, 6, 7, 7]
        },
        'output': [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]
    },
    {
        'input': {
            'nums': [4, 4, 3, 2, 1]
        },
        'output': [[4, 4]]
    },
]


@pytest.mark.sol_491
def test_run():
    for case in cases:
        assert set(Solution.find_subsequences(
            nums=case['input']['nums']
        )) == set(map(tuple, case['output']))
