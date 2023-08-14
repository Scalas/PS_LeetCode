import pytest
from solutions.sol_2187 import Solution

cases = [
    {
        "input": {
            "time": [1, 2, 3],
            "total_trips": 5,
        },
        "output": 3,
    },
    {
        "input": {
            "time": [2],
            "total_trips": 1,
        },
        "output": 2,
    },
]


@pytest.mark.sol_2187
def test_run():
    for case in cases:
        assert (
            Solution.minimum_time(
                time=case["input"]["time"],
                total_trips=case["input"]["total_trips"],
            )
            == case["output"]
        )
