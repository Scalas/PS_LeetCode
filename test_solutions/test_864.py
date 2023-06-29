import pytest
from solutions.sol_864 import Solution

cases = [
    {
        'input': {
            'grid': ["@.a..", "###.#", "b.A.B"],
        },
        'output': 8
    },
    {
        'input': {
            'grid': ["@..aA", "..B#.", "....b"],
        },
        'output': 6
    },
    {
        'input': {
            'grid': ["@Aa"],
        },
        'output': -1
    },
]


@pytest.mark.sol864
def test_run():
    for case in cases:
        assert Solution.shortest_path_all_keys(
            grid=case['input']['grid']
        ) == case['output']
