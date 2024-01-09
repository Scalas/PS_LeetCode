import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_872 import Solution

cases = [
    {
        "input": {
            "root1": [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],
            "root2": [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8],
        },
        "output": True,
    },
    {
        "input": {
            "root1": [1, 2, 3],
            "root2": [1, 3, 2],
        },
        "output": False,
    },
]


@pytest.mark.sol872
def test_run():
    for case in cases:
        assert (
            Solution.leaf_similar(
                root1=list_to_tree(case["input"]["root1"]),
                root2=list_to_tree(case["input"]["root2"]),
            )
            == case["output"]
        )
