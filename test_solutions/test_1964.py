import pytest
from solutions.sol_1964 import Solution

cases = [
    {
        "input": {
            "obstacles": [1, 2, 3, 2],
        },
        "output": [1, 2, 3, 3],
    },
    {
        "input": {
            "obstacles": [2, 2, 1],
        },
        "output": [1, 2, 1],
    },
    {
        "input": {
            "obstacles": [3, 1, 5, 6, 4, 2],
        },
        "output": [1, 1, 2, 3, 2, 2],
    },
]


@pytest.mark.sol1964
def test_run():
    for case in cases:
        assert (
            Solution.longest_obstacle_course_at_each_position(
                obstacles=case["input"]["obstacles"],
            )
            == case["output"]
        )
