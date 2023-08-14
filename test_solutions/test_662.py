import pytest
from solutions.sol_662 import Solution
from converter.leet_code_utils import list_to_tree

cases = [
    {
        "input": {
            "root": [1, 3, 2, 5, 3, None, 9],
        },
        "output": 4,
    },
    {
        "input": {
            "root": [1, 3, 2, 5, None, None, 9, 6, None, 7],
        },
        "output": 7,
    },
    {
        "input": {
            "root": [1, 3, 2, 5],
        },
        "output": 2,
    },
]


@pytest.mark.sol_662
def test_run():
    for case in cases:
        assert (
            Solution.width_of_binary_tree(
                root=list_to_tree(case["input"]["root"]),
            )
            == case["output"]
        )
