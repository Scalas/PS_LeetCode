import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_145 import Solution


cases = [
    {
        "input": {"root": [1, None, 2, 3]},
        "output": [3, 2, 1],
    },
    {
        "input": {"root": []},
        "output": [],
    },
    {
        "input": {"root": [1]},
        "output": [1],
    },
]


@pytest.mark.sol145
def test_run():
    for case in cases:
        assert (
            Solution.postorder_traversal(
                root=list_to_tree(case["input"]["root"]),
            )
            == case["output"]
        )
