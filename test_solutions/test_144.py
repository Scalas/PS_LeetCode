import pytest
from solutions.sol_144 import Solution
from converter.leet_code_utils import list_to_tree

cases = [
    {"input": {"root": [1, None, 2, 3]}, "output": [1, 2, 3]},
    {"input": {"root": []}, "output": []},
    {"input": {"root": [1]}, "output": [1]},
]


@pytest.mark.sol144
def test_run():
    for case in cases:
        assert (
            Solution.preorder_traversal(root=list_to_tree(case["input"]["root"]))
            == case["output"]
        )
