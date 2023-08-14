import pytest
from solutions.sol_1319 import Solution

cases = [
    {
        "input": {
            "n": 4,
            "connections": [[0, 1], [0, 2], [1, 2]],
        },
        "output": 1,
    },
    {
        "input": {
            "n": 6,
            "connections": [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]],
        },
        "output": 2,
    },
    {
        "input": {
            "n": 6,
            "connections": [[0, 1], [0, 2], [0, 3], [1, 2]],
        },
        "output": -1,
    },
]


@pytest.mark.sol1319
def test_run():
    for case in cases:
        assert (
            Solution.make_connected(
                n=case["input"]["n"],
                connections=case["input"]["connections"],
            )
            == case["output"]
        )
