import pytest

from solutions.sol_1043 import Solution

cases = [
    {
        "input": {
            "arr": [1, 15, 7, 9, 2, 5, 10],
            "k": 3,
        },
        "output": 84,
    },
    {
        "input": {
            "arr": [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3],
            "k": 4,
        },
        "output": 83,
    },
    {
        "input": {
            "arr": [1],
            "k": 1,
        },
        "output": 1,
    },
]


@pytest.mark.sol1043
def test_run():
    for case in cases:
        assert (
            Solution.max_sum_after_partitioning(
                arr=case["input"]["arr"], k=case["input"]["k"]
            )
            == case["output"]
        )
