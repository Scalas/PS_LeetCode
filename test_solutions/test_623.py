import pytest

from converter.leet_code_utils import list_to_tree, compare_tree
from solutions.sol_623 import Solution

cases = [
    {
        "input": {"root": [4, 2, 6, 3, 1, 5], "val": 1, "depth": 2},
        "output": [4, 1, 1, 2, None, None, 6, 3, 1, 5],
    },
    {
        "input": {"root": [4, 2, None, 3, 1], "val": 1, "depth": 3},
        "output": [4, 2, None, 1, 1, 3, None, None, 1],
    },
    {
        "input": {"root": [4, 2, 6, None, 3, 1, 5], "val": 1, "depth": 2},
        "output": [4, 1, 1, 2, None, None, 6, None, 3, 1, 5],
    },
    {
        "input": {"root": [4, 2, 6, 3, 1, 5], "val": 1, "depth": 1},
        "output": [1, 4, None, 2, 6, 3, 1, 5],
    },
]


@pytest.mark.sol_623
def test_run():
    for case in cases:
        assert compare_tree(
            Solution.add_one_row(
                root=list_to_tree(case["input"]["root"]),
                val=case["input"]["val"],
                depth=case["input"]["depth"],
            ),
            list_to_tree(case["output"]),
        )
