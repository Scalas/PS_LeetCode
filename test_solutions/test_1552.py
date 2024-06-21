import pytest
from solutions.sol_1552 import Solution

cases = [
    {
        "input": {
            "position": [1, 2, 3, 4, 7],
            "m": 3,
        },
        "output": 3,
    },
    {
        "input": {
            "position": [5, 4, 3, 2, 1, 1000000000],
            "m": 2,
        },
        "output": 999999999,
    },
]


@pytest.mark.sol1552
def test_run():
    for case in cases:
        assert (
            Solution.max_distance(
                position=case["input"]["position"],
                m=case["input"]["m"],
            )
            == case["output"]
        )
