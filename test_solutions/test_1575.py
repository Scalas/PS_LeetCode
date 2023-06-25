import pytest
from solutions.sol_1575 import Solution

cases = [
    {
        'input': {
            'locations': [2,3,6,8,4],
            'start': 1,
            'finish': 3,
            'fuel': 5,
        },
        'output': 4
    },
    {
        'input': {
            'locations': [4, 3, 1],
            'start': 1,
            'finish': 0,
            'fuel': 6,
        },
        'output': 5,
    },
    {
        'input': {
            'locations': [5, 2, 1],
            'start': 0,
            'finish': 2,
            'fuel': 3,
        },
        'output': 0,
    },
]


@pytest.mark.sol1575
def test_run():
    for case in cases:
        assert Solution.count_routes(
            locations=case['input']['locations'],
            start=case['input']['start'],
            finish=case['input']['finish'],
            fuel=case['input']['fuel'],
        ) == case['output']
