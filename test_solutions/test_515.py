import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_515 import Solution

cases = [
    {"input": {"root": [1, 3, 2, 5, 3, None, 9]}, "output": [1, 3, 9]},
    {"input": {"root": [1, 2, 3]}, "output": [1, 3]},
    {"input": {"root": []}, "output": []},
    {"input": {"root": [1, -1]}, "output": [1, -1]},
]


@pytest.mark.sol_515
def test_run():
    for case in cases:
        assert (
            Solution.largest_values(root=list_to_tree(case["input"]["root"]))
            == case["output"]
        )
