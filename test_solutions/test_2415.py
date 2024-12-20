import pytest

from converter.leet_code_utils import list_to_tree, compare_tree
from solutions.sol_2415 import Solution


cases = [
    {
        "input": {"root": [2, 3, 5, 8, 13, 21, 34]},
        "output": [2, 5, 3, 8, 13, 21, 34],
    },
    {
        "input": {"root": [7, 13, 11]},
        "output": [7, 11, 13],
    },
    {
        "input": {"root": [0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]},
        "output": [0, 2, 1, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1],
    },
]


@pytest.mark.sol2415
def test_run():
    for case in cases:
        assert compare_tree(
            Solution.reverse_odd_levels(
                root=list_to_tree(case["input"]["root"]),
            ),
            list_to_tree(case["output"]),
        )
