import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_1026 import Solution

cases = [
    {
        "input": {
            "root": [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13],
        },
        "output": 7,
    },
    {
        "input": {
            "root": [1, None, 2, None, 0, 3],
        },
        "output": 3,
    },
]


@pytest.mark.sol1026
def test_run():
    for case in cases:
        assert (
            Solution.max_ancestor_diff(
                root=list_to_tree(case["input"]["root"]),
            )
            == case["output"]
        )
