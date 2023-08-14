import pytest
from solutions.sol_104 import Solution
from converter.leet_code_utils import list_to_tree

cases = [
    {
        "input": {
            "root": [3, 9, 20, None, None, 15, 7],
        },
        "output": 3,
    },
    {
        "input": {
            "root": [1, None, 2],
        },
        "output": 2,
    },
]


@pytest.mark.sol104
def test_run():
    for case in cases:
        assert (
            Solution.max_depth(
                root=list_to_tree(case["input"]["root"]),
            )
            == case["output"]
        )
