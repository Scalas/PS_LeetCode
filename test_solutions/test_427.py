import pytest
from solutions.sol_427 import Solution
from converter.leet_code_utils import list_to_quad_tree, compare_quad_tree

cases = [
    {
        'input': {
            'grid': [[0, 1], [1, 0]],
        },
        'output': list_to_quad_tree([[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]])
    },
    {
        'input': {
            'grid': [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0],
                     [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]],
        },
        'output': list_to_quad_tree(
            [[0, 1], [1, 1], [0, 1], [1, 1], [1, 0], None, None, None, None, [1, 0], [1, 0], [1, 1], [1, 1]])
    },
]


@pytest.mark.sol_427
def test_run():
    for case in cases:
        assert compare_quad_tree(Solution.construct(
            grid=case['input']['grid'],
        ), case['output'])
