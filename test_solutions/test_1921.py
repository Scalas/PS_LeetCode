import pytest
from solutions.sol_1921 import Solution

cases = [
    {
        "input": {
            "dist": [1, 3, 4],
            "speed": [1, 1, 1],
        },
        "output": 3,
    },
    {
        "input": {
            "dist": [1, 1, 2, 3],
            "speed": [1, 1, 1, 1],
        },
        "output": 1,
    },
    {
        "input": {
            "dist": [3, 2, 4],
            "speed": [5, 3, 2],
        },
        "output": 1,
    },
]


@pytest.mark.sol1921
def test_run():
    for case in cases:
        assert (
            Solution.eliminate_maximum(
                dist=case["input"]["dist"], speed=case["input"]["speed"]
            )
            == case["output"]
        )
