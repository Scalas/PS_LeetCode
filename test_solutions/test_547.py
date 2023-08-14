import pytest
from solutions.sol_547 import Solution

cases = [
    {
        "input": {
            "is_connected": [[1, 1, 0], [1, 1, 0], [0, 0, 1]],
        },
        "output": 2,
    },
    {
        "input": {
            "is_connected": [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        },
        "output": 3,
    },
]


@pytest.mark.sol_547
def test_run():
    for case in cases:
        assert (
            Solution.find_circle_num(is_connected=case["input"]["is_connected"])
            == case["output"]
        )
