import pytest
from solutions.sol_1658 import Solution

cases = [
    {
        "input": {
            "nums": [1, 1, 4, 2, 3],
            "x": 5,
        },
        "output": 2,
    },
    {
        "input": {
            "nums": [5, 6, 7, 8, 9],
            "x": 4,
        },
        "output": -1,
    },
    {
        "input": {
            "nums": [3, 2, 20, 1, 1, 3],
            "x": 10,
        },
        "output": 5,
    },
    {
        "input": {
            "nums": [1, 1],
            "x": 3,
        },
        "output": -1,
    },
    {
        "input": {
            "nums": [1, 2, 3],
            "x": 6,
        },
        "output": 3,
    },
]


@pytest.mark.sol1658
def test_run():
    for case in cases:
        assert (
            Solution.min_operations(
                nums=case["input"]["nums"],
                x=case["input"]["x"],
            )
            == case["output"]
        )
