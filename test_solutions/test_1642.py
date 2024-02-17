import pytest
from solutions.sol_1642 import Solution

cases = [
    {
        "input": {
            "heights": [4, 2, 7, 6, 9, 14, 12],
            "bricks": 5,
            "ladders": 1,
        },
        "output": 4,
    },
    {
        "input": {
            "heights": [4, 12, 2, 7, 3, 18, 20, 3, 19],
            "bricks": 10,
            "ladders": 2,
        },
        "output": 7,
    },
    {
        "input": {
            "heights": [14, 3, 19, 3],
            "bricks": 17,
            "ladders": 0,
        },
        "output": 3,
    },
]


@pytest.mark.sol1642
def test_run():
    for case in cases:
        assert (
            Solution.furthest_building(
                heights=case["input"]["heights"],
                bricks=case["input"]["bricks"],
                ladders=case["input"]["ladders"],
            )
            == case["output"]
        )
