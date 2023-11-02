import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_2265 import Solution

cases = [
    {
        "input": {"root": [4, 8, 5, 0, 1, None, 6]},
        "output": 5,
    },
    {"input": {"root": [1]}, "output": 1},
]


@pytest.mark.sol_2265
def test_run():
    for case in cases:
        assert (
            Solution.average_of_subtree(root=list_to_tree(case["input"]["root"]))
            == case["output"]
        )
