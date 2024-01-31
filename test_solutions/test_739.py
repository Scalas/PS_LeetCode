import pytest
from solutions.sol_739 import Solution

cases = [
    {
        "input": {
            "temperatures": [73, 74, 75, 71, 69, 72, 76, 73],
        },
        "output": [1, 1, 4, 2, 1, 1, 0, 0],
    },
    {
        "input": {
            "temperatures": [30, 40, 50, 60],
        },
        "output": [1, 1, 1, 0],
    },
    {
        "input": {
            "temperatures": [30, 60, 90],
        },
        "output": [1, 1, 0],
    },
]


@pytest.mark.sol_739
def test_run():
    for case in cases:
        assert (
            Solution.daily_temperatures(
                temperatures=case["input"]["temperatures"],
            )
            == case["output"]
        )
