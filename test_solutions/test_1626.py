import pytest
from solutions.sol_1626 import Solution

cases = [
    {
        'input': {
            'scores': [1, 3, 5, 10, 15],
            'ages': [1, 2, 3, 4, 5]
        },
        'output': 34
    },
    {
        'input': {
            'scores': [4, 5, 6, 5],
            'ages': [2, 1, 2, 1]
        },
        'output': 16
    },
    {
        'input': {
            'scores': [1, 2, 3, 5],
            'ages': [8, 9, 10, 1]
        },
        'output': 6
    },
]


@pytest.mark.sol1626
def test_run():
    for case in cases:
        assert Solution.best_team_score(
            scores=case['input']['scores'],
            ages=case['input']['ages']
        ) == case['output']
