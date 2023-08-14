import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_1372 import Solution

cases = [
    {
        "input": {
            "root": [
                1,
                None,
                1,
                1,
                1,
                None,
                None,
                1,
                1,
                None,
                1,
                None,
                None,
                None,
                1,
                None,
                1,
            ],
        },
        "output": 3,
    },
    {
        "input": {
            "root": [1, 1, 1, None, 1, None, None, 1, 1, None, 1],
        },
        "output": 4,
    },
    {
        "input": {
            "root": [1],
        },
        "output": 0,
    },
]


@pytest.mark.sol1372
def test_run():
    for case in cases:
        assert (
            Solution.longest_zig_zag(root=list_to_tree(case["input"]["root"]))
            == case["output"]
        )
