import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_2331 import Solution

cases = [
    {
        "input": {
            "root": [2, 1, 3, None, None, 0, 1],
        },
        "output": True,
    },
    {
        "input": {
            "root": [0],
        },
        "output": False,
    },
]


@pytest.mark.sol_2331
def test_run():
    for case in cases:
        assert (
            Solution.evaluate_tree(
                root=list_to_tree(case["input"]["root"]),
            )
            == case["output"]
        )
