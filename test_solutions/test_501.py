import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_501 import Solution

cases = [
    {
        "input": {"root": [1, None, 2, 2]},
        "output": [2],
    },
    {"input": {"root": [0]}, "output": [0]},
]


@pytest.mark.sol_501
def test_run():
    for case in cases:
        assert (
            Solution.find_mode(root=list_to_tree(case["input"]["root"]))
            == case["output"]
        )
