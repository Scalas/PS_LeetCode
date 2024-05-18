import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_979 import Solution

cases = [
    {"input": {"root": [3, 0, 0]}, "output": 2},
    {"input": {"root": [0, 3, 0]}, "output": 3},
    {"input": {"root": [0, 2, 0, 0, 0, None, 0, None, None, 5]}, "output": 14},
    {"input": {"root": [0, 0, 2, 0, 0, None, 0, None, None, 5]}, "output": 10},
]


@pytest.mark.sol979
def test_run():
    for case in cases:
        assert (
            Solution.distribute_coins(root=list_to_tree(case["input"]["root"]))
            == case["output"]
        )
