import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_2583 import Solution


cases = [
    {
        "input": {"root": [5, 8, 9, 2, 1, 3, 7, 4, 6], "k": 2},
        "output": 13,
    },
    {
        "input": {"root": [1, 2, None, 3], "k": 1},
        "output": 3,
    },
]


@pytest.mark.sol2583
def test_run():
    for case in cases:
        assert (
            Solution.kth_largest_level_sum(
                root=list_to_tree(case["input"]["root"]),
                k=case["input"]["k"],
            )
            == case["output"]
        )
