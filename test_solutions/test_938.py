import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_938 import Solution

cases = [
    {
        "input": {
            "root": [10, 5, 15, 3, 7, None, 18],
            "low": 7,
            "high": 15,
        },
        "output": 32,
    },
    {
        "input": {
            "root": [10, 5, 15, 3, 7, 13, 18, 1, None, 6],
            "low": 6,
            "high": 10,
        },
        "output": 23,
    },
]


@pytest.mark.sol938
def test_run():
    for case in cases:
        assert (
            Solution.range_sum_bst(
                root=list_to_tree(case["input"]["root"]),
                low=case["input"]["low"],
                high=case["input"]["high"],
            )
            == case["output"]
        )
