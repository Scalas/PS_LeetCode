import pytest

from solutions.sol_1361 import Solution

cases = [
    {
        "input": {
            "n": 4,
            "left_child": [1, -1, 3, -1],
            "right_child": [2, -1, -1, -1],
        },
        "output": True,
    },
    {
        "input": {
            "n": 4,
            "left_child": [1, -1, 3, -1],
            "right_child": [2, 3, -1, -1],
        },
        "output": False,
    },
    {
        "input": {
            "n": 2,
            "left_child": [1, 0],
            "right_child": [-1, -1],
        },
        "output": False,
    },
    {
        "input": {
            "n": 4,
            "left_child": [1, 0, 3, -1],
            "right_child": [-1, -1, -1, -1],
        },
        "output": False,
    },
    {
        "input": {
            "n": 3,
            "left_child": [1, -1, -1],
            "right_child": [-1, -1, 1],
        },
        "output": False,
    },
]


@pytest.mark.sol1361
def test_run():
    for case in cases:
        assert (
            Solution.validate_binary_tree_nodes(
                n=case["input"]["n"],
                left_child=case["input"]["left_child"],
                right_child=case["input"]["right_child"],
            )
            == case["output"]
        )
