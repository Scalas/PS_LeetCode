import pytest
from solutions.sol_226 import Solution
from converter.leet_code_utils import list_to_tree, compare_tree

cases = [
    {
        "input": {
            "root": [4, 2, 7, 1, 3, 6, 9],
        },
        "output": [4, 7, 2, 9, 6, 3, 1],
    },
    {
        "input": {
            "root": [2, 1, 3],
        },
        "output": [2, 3, 1],
    },
    {
        "input": {
            "root": [],
        },
        "output": [],
    },
]


@pytest.mark.sol226
def test_run():
    for case in cases:
        assert (
            compare_tree(
                Solution.invert_tree(
                    root=list_to_tree(case["input"]["root"]),
                ),
                list_to_tree(case["output"]),
            )
            == True
        )
