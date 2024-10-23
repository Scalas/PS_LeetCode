import pytest

from converter.leet_code_utils import list_to_tree, compare_tree
from solutions.sol_2641 import Solution


cases = [
    {
        "input": {"root": [5, 4, 9, 1, 10, None, 7]},
        "output": [0, 0, 0, 7, 7, None, 11],
    },
    {
        "input": {"root": [3, 1, 2]},
        "output": [0, 0, 0],
    },
]


@pytest.mark.sol2641
def test_run():
    for case in cases:
        assert compare_tree(
            Solution.replace_value_in_tree(
                root=list_to_tree(case["input"]["root"]),
            ),
            list_to_tree(case["output"]),
        )
