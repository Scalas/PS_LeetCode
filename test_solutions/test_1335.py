import pytest
from solutions.sol_1335 import Solution

cases = [
    {
        "input": {
            "job_difficulty": [6, 5, 4, 3, 2, 1],
            "d": 2,
        },
        "output": 7,
    },
    {
        "input": {
            "job_difficulty": [9, 9, 9],
            "d": 4,
        },
        "output": -1,
    },
    {
        "input": {
            "job_difficulty": [1, 1, 1],
            "d": 3,
        },
        "output": 3,
    },
    {
        "input": {
            "job_difficulty": [7, 1, 7, 1, 7, 1],
            "d": 3,
        },
        "output": 15,
    },
    {
        "input": {
            "job_difficulty": [11, 111, 22, 222, 33, 333, 44, 444],
            "d": 6,
        },
        "output": 843,
    },
]


@pytest.mark.sol1335
def test_run():
    for case in cases:
        assert (
            Solution.min_difficulty(
                job_difficulty=case["input"]["job_difficulty"],
                d=case["input"]["d"],
            )
            == case["output"]
        )
