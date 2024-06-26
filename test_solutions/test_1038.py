import pytest

from converter.leet_code_utils import list_to_tree, compare_tree
from solutions.sol_1038 import Solution


cases = [
    {
        "input": {
            "root": [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
        },
        "output": [
            30,
            36,
            21,
            36,
            35,
            26,
            15,
            None,
            None,
            None,
            33,
            None,
            None,
            None,
            8,
        ],
    },
    {
        "input": {"root": [0, None, 1]},
        "output": [1, None, 1],
    },
]


@pytest.mark.sol1038
def test_run():
    for case in cases:
        assert compare_tree(
            Solution.bst_to_gst(
                root=list_to_tree(case["input"]["root"]),
            ),
            list_to_tree(case["output"]),
        )
