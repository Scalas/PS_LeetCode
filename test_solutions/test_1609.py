import pytest
from solutions.sol_1609 import Solution
from converter.leet_code_utils import list_to_tree

cases = [
    {
        "input": {"root": [1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2]},
        "output": True,
    },
    {"input": {"root": [5, 4, 2, 3, 3, 7]}, "output": False},
    {"input": {"root": [5, 9, 1, 3, 5, 7]}, "output": False},
]


@pytest.mark.sol1609
def test_run():
    for case in cases:
        assert (
            Solution.is_even_odd_tree(root=list_to_tree(case["input"]["root"]))
            == case["output"]
        )
