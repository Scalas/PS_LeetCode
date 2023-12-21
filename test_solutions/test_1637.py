import pytest
from solutions.sol_1637 import Solution

cases = [
    {
        "input": {
            "points": [[8, 7], [9, 9], [7, 4], [9, 7]],
        },
        "output": 1,
    },
    {
        "input": {
            "points": [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]],
        },
        "output": 3,
    },
]


@pytest.mark.sol1637
def test_run():
    for case in cases:
        assert (
            Solution.max_width_of_vertical_area(
                points=case["input"]["points"],
            )
            == case["output"]
        )
