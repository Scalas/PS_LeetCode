import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_1457 import Solution

cases = [
    {
        "input": {
            "root": [2, 3, 1, 3, 1, None, 1],
        },
        "output": 2,
    },
    {
        "input": {
            "root": [2, 1, 1, 1, 3, None, None, None, None, None, 1],
        },
        "output": 1,
    },
    {
        "input": {
            "root": [9],
        },
        "output": 1,
    },
]


@pytest.mark.sol1457
def test_run():
    for case in cases:
        assert (
            Solution.pseudo_palindromic_paths(
                root=list_to_tree(case["input"]["root"]),
            )
            == case["output"]
        )
