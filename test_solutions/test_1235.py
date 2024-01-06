import pytest
from solutions.sol_1235 import Solution

cases = [
    {
        "input": {
            "startTime": [1, 2, 3, 3],
            "endTime": [3, 4, 5, 6],
            "profit": [50, 10, 40, 70],
        },
        "output": 120,
    },
    {
        "input": {
            "startTime": [1, 2, 3, 4, 6],
            "endTime": [3, 5, 10, 6, 9],
            "profit": [20, 20, 100, 70, 60],
        },
        "output": 150,
    },
    {
        "input": {
            "startTime": [1, 1, 1],
            "endTime": [2, 3, 4],
            "profit": [5, 6, 4],
        },
        "output": 6,
    },
]


@pytest.mark.sol1235
def test_run():
    for case in cases:
        assert (
            Solution.job_scheduling(
                startTime=case["input"]["startTime"],
                endTime=case["input"]["endTime"],
                profit=case["input"]["profit"],
            )
            == case["output"]
        )
