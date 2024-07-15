import pytest

from converter.leet_code_utils import compare_tree, list_to_tree
from solutions.sol_2196 import Solution


cases = [
    {
        "input": {
            "descriptions": [
                [20, 15, 1],
                [20, 17, 0],
                [50, 20, 1],
                [50, 80, 0],
                [80, 19, 1],
            ]
        },
        "output": [50, 20, 80, 15, 17, 19],
    },
    {
        "input": {"descriptions": [[1, 2, 1], [2, 3, 0], [3, 4, 1]]},
        "output": [1, 2, None, None, 3, 4],
    },
]


@pytest.mark.sol2196
def test_run():
    for case in cases:
        assert compare_tree(
            Solution.create_binary_tree(
                descriptions=case["input"]["descriptions"],
            ),
            list_to_tree(case["output"]),
        )
