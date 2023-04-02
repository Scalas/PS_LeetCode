import pytest
from solutions.sol_2300 import Solution

cases = [
    {
        'input': {
            'spells': [5, 1, 3],
            'potions': [1, 2, 3, 4, 5],
            'success': 7,
        },
        'output': [4, 0, 3],
    },
    {
        'input': {
            'spells': [3, 1, 2],
            'potions': [8, 5, 8],
            'success': 16,
        },
        'output': [2, 0, 2],
    },
]


@pytest.mark.sol_2300
def test_run():
    for case in cases:
        assert Solution.successful_pairs(
            spells=case['input']['spells'],
            potions=case['input']['potions'],
            success=case['input']['success'],
        ) == case['output']
