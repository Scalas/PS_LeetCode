import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_988 import Solution

cases = [
    {
        "input": {
            "root": [0, 1, 2, 3, 4, 3, 4],
        },
        "output": "dba",
    },
    {
        "input": {
            "root": [25, 1, 3, 1, 3, 0, 2],
        },
        "output": "adz",
    },
    {
        "input": {
            "root": [2, 2, 1, None, 1, 0, None, 0],
        },
        "output": "abc",
    },
]


@pytest.mark.sol988
def test_run():
    for case in cases:
        assert (
            Solution.smallest_from_leaf(
                root=list_to_tree(case["input"]["root"]),
            )
            == case["output"]
        )
