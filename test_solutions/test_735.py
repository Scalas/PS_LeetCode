import pytest
from solutions.sol_735 import Solution

cases = [
    {
        "input": {
            "asteroids": [5, 10, -5],
        },
        "output": [5, 10],
    },
    {
        "input": {
            "asteroids": [8, -8],
        },
        "output": [],
    },
    {
        "input": {
            "asteroids": [10, 2, -5],
        },
        "output": [10],
    },
]


@pytest.mark.sol_735
def test_run():
    for case in cases:
        assert (
            Solution.asteroid_collision(
                asteroids=case["input"]["asteroids"],
            )
            == case["output"]
        )
