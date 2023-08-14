import pytest
from solutions.sol_101 import Solution
from converter.leet_code_utils import list_to_tree

cases = [
    {
        "input": {
            "root": [1, 2, 2, 3, 4, 4, 3],
        },
        "output": True,
    },
    {
        "input": {
            "root": [1, 2, 2, None, 3, None, 3],
        },
        "output": False,
    },
]


@pytest.mark.sol101
def test_run():
    for case in cases:
        assert (
            Solution.is_symmetric(
                root=list_to_tree(case["input"]["root"]),
            )
            == case["output"]
        )
