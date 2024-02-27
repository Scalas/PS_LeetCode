import pytest

from converter.leet_code_utils import list_to_tree
from solutions.sol_543 import Solution

cases = [
    {"input": {"root": [1, 2, 3, 4, 5]}, "output": 3},
    {"input": {"root": [1, 2]}, "output": 1},
    {
        "input": {
            "root": [
                4,
                -7,
                -3,
                None,
                None,
                -9,
                -3,
                9,
                -7,
                -4,
                None,
                6,
                None,
                -6,
                -6,
                None,
                None,
                0,
                6,
                5,
                None,
                9,
                None,
                None,
                -1,
                -4,
                None,
                None,
                None,
                -2,
            ]
        },
        "output": 8,
    },
]


@pytest.mark.sol_543
def test_run():
    for case in cases:
        assert (
            Solution.diameter_of_binary_tree(
                root=list_to_tree(case["input"]["root"]),
            )
            == case["output"]
        )
