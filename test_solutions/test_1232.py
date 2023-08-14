import pytest
from solutions.sol_1232 import Solution

cases = [
    {
        "input": {
            "coordinates": [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],
        },
        "output": True,
    },
    {
        "input": {
            "coordinates": [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]],
        },
        "output": False,
    },
]


@pytest.mark.sol1232
def test_run():
    for case in cases:
        assert (
            Solution.check_straight_line(
                coordinates=case["input"]["coordinates"],
            )
            == case["output"]
        )
