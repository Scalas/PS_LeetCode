import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_606 import Solution

cases = [
    {"input": {"root": [1, 2, 3, 4]}, "output": "1(2(4))(3)"},
    {"input": {"root": [1, 2, 3, None, 4]}, "output": "1(2()(4))(3)"},
]


@pytest.mark.sol_605
def test_run():
    for case in cases:
        assert (
            Solution.tree2str(
                root=list_to_tree(case["input"]["root"]),
            )
            == case["output"]
        )
